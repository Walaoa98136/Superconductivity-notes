# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 12:52:36 2026

@author: Straight A
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup the Figure and Axes ---
# Increase figure size slightly and set facecolor to white
fig, ax = plt.subplots(figsize=(12, 10), facecolor='white')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')  # Turn off the default axis grid/labels

# Title - Centered and clear
ax.text(5, 9.6, "Kamerlingh Onnes 1911 4-Probe Experimental Setup", 
        fontsize=18, fontweight='bold', ha='center', color='#2c3e50', zorder=10)

# ==================== 1. DRAWING THE CRYOGENIC SYSTEM (LEFT SIDE) ====================
# REDESIGN NOTE for Spyder: We remove rx/ry (rounded corners) for compatibility.
# We draw nested square containers.

# --- Outer Glass Dewar (Vacuum Insulation) ---
# Outer Glass Wall (dashed)
outer_glass_wall = patches.Rectangle((1.0, 1.2), 3.0, 7.5, edgecolor='#7f8c8d', facecolor='none', linewidth=2, linestyle='--', zorder=2)
ax.add_patch(outer_glass_wall)
# Vacuum space label
ax.text(1.2, 8.4, "Vacuum\n(Insulation)", fontsize=9, color='#7f8c8d', rotation=90, va='center')

# Outer Coolant (Liquid Air) - Fill layer
outer_coolant_fill = patches.Rectangle((1.1, 1.3), 2.8, 7.3, facecolor='#ecf0f1', alpha=0.7, zorder=1) # Light gray/white fill
ax.add_patch(outer_coolant_fill)
ax.text(2.5, 1.5, "Outer Dewar\n(Liquid Air Bath)", fontsize=10, ha='center', color='#7f8c8d', fontweight='bold')

# --- Inner Glass Dewar (Helium Container) ---
# Inner Glass Wall (dashed)
inner_glass_wall = patches.Rectangle((1.5, 1.8), 2.0, 6.2, edgecolor='#3498db', facecolor='none', linewidth=2, linestyle='--', zorder=2)
ax.add_patch(inner_glass_wall)

# Inner Coolant (Liquid Helium) - Fill layer
inner_coolant_fill = patches.Rectangle((1.6, 1.9), 1.8, 6.0, facecolor='#e8f4f8', zorder=1) # Light blue fill
ax.add_patch(inner_coolant_fill)
ax.text(2.5, 2.1, "Inner Dewar\n(Liquid Helium, 4.2 K)", fontsize=10, ha='center', color='#2980b9', fontweight='bold')

# --- Mercury Sample (Capillary Tube) ---
# A slender glass tube containing Hg
capillary_tube_body = patches.Rectangle((2.3, 3.0), 0.4, 4.0, edgecolor='#2c3e50', facecolor='#bdc3c7', linewidth=1.5, zorder=3)
ax.add_patch(capillary_tube_body)
# Solid mercury fill (dark gray)
mercury_fill = patches.Rectangle((2.35, 3.1), 0.3, 3.0, facecolor='#7f8c8d', zorder=4)
ax.add_patch(mercury_fill)
ax.text(2.5, 3.5, "Hg", fontsize=12, ha='center', va='center', fontweight='bold', color='#2c3e50', zorder=5)

# ==================== 2. DRAWING THE ELECTRICAL MEASUREMENT CIRCUIT (RIGHT SIDE) ====================
# A defined box for the instrumentation
circuit_box = patches.Rectangle((5.5, 2.0), 4.0, 6.5, edgecolor='#2c3e50', facecolor='#fdfefe', linewidth=1.5, linestyle='-', zorder=1)
ax.add_patch(circuit_box)
ax.text(7.5, 8.2, "Electrical Measurement Circuit", fontsize=12, fontweight='bold', ha='center', color='#2c3e50')

# Instrument 1: Current Source (Battery/Supply)
# Placed high
battery_body = patches.Circle((7.5, 6.5), 0.5, edgecolor='#e74c3c', facecolor='#fadbd8', linewidth=2, zorder=2)
ax.add_patch(battery_body)
ax.text(7.5, 6.5, "Constant\nCurrent\nSource (I)", fontsize=9, ha='center', va='center', fontweight='bold', color='#c0392b')

# Instrument 2: Voltmeter (Sensitive Galvanometer)
# Placed low
voltmeter_body = patches.Circle((7.5, 3.5), 0.5, edgecolor='#2980b9', facecolor='#d4e6f1', linewidth=2, zorder=2)
ax.add_patch(voltmeter_body)
ax.text(7.5, 3.5, "Sensitive\nVoltage\nMeter (V)", fontsize=9, ha='center', va='center', fontweight='bold', color='#2980b9')

# --- Drawing the Wires (Leads) ---
# wire_kwargs defined as dictionaries for consistency
kwargs_current = dict(color='#e74c3c', linewidth=2.5, zorder=5) # Bold Red
kwargs_voltage = dict(color='#2980b9', linewidth=2.5, zorder=5) # Bold Blue

# --- Current Leads (Red) ---
# Lead 1 (Source to Top of Sample)
ax.plot([7.5, 7.5, 2.5], [7.0, 7.8, 7.8], **kwargs_current)
ax.plot([2.5, 2.5], [7.8, 6.0], **kwargs_current) # Contact 1 (Top I)
ax.scatter([2.5], [6.0], color='#e74c3c', s=60, zorder=6)

# Lead 2 (Source to Bottom of Sample)
ax.plot([7.5, 7.5, 0.5, 0.5, 2.5], [6.0, 0.8, 0.8, 3.1, 3.1], **kwargs_current) # Contact 2 (Bottom I)
ax.scatter([2.5], [3.1], color='#e74c3c', s=60, zorder=6)

# --- Voltage Leads (Blue) ---
# Lead 3 (Meter to Inside Top of Sample)
ax.plot([7.0, 5.0, 5.0, 2.5], [3.5, 3.5, 5.2, 5.2], **kwargs_voltage) # Contact 3 (Top V)
ax.scatter([2.5], [5.2], color='#2980b9', s=60, zorder=6)

# Lead 4 (Meter to Inside Bottom of Sample)
ax.plot([7.5, 7.5, 5.5, 5.5, 2.5], [3.0, 1.5, 1.5, 3.8, 3.8], **kwargs_voltage) # Contact 4 (Bottom V)
ax.scatter([2.5], [3.8], color='#2980b9', s=60, zorder=6)

# ==================== 3. EXPLANATORY LABELS & ANNOTATIONS ====================

# Label Leads clearly
ax.text(3.5, 8.0, "Current Lead (I+)", color='#e74c3c', fontsize=9, fontweight='bold', ha='right')
ax.text(0.6, 1.0, "Current Lead (I-)", color='#e74c3c', fontsize=9, fontweight='bold')
ax.text(3.8, 5.3, "Voltage Lead (V+)", color='#2980b9', fontsize=9, fontweight='bold')
ax.text(3.8, 1.6, "Voltage Lead (V-)", color='#2980b9', fontsize=9, fontweight='bold')

# A defining box for the Kelvin Method
kelvin_box = patches.Rectangle((0.5, 0.3), 9.0, 0.8, edgecolor='#27ae60', facecolor='#e8f8f5', linewidth=2, zorder=1)
ax.add_patch(kelvin_box)
ax.text(5.0, 0.7, "The 4-Probe (Kelvin) Method eliminates lead and contact resistance ($R_{contact}$, $R_{wire}$).\n"
                   "The Voltmeter (V) measures the voltage drop purely across the Mercury sample ($R_{Hg}$).\n"
                   "Result: $R_{measured} = V / I$ drops exactly to ZERO at 4.2 K.", 
        fontsize=10, ha='center', va='center', color='#1e8449', fontweight='bold', zorder=2)

# For Spyder users: It is crucial to use show() if your IDE doesn't auto-display
# and ensure you look at the 'Plots' pane or the generated file.
plt.tight_layout()
plt.savefig('onnes_4probe_universal.png', dpi=300)
# plt.show() # Uncomment if running locally to see the interactive window
print("Compatible illustration generated as 'onnes_4probe_universal.png'")