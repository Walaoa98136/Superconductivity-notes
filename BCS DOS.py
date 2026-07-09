# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 20:32:52 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the energy scale relative to the Fermi Level (E - Ef)
energy = np.linspace(-5, 5, 1000)

# Set the superconducting energy gap parameter
Delta = 1.5
Gamma = 0.02  # Tiny broadening parameter to prevent numerical infinity at the peak

# --- Calculate Normal Metal DOS ---
# Normalized to 1.0 for flat-band approximation near Ef
dos_normal = np.ones_like(energy)

# --- Calculate BCS Superconducting DOS (Dynes Formula) ---
# Using complex numbers to cleanly handle the square root singularity
Z = energy - 1j * Gamma
dos_super = np.real(Z / np.sqrt(Z**2 - Delta**2))

# --- Plotting Configuration ---
fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')

# Plot Normal Metal reference
ax.plot(energy, dos_normal, color='#7f8c8d', linestyle='--', linewidth=2, label='Normal Metal ($T > T_c$)')

# Plot Superconducting DOS
ax.plot(energy, dos_super, color='#c0392b', linewidth=3, label=r'Superconductor ($T < T_c$)')
ax.fill_between(energy, 0, dos_super, color='#e74c3c', alpha=0.1)

# --- Graphical Annotations ---
# Shading the forbidden gap region
ax.axvspan(-Delta, Delta, color='#ecf0f1', alpha=0.5, label=r'Forbidden Energy Gap ($2\Delta$)')

# Vertical line pointers for the gap edges
ax.axvline(-Delta, color='#2c3e50', linestyle=':', alpha=0.7)
ax.axvline(Delta, color='#2c3e50', linestyle=':', alpha=0.7)
ax.axvline(0, color='black', linewidth=1)

# Labels for key features
ax.text(0, 0.5, r'No States' + '\n' + r'Allowed', color='#7f8c8d', fontsize=11, ha='center', fontweight='bold')
ax.text(Delta + 0.1, 2.5, r'BCS Pile-up Peak' + '\n' + r'(Singularity)', color='#c0392b', fontsize=10, va='center')
ax.text(-5, 1.1, 'Asymptotic approach to Normal State', fontsize=9, color='#7f8c8d')

# Labels and Limits
ax.set_title('BCS Density of States (DOS) Profile', fontsize=14, fontweight='bold', color='#2c3e50')
ax.set_xlabel(r'Energy Relative to Fermi Level ($E - E_F$)', fontsize=12)
ax.set_ylabel(r'Normalized Density of States $N(E) / N_n(0)$', fontsize=12)
ax.set_xlim(-5, 5)
ax.set_ylim(0, 4)
ax.grid(True, linestyle=':', alpha=0.4)
ax.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.savefig('bcs_density_of_states.png', dpi=300)
plt.show()