import scipy.constants as const
from itertools import product
import pandas as pd

# Set pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.expand_frame_repr', False)

def calculate_transition_energy(Z, n1, l1, m_l1, n2, l2, m_l2):
    # Rydberg constant for any atom
    R_inf = const.physical_constants['Rydberg constant times hc in J'][0]

    # Calculate energy, frequency, and wavelength for the transition
    energy = R_inf * Z**2 * (1/n1**2 - 1/n2**2)

    frequency = energy / const.h
    wavelength = const.c / frequency
    
    return energy, frequency, wavelength

def zeeman_effect(energy, magnetic_field, m_l1, m_l2_values):
    # Calculate energy shifts due to the external magnetic field for multiple m_l2 values
    delta_energy_values = [const.physical_constants['Bohr magneton'][0] * magnetic_field * (m_l2 - m_l1) for m_l2 in m_l2_values]

    # Calculate final zeeman energy, frequency, and wavelength for each delta_energy
    results = []
    for delta_energy in delta_energy_values:
        energy_with_magnetic_field = energy + delta_energy
        frequency = energy_with_magnetic_field / const.h
        wavelength = const.c / frequency
        results.append((energy_with_magnetic_field, frequency, wavelength))

    return results

def main():
    # Get atomic number (Z) from the user
    Z = int(input("Enter the atomic number (Z): "))

    # Simulation for the first atom system
    n1 = int(input("Enter the value of n1: "))
    
    # Simulation for the second atom system
    n2 = int(input("Enter the value of n2: "))

    magnetic_field = float(input("\nEnter the external magnetic field (in Tesla) for Zeeman Effect: "))

    # Create a list to store results
    results_list = []

    # Print results for normal transition
    energy_normal, frequency_normal, wavelength_normal = calculate_transition_energy(Z, n1, 0, 0, n2, 0, 0)
    print("\nNormal Transition:")
    print(f"Energy: {energy_normal  / const.eV:.6f} eV")
    print(f"Frequency: {frequency_normal / 1e15:.6f} PHz")
    print(f"Wavelength: {wavelength_normal * 1e9:.6f} nm")

    # Print results in a table format if there are valid combinations for Zeeman effect
    print("\nZeeman Effect for Different l, m_l, and m_s combinations:")
    print("-" * 100)

    # Generate valid combinations of l1, m_l1 values
    valid_combinations_1 = product(range(n1), range(-n1, n1 + 1))

    # Generate valid combinations of l2, m_l2 values
    valid_combinations_2 = product(range(n2), range(-n2, n2 + 1))

    for (l1, m_l1), (l2, m_l2) in product(valid_combinations_1, valid_combinations_2):
        # Apply selection rule for allowed transitions in Zeeman effect
        if -l1 <= m_l1 <= l1 and -l2 <= m_l2 <= l2 and abs(m_l1 - m_l2) <= 1 and abs(l1 - l2) == 1:
            energy, frequency, wavelength = calculate_transition_energy(Z, n1, l1, m_l1, n2, l2, m_l2)
            results = zeeman_effect(energy, magnetic_field, m_l1, [m_l2])

            for m_l2_result, (final_energy, freq, wl) in zip([m_l2], results):
                results_list.append((l1, m_l1, l2, m_l2_result, final_energy / const.eV, freq / 1e15, wl * 1e9))

    # Create a DataFrame using pandas
    columns = ["l1", "m_l1", "l2", "m_l2", "Final Energy (eV)", "Frequency (PHz)", "Wavelength (nm)"]
    results_df = pd.DataFrame(results_list, columns=columns)

    # Display the DataFrame
    print(results_df)

    # Print unique frequencies and their counts
    unique_frequencies = results_df['Frequency (PHz)'].unique()
    print("\nUnique Frequencies and their Counts:")
    for freq in unique_frequencies:
        count = results_df[results_df['Frequency (PHz)'] == freq].shape[0]
        print(f"Frequency: {freq:.6f} PHz | Count: {count}")

if __name__ == "__main__":
    main()