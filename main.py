import math

# TorusPowderCompositionCalc
# This program calculates the volume of a torus with a square cross-section
# and determines the masses of constituent powders needed to fill that volume
# while maintaining specified composition percentages.

# Torus dimensions (in mm)
D_outer = 38.0    # Outer diameter of the torus
D_inner = 21.0    # Inner diameter of the torus
h = 11.0          # Height of the square cross-section (thickness of the torus)

# Constituents (powder composition)
constituents = [
    {'name': 'Aluminum', 'percentage': 0.95, 'density': 2.70},
    {'name': 'Iron',     'percentage': 0.05, 'density': 7.874},
]

# Ensure percentages sum to 1 (or 100%)
assert sum([c['percentage'] for c in constituents]) == 1.0, "Percentages do not sum to 100%."

# Convert dimensions from mm to cm (since densities are in g/cm³)
D_outer_cm = D_outer / 10.0
D_inner_cm = D_inner / 10.0
h_cm = h / 10.0

# Calculations for the torus volume
# The torus is considered to have a square cross-section
w_cm = (D_outer_cm - D_inner_cm) / 2.0        # Width of the square cross-section
A = w_cm * h_cm                               # Area of the square cross-section
R_c = (D_outer_cm + D_inner_cm) / 4.0         # Distance from the axis of rotation to the centroid of the cross-section
V = 2 * math.pi * R_c * A                     # Volume of the torus in cm³ (using Pappus's Theorem)

# Calculate the total mass of the powder mixture
# Using the rule of mixtures for densities and mass percentages
denominator = sum([c['percentage'] / c['density'] for c in constituents])
m_total = V / denominator                     # Total mass of the powder mixture in grams

# Calculate the mass of each constituent in the mixture
for c in constituents:
    c['mass'] = c['percentage'] * m_total     # Mass of each constituent in grams

# Prepare the output
output_lines = []

# Application Header
output_lines.append("==========================================")
output_lines.append("        TorusPowderCompositionCalc        ")
output_lines.append("==========================================\n")

# Input Parameters
output_lines.append(">>> Input Parameters:")
output_lines.append(f"  Torus Dimensions:")
output_lines.append(f"    Outer Diameter (D_outer): {D_outer} mm")
output_lines.append(f"    Inner Diameter (D_inner): {D_inner} mm")
output_lines.append(f"    Height of Cross-Section (h): {h} mm\n")

# Constituents
output_lines.append("  Powder Constituents:")
for c in constituents:
    output_lines.append(f"    {c['name']}:")
    output_lines.append(f"      Percentage by Weight: {c['percentage']*100:.2f}%")
    output_lines.append(f"      Density: {c['density']} g/cm³")
output_lines.append("")

# Results
output_lines.append(">>> Calculation Results:")
output_lines.append(f"  Volume of Torus: {V:.2f} cm³")
output_lines.append(f"  Total Mass of Powder Mixture: {m_total:.2f} grams\n")
output_lines.append("  Mass of Each Constituent:")
for c in constituents:
    output_lines.append(f"    {c['name']} ({c['percentage']*100:.0f}%): {c['mass']:.2f} grams")
output_lines.append("")

# Footer
output_lines.append("==========================================")
output_lines.append("    End of  TorusPowderCompositionCalc    ")
output_lines.append("==========================================")

# Write to file
with open("RESULT.TXT", "w") as f:
    for line in output_lines:
        f.write(line + "\n")

# Read from file and output to console
with open("RESULT.TXT", "r") as f:
    content = f.read()
    print(content)
