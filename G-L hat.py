# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:19:25 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 6), facecolor='white')

# --- Panel 1: 1D Free Energy vs Temperature ---
ax1 = fig.add_subplot(121)
psi = np.linspace(-2.5, 2.5, 500)
beta = 1.0

# T > Tc (alpha > 0)
alpha_high = 1.0
f_high = alpha_high * psi**2 + (beta/2) * psi**4
ax1.plot(psi, f_high, label='$T > T_c$ (Normal State)', color='#7f8c8d', linewidth=2.5)

# T = Tc (alpha = 0)
alpha_c = 0.0
f_c = alpha_c * psi**2 + (beta/2) * psi**4
ax1.plot(psi, f_c, label='$T = T_c$ (Transition)', color='#f39c12', linestyle='--', linewidth=2.5)

# T < Tc (alpha < 0)
alpha_low = -2.0
f_low = alpha_low * psi**2 + (beta/2) * psi**4
ax1.plot(psi, f_low, label='$T < T_c$ (Superconducting)', color='#2980b9', linewidth=2.5)

# Minimum points for T < Tc
psi_min = np.sqrt(-alpha_low/beta)
f_min = alpha_low * psi_min**2 + (beta/2) * psi_min**4
ax1.scatter([-psi_min, psi_min], [f_min, f_min], color='#c0392b', s=80, zorder=5)

# Annotations
ax1.annotate('Minimum Energy\n$(\pm \psi_0)$', 
             xy=(psi_min, f_min), xytext=(0.5, -2.5),
             arrowprops=dict(facecolor='#c0392b', arrowstyle='->', lw=1.5), 
             fontsize=10, fontweight='bold', color='#c0392b', ha='center')

ax1.set_title('1D Ginzburg-Landau Free Energy', fontsize=14, fontweight='bold')
ax1.set_xlabel('Order Parameter $\psi$ (Real Part)', fontsize=12)
ax1.set_ylabel('Free Energy Density $\Delta F$', fontsize=12)
ax1.axhline(0, color='black', linewidth=1)
ax1.axvline(0, color='black', linewidth=1)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(fontsize=11)
ax1.set_ylim(-3, 6)

# --- Panel 2: 3D "Mexican Hat" Potential (T < Tc) ---
ax2 = fig.add_subplot(122, projection='3d')
re_psi = np.linspace(-2.2, 2.2, 100)
im_psi = np.linspace(-2.2, 2.2, 100)
Re, Im = np.meshgrid(re_psi, im_psi)
mag_sq = Re**2 + Im**2

# Using alpha < 0 for Mexican hat
F_3d = alpha_low * mag_sq + (beta/2) * mag_sq**2

# Plot surface
surf = ax2.plot_surface(Re, Im, F_3d, cmap='coolwarm', alpha=0.85, antialiased=True, edgecolor='none')
ax2.set_title('3D "Mexican Hat" Potential ($T < T_c$)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Re($\psi$)', fontsize=12)
ax2.set_ylabel('Im($\psi$)', fontsize=12)
ax2.set_zlabel('Free Energy $\Delta F$', fontsize=12)

# Adjust view
ax2.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('ginzburg_landau_potential.png', dpi=300)
plt.close()

print("Ginzburg-Landau illustration generated successfully.")