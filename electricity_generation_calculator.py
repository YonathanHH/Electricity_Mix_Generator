#!/usr/bin/env python3
"""
Electricity Generation Mix Calculator
A capstone project for tracking and analyzing electricity generation data

Author: Yonathan Hary Hutagalung
Description: This program tracks electricity generation data across different regions
            and analyzes the percentage of green energy vs conventional sources.
"""
# Global variables to store data and energy type information
data = [
    {
        'id': 0,
        'lokasi': 'Bandung',
        'powerplant': 'Patuha',
        'energy_type': 'Geothermal',
        'energy_generated': 40.0,
        'green_energy': True,
        'percentage': 0.0  # Will be calculated
    },
    {
        'id': 1,
        'lokasi': 'Bandung',
        'powerplant': 'Takuban Perahu',
        'energy_type': 'Geothermal',
        'energy_generated': 40.0,
        'green_energy': True,
        'percentage': 0.0
    },
    {
        'id': 2,
        'lokasi': 'Cikarang',
        'powerplant': 'Cikarang I',
        'energy_type': 'Coal',
        'energy_generated': 40.0,
        'green_energy': False,
        'percentage': 0.0
    },
    {
        'id': 3,
        'lokasi': 'Cikarang',
        'powerplant': 'Cikarang II',
        'energy_type': 'Gas',
        'energy_generated': 60.0,
        'green_energy': False,
        'percentage': 0.0
    },
    {
        'id': 4,
        'lokasi': 'Cirebon',
        'powerplant': 'Kuningan',
        'energy_type': 'Biomass',
        'energy_generated': 10.0,
        'green_energy': True,
        'percentage': 0.0
    }
]
# Available energy types and their green energy classification
energy_types = [
    'Geothermal',    # Green
    'Diesel',        # Not Green
    'Coal',          # Not Green
    'Gas',           # Not Green
    'Biomass',       # Green
    'Hydro',         # Green
    'Wind',          # Green
    'Solar',          # Green
    'Nuclear'        # Green
]
# Set of green energy sources for easy checking
green_energy_sources = {'Geothermal', 'Biomass', 'Hydro', 'Wind', 'Solar', 'Nuclear'}
def calculate_percentages():
    """Calculate the percentage of total generation for each power plant."""
    global data
    
    if not data:
        return
    
    total_generation = 0
    for plant in data:
        total_generation += plant['energy_generated']
    
    if total_generation > 0:
        for plant in data:
            plant['percentage'] = (plant['energy_generated'] / total_generation) * 100
    else:
        for plant in data:
            plant['percentage'] = 0.0
def list_generation_data():
    """Display all electricity generation data in a formatted table."""
    global data
    
    print("\n" + "="*100)
    print("ELECTRICITY GENERATION DATA")
    print("="*100)
    
    if not data:
        print("No data available.")
        return
    print(f"{'ID':<3} {'Lokasi':<12} {'Powerplant':<18} {'Energy Type':<12} {'Generated (MWh)':<16} {'Green Energy':<12} {'Percentage':<10}")
    print("-" * 100)
    
    # Table data
    for plant in data:
        green_status = "True" if plant['green_energy'] else "False"
        print(f"{plant['id']:<3} {plant['lokasi']:<12} {plant['powerplant']:<18} "
              f"{plant['energy_type']:<12} {plant['energy_generated']:<16.1f} "
              f"{green_status:<12} {plant['percentage']:<10.1f}%")
    
    print("-" * 100)
    
    # Calculate and display total generation
    total_generation = 0
    for plant in data:
        total_generation += plant['energy_generated']
    
    print(f"Total Generation: {total_generation:.1f} MWh")
    print("="*100)
def add_generation_data():
    """Add new electricity generation data through user input."""
    global data, energy_types, green_energy_sources

    print("\n" + "="*60)
    print("ADD NEW ELECTRICITY GENERATION DATA")
    print("="*60)

    # Get location input
    lokasi = input("Dimana lokasi powerplant? ").strip()
    if not lokasi:
        print("Error: Lokasi tidak boleh kosong!")
        return

    # Get powerplant name
    powerplant = input("Apa nama powerplant? ").strip()
    if not powerplant:
        print("Error: Nama powerplant tidak boleh kosong!")
        return

    # Display energy type options
    print("\nPilih jenis powerplant:")
    for i in range(len(energy_types)):
        energy_type = energy_types[i]
        if energy_type in green_energy_sources:
            green_status = "✓ Green"
        else:
            green_status = "✗ Not Green"
        print(f"{i}. {energy_type} ({green_status})")

    # Get energy type selection
    while True:
        pilihan = input(f"Masukkan pilihan (0-{len(energy_types)-1}): ")
        energy_index = int(pilihan)
        if 0 <= energy_index < len(energy_types):
            energy_type = energy_types[energy_index]
            break
        else:
            print(f"Error: Pilihan harus antara 0-{len(energy_types)-1}")

    # Get energy generation amount, no try-except
    while True:
        energy_str = input("Berapa energy yang diproduksi dalam MWh? ")
        energy_generated = float(energy_str)
        if energy_generated < 0:
            print("Error: Energy yang diproduksi tidak boleh negatif!")
            continue
        break

    # Determine if it's green energy
    green_energy = energy_type in green_energy_sources

    # Find new ID (get maximum ID + 1)
    new_id = 0
    if data:
        max_id = 0
        for plant in data:
            if plant['id'] > max_id:
                max_id = plant['id']
        new_id = max_id + 1

    # Create new data entry
    new_data = {
        'id': new_id,
        'lokasi': lokasi,
        'powerplant': powerplant,
        'energy_type': energy_type,
        'energy_generated': energy_generated,
        'green_energy': green_energy,
        'percentage': 0.0
    }

    # Add to data list
    data.append(new_data)

    # Recalculate percentages
    calculate_percentages()

    print(f"\n✓ Data berhasil ditambahkan!")
    print(f" Powerplant: {powerplant}")
    print(f" Lokasi: {lokasi}")
    if green_energy:
        energy_class = "Green Energy"
    else:
        energy_class = "Conventional Energy"
    print(f" Jenis: {energy_type} ({energy_class})")
    print(f" Produksi: {energy_generated:.1f} MWh")
def remove_generation_data():
    """Remove electricity generation data by index."""
    global data

    print("\n" + "="*60)
    print("REMOVE ELECTRICITY GENERATION DATA")
    print("="*60)

    if not data:
        print("Tidak ada data untuk dihapus.")
        return

    # Show current data with indices
    print("Data yang tersedia:")
    for plant in data:
        print(f"ID {plant['id']}: {plant['powerplant']} ({plant['lokasi']}) - {plant['energy_generated']:.1f} MWh")

    # Get index to remove
    user_input = input("\nMasukkan ID data yang akan dihapus: ")
    target_id = int(user_input)

    # Find and remove the data
    found = False
    for i in range(len(data)):
        if data[i]['id'] == target_id:
            removed_data = data.pop(i)
            for i in range(len(data)):
                data[i]['id'] = i # Biar ID selalu sequence
            calculate_percentages()  # Recalculate percentages
            print(f"✓ Data berhasil dihapus: {removed_data['powerplant']} ({removed_data['lokasi']})")
            found = True
            break

    if not found:
        print(f"Error: Data dengan ID {target_id} tidak ditemukan!")
def track_percentage_by_source():
    """Track the percentage of electricity generated by each energy source."""
    global data, green_energy_sources
    
    print("\n" + "="*60)
    print("PERCENTAGE BY ENERGY SOURCE")
    print("="*60)
    
    if not data:
        print("Tidak ada data untuk dianalisis.")
        return
    
    # Calculate totals by energy type
    source_totals = {}
    total_generation = 0
    
    for plant in data:
        total_generation += plant['energy_generated']
        energy_type = plant['energy_type']
        if energy_type not in source_totals:
            source_totals[energy_type] = 0
        source_totals[energy_type] += plant['energy_generated']
    
    # Display results
    print(f"{'Energy Source':<15} {'Generation (MWh)':<18} {'Percentage':<12} {'Type'}")
    print("-" * 60)
    
    # Sort energy types alphabetically for consistent display
    sorted_sources = []
    for energy_type in source_totals:
        sorted_sources.append(energy_type)
    sorted_sources.sort()
    
    for energy_type in sorted_sources:
        generation = source_totals[energy_type]
        if total_generation > 0:
            percentage = generation / total_generation * 100
        else:
            percentage = 0
        
        if energy_type in green_energy_sources:
            energy_class = "Green"
        else:
            energy_class = "Conventional"
            
        print(f"{energy_type:<15} {generation:<18.1f} {percentage:<12.1f}% {energy_class}")
    
    print("-" * 60)
    print(f"{'Total':<15} {total_generation:<18.1f} {'100.0%':<12}")
def track_green_energy_percentage():
    """Track the percentage of electricity generated by green energy sources."""
    global data
    
    print("\n" + "="*60)
    print("GREEN ENERGY ANALYSIS")
    print("="*60)
    
    if not data:
        print("Tidak ada data untuk dianalisis.")
        return
    
    # Calculate green vs conventional energy
    green_generation = 0
    conventional_generation = 0
    green_count = 0
    conventional_count = 0
    
    for plant in data:
        if plant['green_energy']:
            green_generation += plant['energy_generated']
            green_count += 1
        else:
            conventional_generation += plant['energy_generated']
            conventional_count += 1
    
    total_generation = green_generation + conventional_generation
    
    # Display results
    print(f"{'Category':<20} {'Count':<8} {'Generation (MWh)':<18} {'Percentage'}")
    print("-" * 60)
    
    if total_generation > 0:
        green_percentage = (green_generation / total_generation) * 100
        conventional_percentage = (conventional_generation / total_generation) * 100
    else:
        green_percentage = 0
        conventional_percentage = 0
    
    print(f"{'Green Energy':<20} {green_count:<8} {green_generation:<18.1f} {green_percentage:.1f}%")
    print(f"{'Conventional Energy':<20} {conventional_count:<8} {conventional_generation:<18.1f} {conventional_percentage:.1f}%")
    print("-" * 60)
    print(f"{'Total':<20} {len(data):<8} {total_generation:<18.1f} 100.0%")
    
    # Additional analysis
    print(f"\n🌱 Green Energy Analysis:")
    print(f"   • {green_percentage:.1f}% of total electricity generation comes from renewable sources")
    print(f"   • {green_count} out of {len(data)} power plants use green energy sources")
    
    if green_percentage >= 50:
        print(f"   • ✓ Excellent! Green energy dominates the energy mix")
    elif green_percentage >= 30:
        print(f"   • ⚠ Good progress, but there's room for improvement")
    else:
        print(f"   • ⚡ Significant opportunity to increase renewable energy adoption")
def display_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("ELECTRICITY GENERATION MIX CALCULATOR")
    print("="*60)
    print("1. List of electricity generation data")
    print("2. Add electricity generation data")
    print("3. Remove electricity data")
    print("4. Track the percentage of electricity generated by source")
    print("5. Track the percentage of electricity by green energy")
    print("6. Exit program")
    print("="*60)
def run_program():
    """Main program function that runs the application."""
    global data
    
    print("🌱 Welcome to Electricity Generation Mix Calculator!")
    print("   Tracking sustainable energy transition progress...")
    
    # Calculate initial percentages
    calculate_percentages()
    
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ").strip()
            
        if choice == '1':
                list_generation_data()
        elif choice == '2':
                add_generation_data()
        elif choice == '3':
                remove_generation_data()
        elif choice == '4':
                track_percentage_by_source()
        elif choice == '5':
                track_green_energy_percentage()
        elif choice == '6':
                print("\n🌱 Terima kasih telah menggunakan Electricity Generation Mix Calculator!")
                print("   Mari bersama-sama mendukung transisi energi berkelanjutan!")
                break
        else:
                print("Error: Pilihan tidak valid! Masukkan angka 1-6.")
            
            # Pause before showing menu again
        input("\nTekan Enter untuk melanjutkan...")
run_program()