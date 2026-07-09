# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:23:46 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup Figure and Layout (2x1 Subplots) ---
fig, axs = plt.subplots(2, 1, figsize=(10, 14), facecolor='white')

# ==================== Panel A: H-T Phase Diagram for Type I vs Type II ====================
ax1 = axs[0]

# --- Schematic H-T Plot ---
# Temperature scale
T = np.linspace(0, 1.2, 500)
T_c = 1.0

# Type I (Normal vs Super)
H_c = 1.0 * (1 - (T/T_c)**2)
H_c[H_c < 0] = 0

# Type II (Normal, Mixed, Super)
H_c1 = 0.3 * (1 - (T/T_c)**2) # Lower Critical Field
H_c1[H_c1 < 0] = 0
H_c2 = 2.5 * (1 - (T/T_c)**2) # Upper Critical Field
H_c2[H_c2 < 0] = 0

# --- Plotting Type I ---
ax1.plot(T, H_c, label='Type I ($H_c$)', color='#7f8c8d', linewidth=2.5, linestyle=':')
ax1.fill_between(T, 0, H_c, color='#bdc3c7', alpha=0.3)
ax1.text(0.4, 0.4, 'Type I\nSuper', fontsize=10, ha='center', color='#7f8c8d')

# --- Plotting Type II ---
ax1.plot(T, H_c1, label='Type II ($H_{c1}$)', color='#c0392b', linewidth=2.5)
ax1.plot(T, H_c2, label='Type II ($H_{c2}$)', color='#2980b9', linewidth=2.5)

# Fill Mixed State
ax1.fill_between(T, H_c1, H_c2, color='#3498db', alpha=0.2)
ax1.text(0.4, 1.3, 'Type II: Mixed State\n(Vortex Lattice, $H_{c1} < H < H_{c2}$)', fontsize=12, ha='center', fontweight='bold', color='#2980b9')

# Fill Super State (Below Hc1)
ax1.fill_between(T, 0, H_c1, color='#e74c3c', alpha=0.1)
ax1.text(0.2, 0.1, 'Type II\nMeissner\n($H < H_{c1}$)', fontsize=10, ha='center', color='#c0392b')

# Normal State (Above Hc, Hc2)
ax1.text(0.9, 2.0, 'Normal State', fontsize=11, ha='center', color='black')

# Formatting Panel A
ax1.set_title('Superconductor Phase Diagrams ($H$ vs $T$)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Temperature $T / T_c$', fontsize=12)
ax1.set_ylabel('Magnetic Field $H / H_c(0)$ or $H_{c2}(0)$', fontsize=12)
ax1.set_xlim(0, 1.2)
ax1.set_ylim(0, 2.8)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(1.0, color='black', linewidth=1.5, linestyle='--', label='$T_c$ Boundary')
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right', fontsize=10)

# ==================== Panel B: Abrikosov Vortex Lattice (Mixed State) ====================
ax2 = axs[1]
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

# Title for Panel B
ax2.text(5, 9.2, "Abrikosov Vortex Lattice Structure (Type II Mixed State)", 
        fontsize=16, fontweight='bold', ha='center', color='#2980b9')

# --- 1. Draw Superconducting Bulk Plane (Blue base) ---
bulk = patches.Rectangle((0.5, 0.5), 9.0, 8.0, edgecolor='#2c3e50', facecolor='#e8f4f8', linewidth=1.5, zorder=1)
ax2.add_patch(bulk)
ax2.text(1.5, 8.0, 'Superconducting Bulk\n(Mixed State)', fontsize=10, fontweight='bold', ha='center', zorder=2)

# --- 2. Generate Hexagonal Grid Points for Vortices ---
n_rows = 5
n_cols = 6
x_start = 1.5
y_start = 2.0
dx = 1.6
dy = 1.4

# Create grid points
points = []
for r in range(n_rows):
    offset = (dx / 2.0) if (r % 2 == 1) else 0.0
    for c in range(n_cols):
        points.append((x_start + c * dx + offset, y_start + r * dy))

# --- 3. Draw Individual Vortices (Quantized Flux Tubes) ---
# Vortex visual settings
vortex_radius = 0.5
inner_core_radius = 0.15 # Coherence Length xi
outer_decay_radius = 0.7  # Penetration Length lambda

# Colors matching G-L description
core_color = '#e74c3c'   # Normal Core (xi)
vortex_blue = '#3498db'  # Superconducting context
arrow_color = '#c0392b'  # Red for magnetic field lines

for p in points:
    px, py = p
    
    # Outer Decay ring (lambda decay of B-field)
    vortex_decay = patches.Circle((px, py), outer_decay_radius, facecolor=vortex_blue, alpha=0.15, zorder=2)
    ax2.add_patch(vortex_decay)

    # Main Vortex circle
    vortex_main = patches.Circle((px, py), vortex_radius, edgecolor='#2c3e50', facecolor='white', alpha=0.7, zorder=3)
    ax2.add_patch(vortex_main)
    
    # Draw field lines exiting the page (red dots)
    # 4 dots around center
    dot_offset = 0.2
    for dx_dot, dy_dot in [(-dot_offset, -dot_offset), (-dot_offset, dot_offset), 
                           (dot_offset, -dot_offset), (dot_offset, dot_offset)]:
        ax2.scatter(px + dx_dot, py + dy_dot, color=arrow_color, s=20, marker='.', zorder=6)

    # Inner Normal Core (coherence length xi)
    vortex_core = patches.Circle((px, py), inner_core_radius, edgecolor='#c0392b', facecolor=core_color, linewidth=1, zorder=5)
    ax2.add_patch(vortex_core)
    ax2.text(px, py, '$\Phi_0$', fontsize=9, ha='center', va='center', fontweight='bold', color='white', zorder=7)

# --- 4. Explanatory Annotations ---
# Label fundamental lengths xi and lambda on a single vortex
sample_vortex = points[11] # Pick a visible one
sx, sy = sample_vortex

# lambda pointer
ax2.annotate('$\lambda$ (Penetration Depth)\nDecay of $B$ and $J_s$', 
             xy=(sx + vortex_radius, sy), xytext=(sx + 3.0, sy + 0.5),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2', lw=1.2),
             ha='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# xi pointer
ax2.annotate('$\xi$ (Coherence Length)\nNormal Core radius', 
             xy=(sx - 0.05, sy + inner_core_radius), xytext=(sx - 2.5, sy + 1.2),
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=-.2', lw=1.2),
             ha='right', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

# Spacing annotation a_0
ax2.plot([sx, sx + dx], [sy - vortex_radius - 0.1, sy - vortex_radius - 0.1], color='black', linewidth=1, marker='|')
ax2.text(sx + dx/2.0, sy - vortex_radius - 0.5, 'Hexagonal Spacing $a_0 \propto 1/\sqrt{B}$', ha='center', fontsize=10, zorder=10)

plt.tight_layout()
plt.savefig('gl_phase_vortex_diagram.png', dpi=300)
plt.close()
print("GL diagrams generated successfully.")