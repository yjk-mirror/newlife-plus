#!/usr/bin/env python3
"""
Newlife Dev Tools — Save file editor / cheat engine

Usage:
  python tools/newlife_cheat.py              # auto-finds latest save
  python tools/newlife_cheat.py save.json    # load specific save

Workflow:
  1. In-game: Save game
  2. Tool auto-detects the new save (or press Reload)
  3. Edit values in the tool
  4. Click APPLY CHANGES — tool writes back to save file
  5. In-game: Load save to pick up changes
"""

import json
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
from pathlib import Path
from datetime import datetime
from copy import deepcopy

# ── Constants ─────────────────────────────────────────────────────────────────

SAVE_DIR = Path(__file__).parent.parent / "newlife_gamedata" / "saves"

PC_TRAITS_KNOWN = sorted([
    # Personality
    "POSH", "CUTE", "SULTRY", "DOWN_TO_EARTH", "BITCHY", "SHY",
    "REFINED", "ROMANTIC", "FLIRTY", "AMBITIOUS", "OVERACTIVE_IMAGINATION", "PLAIN",
    # Transformation
    "ALWAYS_FEMALE", "NOT_TRANSFORMED",
    # Content gating
    "BLOCK_ROUGH", "LIKES_ROUGH",
    # Other
    "HIGH_WILLPOWER", "STRONG_WILLED",
])

FIGURE_OPTIONS   = ["SLIM", "TONED", "WOMANLY"]
BREASTS_OPTIONS  = ["FLAT", "SMALL", "MEDIUM", "MEDIUM_LARGE", "LARGE", "HUGE"]
PERSONALITY_OPTIONS = ["JERK", "SELFISH", "AVERAGE", "ROMANTIC", "CARING"]
RELATIONSHIP_TYPES  = ["STRANGER", "ACQUAINTANCE", "FRIEND", "LOVER", "PARTNER", "EX"]

SKILLS = ["FITNESS", "FEMININITY", "CHARM", "FASHION", "ADMIN",
          "MANAGEMENT", "COOKING", "DANCE", "CHILDCARE"]

NPC_REL_FIELDS = [
    ("PC → NPC Like",        "wLike",                   -100, 100),
    ("PC → NPC Love",        "wLove",                      0, 100),
    ("NPC → PC Like",        "npcLike",                 -100, 100),
    ("NPC → PC Love",        "npcLove",                    0, 100),
    ("NPC attraction → PC",  "npcCalculatedAttraction",    0, 100),
    ("PC attraction → NPC",  "wAttraction",                0, 100),
    ("Knowledge",            "knowledge",                  0, 100),
]


# ── Helpers ───────────────────────────────────────────────────────────────────

def find_latest_save():
    if not SAVE_DIR.exists():
        return None
    saves = list(SAVE_DIR.glob("*.json"))
    return max(saves, key=lambda p: p.stat().st_mtime) if saves else None


# ── Main application ──────────────────────────────────────────────────────────

class CheatEngine:
    def __init__(self, root, save_path=None):
        self.root = root
        self.root.title("Newlife Dev Tools")
        self.root.geometry("1020x740")
        self.root.minsize(800, 600)

        self.save_path = Path(save_path) if save_path else find_latest_save()
        self.data = None
        self.original_data = None
        self._last_mtime = None
        self._watch_running = True

        self._build_ui()

        if self.save_path:
            self.load_save(self.save_path)

        t = threading.Thread(target=self._file_watch_loop, daemon=True)
        t.start()

    # ── UI layout ─────────────────────────────────────────────────────────────

    def _build_ui(self):
        # Top bar: file path + controls
        top = tk.Frame(self.root, pady=4, padx=8)
        top.pack(fill=tk.X, side=tk.TOP)

        tk.Label(top, text="Save:").pack(side=tk.LEFT)
        self.path_var = tk.StringVar(value=str(self.save_path or ""))
        tk.Entry(top, textvariable=self.path_var, width=55).pack(side=tk.LEFT, padx=4)
        tk.Button(top, text="Browse",  command=self._browse).pack(side=tk.LEFT)
        tk.Button(top, text="↺ Reload", command=lambda: self.load_save(self.path_var.get())).pack(side=tk.LEFT, padx=4)

        self.auto_var = tk.BooleanVar(value=True)
        tk.Checkbutton(top, text="Auto-reload on game save", variable=self.auto_var).pack(side=tk.LEFT, padx=8)

        # Bottom bar: apply button + status
        self.status_var = tk.StringVar(value="No save loaded")
        tk.Label(self.root, textvariable=self.status_var, anchor=tk.W,
                 relief=tk.SUNKEN, padx=6, pady=2).pack(fill=tk.X, side=tk.BOTTOM)

        btn_row = tk.Frame(self.root, pady=6, padx=8)
        btn_row.pack(fill=tk.X, side=tk.BOTTOM)

        tk.Button(btn_row, text="▶  APPLY CHANGES", bg="#2d6a2d", fg="white",
                  font=("", 11, "bold"), padx=12, pady=4,
                  command=self._apply).pack(side=tk.LEFT)
        tk.Button(btn_row, text="Reset to loaded", command=self._reset).pack(side=tk.LEFT, padx=8)
        self.apply_label = tk.Label(btn_row, text="", fg="gray")
        self.apply_label.pack(side=tk.LEFT)

        # Notebook
        nb = ttk.Notebook(self.root)
        nb.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

        self._char_frame  = ttk.Frame(nb)
        self._world_frame = ttk.Frame(nb)
        self._npc_frame   = ttk.Frame(nb)

        nb.add(self._char_frame,  text="  Character  ")
        nb.add(self._world_frame, text="  Flags & Stats  ")
        nb.add(self._npc_frame,   text="  NPCs  ")

        self._build_char_tab()
        self._build_world_tab()
        self._build_npc_tab()

    # ── Character tab ─────────────────────────────────────────────────────────

    def _build_char_tab(self):
        f = self._char_frame

        # ── Left column: skills + vitals + appearance
        left = tk.Frame(f)
        left.pack(side=tk.LEFT, fill=tk.BOTH, padx=(12, 4), pady=8)

        row = 0
        tk.Label(left, text="SKILLS", font=("", 10, "bold")).grid(
            row=row, column=0, columnspan=3, sticky=tk.W, pady=(0, 2))
        row += 1
        tk.Label(left, text="Value",    fg="gray", width=7).grid(row=row, column=1)
        tk.Label(left, text="Modifier", fg="gray", width=7).grid(row=row, column=2)
        row += 1

        self._skill_vars = {}
        for skill in SKILLS:
            tk.Label(left, text=skill, width=14, anchor=tk.W).grid(
                row=row, column=0, sticky=tk.W, pady=2)
            val_var = tk.IntVar()
            mod_var = tk.IntVar()
            tk.Spinbox(left, from_=-999, to=999, textvariable=val_var, width=7).grid(
                row=row, column=1, padx=4)
            tk.Spinbox(left, from_=-999, to=999, textvariable=mod_var, width=7).grid(
                row=row, column=2, padx=4)
            self._skill_vars[skill] = (val_var, mod_var)
            row += 1

        ttk.Separator(left, orient=tk.HORIZONTAL).grid(
            row=row, column=0, columnspan=3, sticky=tk.EW, pady=6)
        row += 1

        tk.Label(left, text="VITALS", font=("", 10, "bold")).grid(
            row=row, column=0, columnspan=3, sticky=tk.W)
        row += 1

        self._vital_vars = {}
        for label, key, lo, hi in [("Money", "money", -99999, 999999),
                                    ("Stress", "stress", 0, 100)]:
            tk.Label(left, text=label, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=2)
            var = tk.IntVar()
            tk.Spinbox(left, from_=lo, to=hi, textvariable=var, width=10).grid(
                row=row, column=1, columnspan=2, sticky=tk.W, padx=4)
            self._vital_vars[key] = var
            row += 1

        ttk.Separator(left, orient=tk.HORIZONTAL).grid(
            row=row, column=0, columnspan=3, sticky=tk.EW, pady=6)
        row += 1

        tk.Label(left, text="APPEARANCE", font=("", 10, "bold")).grid(
            row=row, column=0, columnspan=3, sticky=tk.W)
        row += 1

        self._figure_var = tk.StringVar()
        self._breasts_var = tk.StringVar()

        for label, var, opts in [("Figure",  self._figure_var,  FIGURE_OPTIONS),
                                  ("Breasts", self._breasts_var, BREASTS_OPTIONS)]:
            tk.Label(left, text=label, anchor=tk.W).grid(row=row, column=0, sticky=tk.W, pady=2)
            ttk.Combobox(left, textvariable=var, values=opts, state="readonly", width=14).grid(
                row=row, column=1, columnspan=2, sticky=tk.W, padx=4)
            row += 1

        # ── Right column: traits
        right = tk.LabelFrame(f, text=" TRAITS ", padx=6, pady=4)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(4, 12), pady=8)

        self._trait_vars = {}
        for i, trait in enumerate(PC_TRAITS_KNOWN):
            var = tk.BooleanVar()
            tk.Checkbutton(right, text=trait, variable=var, anchor=tk.W).grid(
                row=i // 2, column=i % 2, sticky=tk.W, padx=6, pady=1)
            self._trait_vars[trait] = var

        sep_row = (len(PC_TRAITS_KNOWN) + 1) // 2
        ttk.Separator(right, orient=tk.HORIZONTAL).grid(
            row=sep_row, column=0, columnspan=2, sticky=tk.EW, pady=6)

        tk.Label(right, text="Add custom trait:").grid(
            row=sep_row + 1, column=0, columnspan=2, sticky=tk.W)

        custom_row = tk.Frame(right)
        custom_row.grid(row=sep_row + 2, column=0, columnspan=2, sticky=tk.W, pady=2)
        self._custom_trait_var = tk.StringVar()
        tk.Entry(custom_row, textvariable=self._custom_trait_var, width=18).pack(side=tk.LEFT)
        tk.Button(custom_row, text="Add", command=self._add_custom_trait).pack(side=tk.LEFT, padx=4)

        tk.Label(right, text="Other active traits:").grid(
            row=sep_row + 3, column=0, columnspan=2, sticky=tk.W)
        self._custom_traits_lb = tk.Listbox(right, height=4, width=28)
        self._custom_traits_lb.grid(row=sep_row + 4, column=0, columnspan=2, sticky=tk.W, pady=2)
        tk.Button(right, text="Remove selected",
                  command=self._remove_custom_trait).grid(
            row=sep_row + 5, column=0, columnspan=2, sticky=tk.W)

    # ── Flags & Stats tab ─────────────────────────────────────────────────────

    def _build_world_tab(self):
        f = self._world_frame

        # ── Left: game flags
        left = tk.LabelFrame(f, text=" GAME FLAGS ", padx=6, pady=4)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12, 4), pady=8)

        sb = tk.Scrollbar(left)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self._flags_lb = tk.Listbox(left, yscrollcommand=sb.set, width=40, height=22)
        self._flags_lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb.config(command=self._flags_lb.yview)

        add_row = tk.Frame(f)
        add_row.pack(side=tk.LEFT, anchor=tk.N, padx=4, pady=(80, 0))
        self._new_flag_var = tk.StringVar()
        tk.Entry(add_row, textvariable=self._new_flag_var, width=28).pack(pady=2)
        tk.Button(add_row, text="Add Flag",      command=self._add_flag).pack(fill=tk.X, pady=2)
        tk.Button(add_row, text="Remove Selected", command=self._remove_flag).pack(fill=tk.X, pady=2)

        # ── Right: stats
        right = tk.LabelFrame(f, text=" STATS  (double-click to edit) ", padx=6, pady=4)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(4, 12), pady=8)

        sb2 = tk.Scrollbar(right)
        sb2.pack(side=tk.RIGHT, fill=tk.Y)
        self._stats_tree = ttk.Treeview(right, columns=("Stat", "Value"),
                                        show="headings", height=22,
                                        yscrollcommand=sb2.set)
        self._stats_tree.heading("Stat",  text="Stat")
        self._stats_tree.heading("Value", text="Value")
        self._stats_tree.column("Stat",  width=240)
        self._stats_tree.column("Value", width=80)
        self._stats_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        sb2.config(command=self._stats_tree.yview)
        self._stats_tree.bind("<Double-1>", self._edit_stat)
        self._stats = {}

    # ── NPCs tab ──────────────────────────────────────────────────────────────

    def _build_npc_tab(self):
        f = self._npc_frame

        # Selector row
        sel_row = tk.Frame(f)
        sel_row.pack(fill=tk.X, padx=12, pady=(10, 4))
        tk.Label(sel_row, text="NPC:").pack(side=tk.LEFT)
        self._npc_var = tk.StringVar()
        self._npc_combo = ttk.Combobox(sel_row, textvariable=self._npc_var,
                                       state="readonly", width=35)
        self._npc_combo.pack(side=tk.LEFT, padx=6)
        self._npc_combo.bind("<<ComboboxSelected>>", self._on_npc_selected)

        detail = tk.Frame(f)
        detail.pack(fill=tk.BOTH, expand=True, padx=12)

        # ── Left: relationship values
        left = tk.LabelFrame(detail, text=" RELATIONSHIP ", padx=8, pady=6)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 8), pady=4)

        self._rel_vars = {}
        for i, (label, key, lo, hi) in enumerate(NPC_REL_FIELDS):
            tk.Label(left, text=label, anchor=tk.W, width=24).grid(
                row=i, column=0, sticky=tk.W, pady=3)
            var = tk.IntVar()
            tk.Spinbox(left, from_=lo, to=hi, textvariable=var, width=7).grid(
                row=i, column=1, padx=6)
            self._rel_vars[key] = var

        n = len(NPC_REL_FIELDS)
        tk.Label(left, text="Contactable", anchor=tk.W).grid(
            row=n, column=0, sticky=tk.W, pady=3)
        self._contactable_var = tk.BooleanVar()
        tk.Checkbutton(left, variable=self._contactable_var).grid(row=n, column=1, sticky=tk.W)

        tk.Label(left, text="Relationship type", anchor=tk.W).grid(
            row=n+1, column=0, sticky=tk.W, pady=3)
        self._reltype_var = tk.StringVar()
        ttk.Combobox(left, textvariable=self._reltype_var,
                     values=RELATIONSHIP_TYPES, state="readonly", width=14).grid(
            row=n+1, column=1, sticky=tk.W, padx=6)

        # ── Right: personality + traits
        right = tk.LabelFrame(detail, text=" PERSONALITY & TRAITS ", padx=8, pady=6)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, pady=4)

        tk.Label(right, text="Personality:").pack(anchor=tk.W)
        self._npc_personality_var = tk.StringVar()
        ttk.Combobox(right, textvariable=self._npc_personality_var,
                     values=PERSONALITY_OPTIONS, state="readonly", width=14).pack(
            anchor=tk.W, pady=(0, 8))

        tk.Label(right, text="Traits (read-only):").pack(anchor=tk.W)
        self._npc_traits_lb = tk.Listbox(right, width=30, height=18)
        self._npc_traits_lb.pack(fill=tk.BOTH, expand=True)

        self._all_npcs = []
        self._current_npc_idx = None

    # ── Data: load & populate ─────────────────────────────────────────────────

    def load_save(self, path):
        path = Path(path)
        if not path.exists():
            self.status_var.set(f"File not found: {path}")
            return
        try:
            with open(path, encoding="utf-8") as fh:
                self.data = json.load(fh)
            self.original_data = deepcopy(self.data)
            self.save_path = path
            self.path_var.set(str(path))
            self._last_mtime = path.stat().st_mtime
            self._populate_ui()
            name = self.data.get("player", {}).get("name", "?")
            week = self.data.get("weekNum", "?")
            self.status_var.set(
                f"{name} — Week {week} — Loaded {datetime.now().strftime('%H:%M:%S')} — {path.name}")
            self.root.title(f"Newlife Dev Tools — {name} (Week {week})")
        except Exception as e:
            self.status_var.set(f"Load error: {e}")

    def _populate_ui(self):
        if not self.data:
            return
        p = self.data["player"]

        # Skills
        skills_data = p.get("skills", {})
        for skill, (val_var, mod_var) in self._skill_vars.items():
            entry = skills_data.get(skill, {})
            val_var.set(entry.get("value", 0) if isinstance(entry, dict) else 0)
            mod_var.set(entry.get("modifier", 0) if isinstance(entry, dict) else 0)

        # Vitals
        self._vital_vars["money"].set(p.get("money", 0))
        self._vital_vars["stress"].set(p.get("stress", 0))

        # Appearance
        self._figure_var.set(p.get("figure", "SLIM"))
        self._breasts_var.set(p.get("breasts", "MEDIUM"))

        # Traits
        active = set(p.get("traits", []))
        for trait, var in self._trait_vars.items():
            var.set(trait in active)
        self._custom_traits_lb.delete(0, tk.END)
        for t in sorted(active):
            if t not in self._trait_vars:
                self._custom_traits_lb.insert(tk.END, t)

        # Flags
        self._flags_lb.delete(0, tk.END)
        for flag in sorted(self.data.get("gameFlags", [])):
            self._flags_lb.insert(tk.END, flag)

        # Stats
        self._stats_tree.delete(*self._stats_tree.get_children())
        self._stats = dict(self.data.get("stats", {}))
        for k, v in sorted(self._stats.items()):
            self._stats_tree.insert("", tk.END, iid=k, values=(k, v))

        # NPCs
        self._all_npcs = []
        for npc in self.data.get("maleNpcs", []):
            self._all_npcs.append(("m", npc.get("name", "?"), npc.get("personality", ""), npc))
        for npc in self.data.get("femaleNpcs", []):
            self._all_npcs.append(("f", npc.get("name", "?"), npc.get("personality", ""), npc))

        labels = [f"{'♂' if g == 'm' else '♀'} {n}  ({pers})"
                  for g, n, pers, _ in self._all_npcs]
        self._npc_combo["values"] = labels
        if labels:
            self._npc_combo.current(0)
            self._on_npc_selected(None)

    def _on_npc_selected(self, _event):
        idx = self._npc_combo.current()
        if idx < 0 or not self._all_npcs:
            return
        self._current_npc_idx = idx
        _g, _n, _pers, npc = self._all_npcs[idx]

        self._npc_personality_var.set(npc.get("personality", "AVERAGE"))
        self._npc_traits_lb.delete(0, tk.END)
        for t in npc.get("traits", []):
            self._npc_traits_lb.insert(tk.END, t)

        rel = npc.get("relationship") or {}
        for key, var in self._rel_vars.items():
            var.set(int(rel.get(key, 0) or 0))
        self._contactable_var.set(bool(rel.get("contactable", False)))
        self._reltype_var.set(rel.get("relationshipType", "STRANGER"))

    # ── Apply / Reset ─────────────────────────────────────────────────────────

    def _apply(self):
        if not self.data:
            messagebox.showwarning("No save loaded", "Load a save file first.")
            return
        try:
            self._write_ui_to_data()
            with open(self.save_path, "w", encoding="utf-8") as fh:
                json.dump(self.data, fh, indent=2)
            self._last_mtime = self.save_path.stat().st_mtime
            ts = datetime.now().strftime("%H:%M:%S")
            self.apply_label.config(text=f"Written {ts}", fg="green")
            self.status_var.set(
                f"Applied {ts} — Load save in-game to take effect — {self.save_path.name}")
        except Exception as e:
            messagebox.showerror("Apply failed", str(e))

    def _write_ui_to_data(self):
        p = self.data["player"]

        # Skills
        if "skills" not in p:
            p["skills"] = {}
        for skill, (val_var, mod_var) in self._skill_vars.items():
            p["skills"][skill] = {"value": val_var.get(), "modifier": mod_var.get()}

        # Vitals + appearance
        p["money"]   = self._vital_vars["money"].get()
        p["stress"]  = self._vital_vars["stress"].get()
        p["figure"]  = self._figure_var.get()
        p["breasts"] = self._breasts_var.get()

        # Traits
        traits = [t for t, var in self._trait_vars.items() if var.get()]
        traits += list(self._custom_traits_lb.get(0, tk.END))
        p["traits"] = traits

        # Flags
        self.data["gameFlags"] = list(self._flags_lb.get(0, tk.END))

        # Stats
        self.data["stats"] = dict(self._stats)

        # Current NPC (if one is selected and was modified)
        if self._current_npc_idx is not None:
            _g, _n, _pers, npc = self._all_npcs[self._current_npc_idx]
            npc["personality"] = self._npc_personality_var.get()
            rel = npc.get("relationship") or {}
            for key, var in self._rel_vars.items():
                rel[key] = var.get()
            rel["contactable"]      = self._contactable_var.get()
            rel["relationshipType"] = self._reltype_var.get()
            npc["relationship"] = rel

    def _reset(self):
        if self.original_data:
            self.data = deepcopy(self.original_data)
            self._populate_ui()
            self.apply_label.config(text="Reset", fg="gray")

    # ── UI helpers ────────────────────────────────────────────────────────────

    def _browse(self):
        path = filedialog.askopenfilename(
            initialdir=str(SAVE_DIR),
            filetypes=[("JSON saves", "*.json"), ("All", "*.*")])
        if path:
            self.load_save(path)

    def _add_flag(self):
        flag = self._new_flag_var.get().strip().upper()
        existing = list(self._flags_lb.get(0, tk.END))
        if flag and flag not in existing:
            # Insert sorted
            existing.append(flag)
            existing.sort()
            self._flags_lb.delete(0, tk.END)
            for f in existing:
                self._flags_lb.insert(tk.END, f)
        self._new_flag_var.set("")

    def _remove_flag(self):
        for i in reversed(self._flags_lb.curselection()):
            self._flags_lb.delete(i)

    def _add_custom_trait(self):
        trait = self._custom_trait_var.get().strip().upper()
        if not trait:
            return
        if trait in self._trait_vars:
            self._trait_vars[trait].set(True)
        elif trait not in list(self._custom_traits_lb.get(0, tk.END)):
            self._custom_traits_lb.insert(tk.END, trait)
        self._custom_trait_var.set("")

    def _remove_custom_trait(self):
        for i in reversed(self._custom_traits_lb.curselection()):
            self._custom_traits_lb.delete(i)

    def _edit_stat(self, _event):
        sel = self._stats_tree.selection()
        if not sel:
            return
        key = sel[0]
        current = self._stats.get(key, 0)

        dlg = tk.Toplevel(self.root)
        dlg.title(f"Edit stat: {key}")
        dlg.geometry("260x110")
        dlg.transient(self.root)
        dlg.grab_set()
        dlg.resizable(False, False)

        tk.Label(dlg, text=key, font=("", 9, "bold")).pack(pady=(10, 2))
        var = tk.IntVar(value=current)
        sb = tk.Spinbox(dlg, from_=-999999, to=999999, textvariable=var, width=14)
        sb.pack()
        sb.focus_set()

        def save_stat():
            self._stats[key] = var.get()
            self._stats_tree.item(key, values=(key, var.get()))
            dlg.destroy()

        tk.Button(dlg, text="OK", command=save_stat).pack(pady=6)
        dlg.bind("<Return>", lambda _: save_stat())

    # ── File watcher ──────────────────────────────────────────────────────────

    def _file_watch_loop(self):
        while self._watch_running:
            time.sleep(2)
            if not self.auto_var.get() or not self.save_path:
                continue
            try:
                mtime = self.save_path.stat().st_mtime
                if self._last_mtime and mtime > self._last_mtime:
                    # Schedule reload on the main thread
                    self.root.after(0, lambda: self.load_save(self.save_path))
            except FileNotFoundError:
                pass

    def on_close(self):
        self._watch_running = False
        self.root.destroy()


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    root = tk.Tk()
    save_path = sys.argv[1] if len(sys.argv) > 1 else None
    app = CheatEngine(root, save_path)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()


if __name__ == "__main__":
    main()
