# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:21:46 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the energy scale relative to the Fermi Energy (xi = E - Ef)
xi = np.linspace(-10, 10, 500)

# Set two different Energy Gap (Delta) values to show how the wavefunction changes
Delta_small = 1.0
Delta_large = 3.0

def calculate_amplitudes(xi_array, delta_val):
    # Energy of the quasiparticle excitations
    E = np.sqrt(xi_array**2 + delta_val**2)
    # u_k^2 (Probability of being empty)
    u_sq = 0.5 * (1 + xi_array / E)
    # v_k^2 (Probability of being occupied)
    v_sq = 0.5 * (1 - xi_array / E)
    return u_sq, v_sq

# Calculate for both gap sizes
u_sq_s, v_sq_s = calculate_amplitudes(xi, Delta_small)
u_sq_l, v_sq_l = calculate_amplitudes(xi, Delta_large)

# --- Plotting Setup ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), facecolor='white')

# Panel 1: Occupation Probabilities (v_k^2 and u_k^2)
ax1.plot(xi, v_sq_s, color='#2c3e50', linewidth=2.5, label=r'$v_k^2$ (Occupied State, $\Delta=1$)')
ax1.plot(xi, u_sq_s, color='#7f8c8d', linewidth=2.5, linestyle='--', label=r'$u_k^2$ (Empty State, $\Delta=1$)')
ax1.plot(xi, v_sq_l, color='#c0392b', linewidth=2, alpha=0.7, label=r'$v_k^2$ (Occupied State, $\Delta=3$)')

# Annotations for Panel 1
ax1.axvline(0, color='black', linewidth=1, linestyle=':')
ax1.text(0, -0.07, '$E_F$ (Fermi Level)', ha='center', fontsize=10, fontweight='bold')
ax1.fill_between(xi, 0, v_sq_s, where=(xi>-2)&(xi<2), color='#3498db', alpha=0.1, label='Pairing Region')

ax1.set_title('BCS Coherence Amplitudes / Probabilities', fontsize=14, fontweight='bold', color='#2c3e50')
ax1.set_xlabel(r'Kinetic Energy relative to Fermi Surface ($\xi_k = E - E_F$)', fontsize=11)
ax1.set_ylabel('Probability', fontsize=11)
ax1.set_ylim(-0.1, 1.1)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='lower left', fontsize=10)

# Panel 2: Rigid Phase Representation (Complex Plane Vector Field)
# Visualizing that every k-state shares the identical phase angle phi
angles = np.ones(8) * np.pi / 4 # Rigid phase at 45 degrees
radii = np.linspace(0.5, 2.5, 8)
X = radii * np.cos(angles)
Y = radii * np.sin(angles)

ax2.quiver(np.zeros(8), np.zeros(8), X, Y, angles='xy', scale_units='xy', scale=1, color='#2980b9', width=0.015)
# Draw phase angle arc
arc_theta = np.linspace(0, np.pi/4, 50)
ax2.plot(0.5 * np.cos(arc_theta), 0.5 * np.sin(arc_theta), color='#c0392b', linewidth=2)
ax2.text(0.6, 0.2, r'Rigid Phase $\phi$', color='#c0392b', fontsize=12, fontweight='bold')

ax2.set_xlim(-1, 3)
ax2.set_ylim(-1, 3)
ax2.axhline(0, color='black', linewidth=1)
ax2.axvline(0, color='black', linewidth=1)
ax2.set_aspect('equal')
ax2.set_title(r'Macroscopic Phase Coherence ($e^{i\phi}$)', fontsize=14, fontweight='bold', color='#2c3e50')
ax2.set_xlabel('Real Axis', fontsize=10)
ax2.set_ylabel('Imaginary Axis', fontsize=10)
ax2.grid(True, linestyle=':', alpha=0.3)

plt.tight_layout()
plt.savefig('bcs_ground_state_wavefunction.png', dpi=300)
plt.show() # Forces rendering in Spyder's Plot tab