# TorusPowderCompositionCalc

A Python application that calculates the volume of a torus with a square cross-section and determines the masses of constituent powders needed to fill that volume while maintaining specified composition percentages.

## Features

- **Torus Volume Calculation:**
    - Computes the volume of a torus based on user-defined dimensions:
        - Outer Diameter
        - Inner Diameter
        - Height (thickness) of the square cross-section
    - Utilizes Pappus's Theorem for accurate volume calculation.


- **Powder Composition Analysis:**
    - Calculates the total mass of a powder mixture required to fill the torus.
    - Determines the mass of each constituent in the mixture based on specified weight percentages.
    - Supports multiple constituents with customizable densities and composition ratios.


- **Flexible Input Parameters:**
    - Easily modify torus dimensions and powder constituents in the script.
    - Accepts densities in g/cm³ and dimensions in mm (automatically converts units for consistency).


- **Comprehensive Output:**
    - Generates a detailed, well-formatted report saved as [`RESULT.TXT`](RESULT.TXT) (located in the root directory next to the Python code).
    - Outputs the same report to the console for immediate viewing.
    - Includes all input parameters, calculations, and results for transparency.


- **User-Friendly Structure:**
    - Clear code comments and organized structure for easy understanding and modification.
    - Assertion checks to ensure input percentages sum to 100%, preventing calculation errors.

## Usage

1. **Modify Input Parameters:**
    - Open `TorusPowderCompositionCalc.py` in a text editor.
    - Update the torus dimensions (`D_outer`, `D_inner`, `h`) with your desired values (in millimeters).
    - Edit the `constituents` list to specify the materials, their weight percentages (as decimals), and densities (in g/cm³).
        - Ensure that the sum of the weight percentages equals `1.0` (or 100%).
   - Set the `margin_factor` to `1.1` to use 10% extra powder (e.g.), accounting for manufacturing losses. 

2. **Run the Program:**
    - Execute the script using Python 3:

      ```bash
      python TorusPowderCompositionCalc.py
      ```

    - The program will perform the calculations and output the results.


3. **View the Results:**
    - The console will display the report with all input parameters and calculation results.
    - A file named [`RESULT.TXT`](RESULT.TXT) will be created in the same directory (root), containing the same report.

## Requirements

- Python 3.x

## Notes

- The program uses **Pappus's Theorem** to calculate the volume of the torus with a square cross-section.
- All dimensions are internally converted from millimeters to centimeters to match the units of density (g/cm³).
- The script includes assertion checks and detailed comments for reliability and ease of understanding.
- Ideal for engineers and scientists dealing with material compositions and geometric calculations.

## License

Do what the fuck you want with this. (WTFPL)
