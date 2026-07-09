# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:56:54 2026

@author: Straight A
"""

import numpy as np
import matplotlib.pyplot as plt

# Setup the figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), facecolor='white')

# --- Left Panel: Normal Metal ---
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 10)
ax1.axis('off')

# Draw Fermi Sea (Filled States)
ax1.fill_between([1, 3], 0, 5, color='#bdc3c7', alpha=0.7)
ax1.plot([1, 3], [5, 5], color='#7f8c8d', linewidth=3) # Fermi Level
ax1.text(2, 2.5, 'Filled States\n(Fermi Sea)', ha='center', va='center', fontsize=12, fontweight='bold', color='#2c3e50')
ax1.text(3.1, 5, r'$E_F$ (Fermi Energy)', ha='left', va='center', fontsize=11, fontweight='bold')

# Normal Continuum
ax1.text(2, 7.5, 'Empty States\n(Continuum)', ha='center', va='center', fontsize=12, color='#7f8c8d')
ax1.set_title('Normal Metal ($T=0$K)', fontsize=14, fontweight='bold', color='#2c3e50')

# --- Right Panel: Superconductor ---
ax2.set_xlim(0, 4)
ax2.set_ylim(0, 10)
ax2.axis('off')

# Draw Lowered Sea
ax2.fill_between([1, 3], 0, 4, color='#bdc3c7', alpha=0.4)
ax2.text(2, 2, 'Filled States', ha='center', va='center', fontsize=11, color='#7f8c8d')

# Draw Cooper Pair Collective Ground State
ax2.plot([1, 3], [4, 4], color='#2980b9', linewidth=4)
ax2.text(2, 4.3, 'Cooper Pair Collective State', ha='center', va='bottom', fontsize=11, fontweight='bold', color='#2980b9')

# Draw the Energy Gap (2\Delta)
ax2.fill_between([1, 3], 4, 6, color='#fadbd8', alpha=0.3) # Shaded gap area
ax2.text(2, 5, r'BCS Energy Gap ($2\Delta$)', ha='center', va='center', fontsize=12, fontweight='bold', color='#c0392b')

# Reference dashed line for original Ef
ax2.plot([1, 3], [5, 5], color='#7f8c8d', linestyle='--', alpha=0.5)
ax2.text(3.1, 5, r'Original $E_F$', ha='left', va='center', fontsize=10, color='#7f8c8d')

# Quasiparticle Continuum
ax2.fill_between([1, 3], 6, 9, color='#3498db', alpha=0.1)
ax2.plot([1, 3], [6, 6], color='#2c3e50', linewidth=2)
ax2.text(2, 7.5, 'Quasiparticle Continuum\n(Excited Single Electrons)', ha='center', va='center', fontsize=11, color='#2c3e50')

ax2.set_title('Superconductor ($T=0$K)', fontsize=14, fontweight='bold', color='#2c3e50')

plt.tight_layout()
plt.savefig('bcs_energy_gap_local.png', dpi=300)
plt.show() # This forces Spyder to render it right in front of you!