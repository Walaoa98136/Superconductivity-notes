# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 15:39:15 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup Figure and Layout (2x1 Subplots) ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 14), facecolor='white')

# ==================== Panel A: Isotope Effect Concept (Phenomenological) ====================
# Conceptual plot for T_c vs Isotopic Mass M

# Generate schematic data: Tc proportional to M^(-0.5)
isotopic_mass = np.linspace(190, 210, 100) # mercury-like masses
alpha = 0.5
constant_Hg = 60 # Arbitrary constant for visual scale
tc_values = constant_Hg * (isotopic_mass**(-alpha))

# Mercury Isotope Data points (Schematic based on actual Maxwell/Reynolds 1950 data)
# Masses: 198, 200.7, 202, 204
# Schematic Tc around 4.15 - 4.19 K
Hg_isotopes_M = np.array([198.0, 200.7, 202.0, 204.0])
Hg_isotopes_Tc = constant_Hg * (Hg_isotopes_M**(-alpha)) # Using the same relation

# --- Plot the Theoretical Curve ---
ax1.plot(isotopic_mass, tc_values, color='#7f8c8d', linestyle='--', linewidth=2.5, label=r'BCS Relation: $T_c \propto M^{-0.5}$')

# --- Plot Schematic Experimental Points (Mercury) ---
ax1.scatter(Hg_isotopes_M, Hg_isotopes_Tc, color='#c0392b', s=100, edgecolor='black', zorder=5, label='Mercury Isotopes ($^{198}$Hg - $^{204}$Hg)')

# --- Annotations ---
# Pointers for shift
# Higher mass, lower Tc
# Lower mass, higher Tc
ax1.annotate('Lighter Isotopes\n$Higher\ T_c$', 
             xy=(Hg_isotopes_M[0], Hg_isotopes_Tc[0]), xytext=(192, 4.3),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), ha='center', fontsize=10, fontweight='bold', color='#1e8449')

ax1.annotate('Heavier Isotopes\n$Lower\ T_c$', 
             xy=(Hg_isotopes_M[3], Hg_isotopes_Tc[3]), xytext=(208, 4.0),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), ha='center', fontsize=10, fontweight='bold', color='#c0392b')

# Formatting Panel A
ax1.set_title('The Isotope Effect: $T_c$ Dependence on Atomic Mass $M$', fontsize=16, fontweight='bold')
ax1.set_xlabel(r'Isotopic Mass $M$ (Atomic Mass Units)', fontsize=12)
ax1.set_ylabel(r'Critical Temperature $T_c$ (K)', fontsize=12)
ax1.set_xlim(190, 210)
# Adjust ylim for clarity
ax1.set_ylim(4.1, 4.35)
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.legend(loc='upper right', fontsize=11)

# ==================== Panel B: Microscopic Explanation (Phonon Coupling) ====================
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 10)
ax2.axis('off')

# Title for Panel B
ax2.text(5, 9.2, "Microscopic Mechanism: Electron-Phonon Interaction Boundary", 
        fontsize=16, fontweight='bold', ha='center', color='#2c3e50')

# --- Drawing the Lattice Grid ---
# Draw a simple lattice grid
for x in np.linspace(1, 4, 4):
    for y in np.linspace(1, 4, 4):
        # Draw small ion cores (grey circles)
        ax2.scatter(x, y, color='#bdc3c7', s=150, zorder=1)

# --- Define two Electron Paths ---
# Electron 1 (Top path, interacts with Heavier ions)
# path parameters
x1 = np.linspace(0.5, 4.5, 100)
y1_base = 3.5
# distortion (Lorentzian bump)
gamma_heavy = 0.6
distortion_heavy = 0.4 * (gamma_heavy**2 / ((x1 - 2.5)**2 + gamma_heavy**2))
ax2.plot(x1, y1_base - distortion_heavy, color='#7f8c8d', linestyle='-', linewidth=2, label='Electron Path (Heavier Isotopes)')
ax2.scatter(0.5, y1_base, color='#2c3e50', s=60, marker='o', zorder=5) # electron
ax2.text(0.5, y1_base + 0.3, '$e^-$', ha='center', color='#2c3e50', fontweight='bold')

# Distortion arrows for Heavy ions (small displacement)
ax2.annotate('', xy=(2.5, 3.1), xytext=(2.5, 3.5),
             arrowprops=dict(facecolor='#c0392b', edgecolor='none', arrowstyle='fancy', lw=0.5))
ax2.text(2.6, 3.2, r'Small Ion Displacement $(\delta x)$'+'\n' +r'(Large $M \rightarrow$ Slow Response)', color='#c0392b', fontsize=9)

# Electron 2 (Bottom path, interacts with Lighter ions)
# path parameters
x2 = np.linspace(0.5, 4.5, 100)
y2_base = 1.5
# distortion (Lorentzian bump, sharper)
gamma_light = 0.3
distortion_light = 0.8 * (gamma_light**2 / ((x2 - 2.5)**2 + gamma_light**2))
ax2.plot(x2, y2_base - distortion_light, color='#2980b9', linestyle='-', linewidth=2, label='Electron Path (Lighter Isotopes)')
ax2.scatter(0.5, y2_base, color='#2c3e50', s=60, marker='o', zorder=5) # electron
ax2.text(0.5, y2_base + 0.3, '$e^-$', ha='center', color='#2c3e50', fontweight='bold')

# Distortion arrows for Light ions (larger displacement)
ax2.annotate('', xy=(2.5, 0.7), xytext=(2.5, 1.5),
             arrowprops=dict(facecolor='#1e8449', edgecolor='none', arrowstyle='fancy', lw=0.5))
ax2.text(2.6, 1.0, r'Large Ion Displacement $(\delta x)$'+'\n' +r'(Small $M \rightarrow$ Fast Response)', color='#1e8449', fontsize=9)

# --- Labels & Descriptions ---
# Explain pairing force strength
ax2.text(5.2, 5.0, 'Electron-Phonon Coupling Strength:\n'
                   r'Lighter Isotopes $(M) \rightarrow$' + '\n'
                   r'Faster Lattice response ($\omega_D \propto M^{-0.5}$) $\rightarrow$' + '\n'
                   r'Stronger Pairing Potential ($V$) $\rightarrow$' + '\n'
                   r'Higher Binding Energy ($2\Delta$) $\rightarrow$' + '\n'
                   r'Higher Critical Temperature ($T_c$)', fontsize=11, fontweight='bold', color='#2c3e50', bbox=dict(facecolor='#e8f8f5', alpha=0.5, edgecolor='#27ae60'))

# The final BCS Isotope relation
final_box = patches.Rectangle((0.5, 0.3), 9.0, 0.6, edgecolor='#7f8c8d', facecolor='#f8f9f9', linewidth=1.5, rx=0.1, ry=0.1)
ax2.add_patch(final_box)
ax2.text(5.0, 0.6, r'BCS Prediction: $T_c \cdot M^{\alpha} = \text{Constant}$, where $\alpha = 0.5$ for most conventional metals.', 
        fontsize=11, ha='center', va='center', fontweight='bold', color='#c0392b')

plt.tight_layout()
plt.savefig('isotope_effect_conventional.png', dpi=300)
plt.close()
print("Isotope Effect diagram generated successfully.")