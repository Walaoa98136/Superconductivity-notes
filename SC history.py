# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:32:22 2026

@author: Straight A
"""

import matplotlib.pyplot as plt
import numpy as np

# Data compilation
# Format: [Material, Year, Tc, Discoverer, Type]
data = [
    ("Hg", 1911, 4.2, "Kamerlingh Onnes", "Conventional"),
    ("Nb", 1930, 9.2, "Meissner", "Conventional"),
    ("NbN", 1941, 16.0, "Aschermann", "Conventional"),
    ("V$_3$Si", 1953, 17.5, "Hardy & Hulm", "Conventional"),
    ("Nb$_3$Sn", 1954, 18.0, "Matthias", "Conventional"),
    ("Nb$_3$Ge", 1973, 23.2, "Gavaler", "Conventional"),
    ("LBCO", 1986, 35.0, "Bednorz & Müller", "High-Tc"),
    ("YBCO", 1987, 93.0, "Wu & Chu", "High-Tc"),
    ("BSCCO", 1988, 105.0, "Maeda", "High-Tc"),
    ("Hg-Ba-Ca-Cu-O", 1993, 133.0, "Schilling", "High-Tc"),
    ("MgB$_2$", 2001, 39.0, "Akimitsu", "Conventional"),
    ("LaFeAsO", 2008, 26.0, "Hosono", "High-Tc"),
    ("H$_2$S (155 GPa)", 2015, 203.0, "Drozdov & Eremets", "Conventional"),
    ("LaH$_{10}$ (170 GPa)", 2018, 250.0, "Drozdov / Hemley", "Conventional")
]

# Separate data
conv_years = [d[1] for d in data if d[4] == "Conventional"]
conv_tc = [d[2] for d in data if d[4] == "Conventional"]
conv_labels = [f"{d[0]}\n({d[3]})" for d in data if d[4] == "Conventional"]

high_years = [d[1] for d in data if d[4] == "High-Tc"]
high_tc = [d[2] for d in data if d[4] == "High-Tc"]
high_labels = [f"{d[0]}\n({d[3]})" for d in data if d[4] == "High-Tc"]

plt.figure(figsize=(14, 8))

# Plot conventional
plt.scatter(conv_years, conv_tc, color='blue', s=100, label='Conventional (BCS & Hydrides)', edgecolors='black', zorder=5)

# Plot High-Tc
plt.scatter(high_years, high_tc, color='red', s=100, label='High-Temperature (Cuprates & Pnictides)', edgecolors='black', zorder=5)

# Add liquid nitrogen reference line
plt.axhline(y=77, color='cyan', linestyle='--', linewidth=2, label='Liquid Nitrogen Boiling Point (77 K)', zorder=1)

# Add labels
for i, (year, tc, label) in enumerate(zip(conv_years, conv_tc, conv_labels)):
    # Custom offsets to prevent overlap
    x_offset = 1.5
    y_offset = -5 if tc < 30 else 5
    if "H$_2$S" in label:
        x_offset = -12
        y_offset = 5
    elif "LaH$_{10}$" in label:
        x_offset = -14
        y_offset = -5
    elif "MgB" in label:
        x_offset = 1.5
        y_offset = -5
    elif "Nb" in label:
        x_offset = 1
        y_offset = -5
        
    plt.text(year + x_offset, tc + y_offset, label, fontsize=9, color='darkblue', 
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', pad=1))

for i, (year, tc, label) in enumerate(zip(high_years, high_tc, high_labels)):
    x_offset = -12 if "YBCO" in label or "Hg-Ba" in label else 1.5
    y_offset = 5
    if "LBCO" in label:
        x_offset = -12
    plt.text(year + x_offset, tc + y_offset, label, fontsize=9, color='darkred',
             bbox=dict(facecolor='white', alpha=0.6, edgecolor='none', pad=1))

plt.title('Timeline of Superconductor Discoveries ($T_c$ vs. Year)', fontsize=16, fontweight='bold')
plt.xlabel('Year of Discovery', fontsize=14)
plt.ylabel('Critical Temperature $T_c$ (K)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.7, zorder=0)
plt.legend(loc='upper left', fontsize=12)

# Set limits to give some padding
plt.xlim(1905, 2025)
plt.ylim(0, 270)

plt.tight_layout()
plt.savefig('superconductor_timeline.png', dpi=300)
plt.close()

print("Timeline graph generated successfully.")