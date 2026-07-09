# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:42:57 2026

@author: Straight A
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Create a schematic diagram comparing an Ideal Conductor vs a Superconductor
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

def draw_scene(ax, title, state, has_field_inside):
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=10)
    
    if state == 'Normal':
        color = '#d3d3d3'
        label = 'Normal State\n(R > 0)'
    elif state == 'Super':
        color = '#3498db'
        label = 'Superconductor\n(R = 0, B = 0)'
    else:
        color = '#2ecc71'
        label = 'Ideal Conductor\n(R = 0)'
        
    rect = patches.Circle((0, 0), 0.8, edgecolor='black', facecolor=color, linewidth=2, zorder=3)
    ax.add_patch(rect)
    ax.text(0, 0, label, ha='center', va='center', fontsize=10, fontweight='bold', zorder=4)
    
    y_lines = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
    for y in y_lines:
        if has_field_inside:
            ax.plot([-2, 2], [y, y], color='red', linestyle='-', linewidth=1.5, zorder=1)
        else:
            if abs(y) < 0.8:
                sign = 1 if y >= 0 else -1
                x = np.linspace(-2, 2, 100)
                bump = 0.9 * np.exp(-x**2 * 2)  # Adjust bump for better visual
                if y == 0:
                    bump = 1.0 * np.exp(-x**2 * 2)
                    # Split zero line into two lines curving up and down
                    ax.plot(x, bump, color='red', linestyle='-', linewidth=1.5, zorder=1)
                    ax.plot(x, -bump, color='red', linestyle='-', linewidth=1.5, zorder=1)
                else:
                    ax.plot(x, y + sign * bump, color='red', linestyle='-', linewidth=1.5, zorder=1)
            else:
                ax.plot([-2, 2], [y, y], color='red', linestyle='-', linewidth=1.5, zorder=1)

# Row 1: Field applied at high T, then cooled
draw_scene(axs[0, 0], "1. Ideal Conductor (R=0)\n[Cooled inside a Magnetic Field]", "Ideal", has_field_inside=True)
axs[0, 0].text(0, -1.9, "Field gets TRAPPED inside.\nFaraday's Law: d\u03A6/dt = 0", fontsize=11, ha='center', bbox=dict(facecolor='yellow', alpha=0.3))

draw_scene(axs[0, 1], "2. Superconductor (Meissner Effect)\n[Cooled inside a Magnetic Field]", "Super", has_field_inside=False)
axs[0, 1].text(0, -1.9, "Field is ACTIVELY EXPELLED!\nMacroscopic Quantum State: B = 0", fontsize=11, ha='center', bbox=dict(facecolor='yellow', alpha=0.3))

# Row 2: Cooled first in zero field, then field applied
draw_scene(axs[1, 0], "3. Ideal Conductor (R=0)\n[Field applied AFTER cooling]", "Ideal", has_field_inside=False)
axs[1, 0].text(0, -1.9, "Field is EXCLUDED by surface currents.\n(Responds to change in field)", fontsize=11, ha='center', bbox=dict(facecolor='yellow', alpha=0.3))

draw_scene(axs[1, 1], "4. Superconductor (Meissner Effect)\n[Field applied AFTER cooling]", "Super", has_field_inside=False)
axs[1, 1].text(0, -1.9, "Field is EXCLUDED.\n(Thermodynamic Ground State)", fontsize=11, ha='center', bbox=dict(facecolor='yellow', alpha=0.3))

plt.suptitle("The Crucial Difference: Perfect Conductor vs. Superconductor", fontsize=18, fontweight='bold', y=0.98)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('zero_resistance_vs_superconductor.png', dpi=300)
plt.close()
print("Comparison graph generated successfully.")