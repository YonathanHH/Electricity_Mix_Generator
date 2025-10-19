"""
Electricity Generation Mix Calculator
A capstone project for tracking and analyzing electricity generation data
Author: Yonathan Hary Hutagalung
Scope: This program tracks electricity generation data across different regions and analyzes the percentage of green energy vs conventional sources.
"""
# Global variables to store data and energy type information
data = [
    {
        'id': 0,
        'location': 'Bandung',
        'powerplant': 'Patuha',
        'energy_type': 'Geothermal',
        'energy_generated': 40.0,
        'green_energy': True,
        'percentage': 0.0, # Will be calculated
        'intermittent': False
    },
    {
        'id': 1,
        'location': 'Bandung',
        'powerplant': 'Takuban Perahu',
        'energy_type': 'Geothermal',
        'energy_generated': 40.0,
        'green_energy': True,
        'percentage': 0.0,
        'intermittent': False
    },
    {
        'id': 2,
        'location': 'Cikarang',
        'powerplant': 'Cikarang I',
        'energy_type': 'Coal',
        'energy_generated': 40.0,
        'green_energy': False,
        'percentage': 0.0,
        'intermittent': False
    },
    {
        'id': 3,
        'location': 'Cikarang',
        'powerplant': 'Cikarang II',
        'energy_type': 'Gas',
        'energy_generated': 60.0,
        'green_energy': False,
        'percentage': 0.0,
        'intermittent': False
    },
    {
        'id': 4,
        'location': 'Cirebon',
        'powerplant': 'Kuningan',
        'energy_type': 'Biomass',
        'energy_generated': 10.0,
        'green_energy': True,
        'percentage': 0.0,
        'intermittent': False
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
    'Solar',         # Green
    'Nuclear'        # Green
]
# Set of green energy sources for easy checking
green_energy_sources = {'Geothermal', 'Biomass', 'Hydro', 'Wind', 'Solar', 'Nuclear'}
#Set intermittent
intermittent = {'Solar', 'Wind'}
def calculate_percentages():
    #Calculate the percentage of total generation for each power plant.
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
    # Display all electricity generation data in a formatted table.
    global data
    
    print('\n' + '='*140)
    print('ELECTRICITY GENERATION DATA')
    print('='*140)
    
    if not data:
        print('No data available.')
        return
    print(f'{'ID':<3} {'Location':<12} {'Powerplant':<18} {'Energy Type':<12} {'Generated (MWh)':<16} {'Green Energy':<12} {'Percentage':<10} {'Intermittent':<10}')
    print('-' * 140)
    
    # Table data
    for plant in data:
        if plant['green_energy']:
            green_status = 'True'
        else:
            green_status = 'False'
    
    for plant in data:
        if plant['intermittent']:
            intermittent = 'True'
        else:
            intermittent = 'False'

        print(f'{plant['id']:<3} {plant['location']:<12} {plant['powerplant']:<18} '
              f'{plant['energy_type']:<12} {plant['energy_generated']:<16.1f} '
              f'{green_status:<12} {plant['percentage']:<5.1f}%'
              f'{'':<5} {intermittent:<10}')
    
    print('-' * 140)
    
    # Calculate and display total generation
    total_generation = 0
    for plant in data:
        total_generation += plant['energy_generated']
    
    print(f'Total Generation: {total_generation:.1f} MWh')
    print('='*140)

def add_generation_data():
    #Add new electricity generation data through user input
    global data, energy_types, green_energy_sources

    print('\n' + '='*60)
    print('ADD NEW ELECTRICITY GENERATION DATA')
    print('='*60)

    # Get location input
    location = input('Where is the powerplant located? ')
    if not location:
        print('Error: Location cannot be empty!')
        return

    # Get powerplant name
    
    while True:
        powerplant = input('What is the powerplant name? ')
        if not powerplant:
            print('Error: Powerplant name cannot be empty!')
            continue
        else:
            break

    # Display energy type options
    print('\nChoose energy type:')
    for i in range(len(energy_types)):
        energy_type = energy_types[i]
        if energy_type in green_energy_sources:
            green_status = 'Green'
        else:
            green_status = 'Not Green'
        print(f'{i}. {energy_type} ({green_status})')

    # Get energy type selection
    while True:
        pilihan = input(f'Choose an energy type (0-{len(energy_types)-1}): ')
        if pilihan =='':
            print('Error: Energy type cannot be empty!')
            continue
        if pilihan.isdigit():
            pilihan_int = int(pilihan)
            if pilihan_int >= 0 and pilihan_int < len(energy_types):
                break
            else:
                print('Error: Invalid energy type selection!')
                continue

    while True:
        energy_str = input('How much energy is generated in MWh? ')
        if energy_str == '':
            print('Error: Energy generated cannot be empty!')
            continue
        temp_str = energy_str
        if not temp_str.replace('.', '', 1).isdigit():
            print('Error: You entered a non-numeric value! Please enter numbers only.')
            continue

        energy_generated = float(energy_str)
        if energy_generated < 0:
            print('Error: Energy generated cannot be negative!')
            continue
        break

    # Determine if it's green energy
    green_energy = energy_type in green_energy_sources
    # Determine if it's intermittent
    intermittent_energy = energy_type in intermittent

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
        'location': location,
        'powerplant': powerplant,
        'energy_type': energy_type,
        'energy_generated': energy_generated,
        'green_energy': green_energy,
        'percentage': 0.0,
        'intermittent': intermittent_energy
    }

    # Add to data list
    data.append(new_data)

    # Recalculate percentages
    calculate_percentages()

    print(f'\nData added successfully!')
    print(f' Powerplant: {powerplant}')
    print(f' Location: {location}')
    if green_energy:
        energy_class = 'Green Energy'
    else:
        energy_class = 'Conventional Energy'
    print(f' Type: {energy_type} ({energy_class})')
    print(f' Produced: {energy_generated:.1f} MWh')
    if intermittent:
        print(f' Intermittent: Yes')
    else:
        print(f' Intermittent: No')

def remove_generation_data():
    # Remove electricity generation data by index
    global data

    print('\n' + '='*60)
    print('REMOVE ELECTRICITY GENERATION DATA')
    print('='*60)

    if not data:
        print('Nothing to remove.')
        return

    # Show current data with indices
    print('Available data:')
    for plant in data:
        print(f'ID {plant['id']}: {plant['powerplant']} ({plant['location']}) - {plant['energy_generated']:.1f} MWh')

    remove_input = input('\nChoose an ID to remove (or "all" to remove all data): ')
    if remove_input == '':
        print('Error: ID cannot be empty!')
        return
    if remove_input.upper() == 'ALL':
        confirm = input('Confirm the deletion of all data? (y/n): ').lower()
        if confirm == 'y':
            data.clear()
            print('Data has been deleted!')
        else:
            print('Deletion canceled.')
        return
    if not remove_input.isdigit():
        print('Error: ID must be a number!')
        return
    
    target_id = int(remove_input)
    found = False
    for i in range(len(data)):
        if data[i]['id'] == target_id:
            removed_data = data.pop(i)
            calculate_percentages()
            print(f'Data deleted: {removed_data['powerplant']} ({removed_data['location']})')
            found = True
            break
    # Reindex all IDs to be sequential starting from 0
    if found:
        for idx, plant in enumerate(data, start=0):
            plant['id'] = idx

    if not found:
        print(f'Error: Data with ID {target_id} cannot be found!')

def track_percentage_by_source():
    #Track the percentage of electricity generated by each energy source.
    global data, green_energy_sources
    
    print('\n' + '='*60)
    print('PERCENTAGE BY ENERGY SOURCE')
    print('='*60)
    
    if not data:
        print('Nothing to be analyzed.')
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
    print(f'{'Energy Source':<15} {'Generation (MWh)':<18} {'Percentage':<12} {'Type'}')
    print('-' * 60)
    
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
            energy_class = 'Green'
        else:
            energy_class = 'Conventional'
            
        print(f'{energy_type:<15} {generation:<18.1f} {percentage:<12.1f}% {energy_class}')
    
    print('-' * 60)
    print(f'{'Total':<15} {total_generation:<18.1f} {'100.0%':<12}')

def track_green_energy_percentage():
    #Track the percentage of electricity generated by green energy sources.
    global data
    
    print('\n' + '='*60)
    print('GREEN ENERGY ANALYSIS')
    print('='*60)
    
    if not data:
        print('Nothing to analyze.')
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
    print(f'{'Category':<20} {'Count':<8} {'Generation (MWh)':<18} {'Percentage'}')
    print('-' * 60)
    
    if total_generation > 0:
        green_percentage = (green_generation / total_generation) * 100
        conventional_percentage = (conventional_generation / total_generation) * 100
    else:
        green_percentage = 0
        conventional_percentage = 0
    
    print(f'{'Green Energy':<20} {green_count:<8} {green_generation:<18.1f} {green_percentage:.1f}%')
    print(f'{'Conventional Energy':<20} {conventional_count:<8} {conventional_generation:<18.1f} {conventional_percentage:.1f}%')
    print('-' * 60)
    print(f'{'Total':<20} {len(data):<8} {total_generation:<18.1f} 100.0%')
    
    # Additional analysis
    print(f'\nGreen Energy Analysis:')
    print(f'   - {green_percentage:.1f}% of total electricity generation comes from renewable sources')
    print(f'   - {green_count} out of {len(data)} power plants use green energy sources')
    
    if green_percentage >= 50:
        print(f'Excellent! Green energy dominates the energy mix')
    elif green_percentage >= 30:
        print(f'Good progress, but there is room for improvement')
    else:
        print(f'Significant opportunity to increase renewable energy adoption')

def track_intermittency_percentage():
    #Track the percentage of electricity generated by intermittent energy sources.
    global data
    
    print('\n' + '='*60)
    print('INTERMITTENCY ANALYSIS')
    print('='*60)
    
    if not data:
        print('Nothing to analyze.')
        return
    
    # Calculate intermittent energy
    intermittent_generation = 0
    intermittent_count = 0
    non_intermittent_generation = 0
    non_intermittent_count = 0
    
    for plant in data:
        if plant['intermittent']:
            intermittent_generation += plant['energy_generated']
            intermittent_count += 1
        else:
            non_intermittent_generation += plant['energy_generated']
            non_intermittent_count += 1
    
    total_generation = intermittent_generation + non_intermittent_generation
    
    # Display results
    print(f'{'Category':<20} {'Count':<8} {'Generation (MWh)':<18} {'Percentage'}')
    print('-' * 60)
    
    if total_generation > 0:
        intermittent_percentage = (intermittent_generation / total_generation) * 100
        non_intermittent_percentage = (non_intermittent_generation / total_generation) * 100
    else:
        intermittent_percentage = 0
        non_intermittent_percentage = 0
    
    print(f'{'Intermittent Energy':<20} {intermittent_count:<8} {intermittent_generation:<18.1f} {intermittent_percentage:.1f}%')
    print(f'{'Stable Energy':<20} {non_intermittent_count:<8} {non_intermittent_generation:<18.1f} {non_intermittent_percentage:.1f}%')
    print('-' * 60)
    print(f'{'Total':<20} {len(data):<8} {total_generation:<18.1f} 100.0%')
    
    # Additional analysis
    print(f'\nIntermittency Analysis:')
    print(f'{intermittent_percentage:.1f}% of total electricity generation is intermittent')
    print(f'{intermittent_count} out of {len(data)} power plants are intermittent')
    
    if intermittent_percentage <= 5:
        print(f'Significant opportunity to improve the usage of intermittent energy sources')
    elif intermittent_percentage <= 15:
        print(f'Excellent! The use of intermittent energy sources is efficient')
    elif intermittent_percentage <= 30:
        print(f'Good progress, but need to add more stable energy sources!')
    else:
        print(f'WARNING! The use of intermittent energy sources is too high! Build more stable energy sources!')
    
def update_generation_data():
    global data, energy_types, green_energy_sources
    print('\n' + '='*60)
    print('UPDATE ELECTRICITY GENERATION DATA')
    print('='*60)

    if not data:
        print('Nothing to update.')
        return

    # List current entries
    for plant in data:
        print(f'ID {plant['id']}: {plant['powerplant']} ({plant['location']}) - {plant['energy_generated']:.1f} MWh')

    # Get target ID
    target_id_input = input('\nChoose an ID to update: ')
    selected_plant = None
    if target_id_input == '':
        print('Error: ID cannot be empty!')
        return
    if not target_id_input.isdigit():
        print('Error: ID must be a number!')
        return
    for plant in data:
        target_id = int(target_id_input)
        if plant['id'] == target_id:
            selected_plant = plant
            break
        else:
            continue
    if selected_plant is None:
        print('Error: ID not found.')
        return

    # Update powerplant name
    powerplant = input(f'Powerplant name now: {selected_plant['powerplant']} - New name (blank for same): ? ')
    if powerplant == '':
        powerplant = selected_plant['powerplant']

    # Update generation amount
    energy_generated_in = input(f'New Production: {selected_plant['energy_generated']} - New production (blank for same): ')
    while True:
        if energy_generated_in == '':
            energy_generated = selected_plant['energy_generated']
            break
        vase_energen = energy_generated_in
        if not vase_energen.replace('.', '', 1).isdigit():
            print('Error: You entered a non-numeric value! Please enter numbers only.')
            energy_generated_in = input('Try again - New production (blank for same): ')
            continue
        energy_generated = float(energy_generated_in)
        if energy_generated < 0:
            print('Error: Energy generated cannot be negative!')
            energy_generated_in = input('Try again - New production (blank for same): ')
            continue
        break

    # Update entry
    selected_plant['powerplant'] = powerplant
    selected_plant['energy_generated'] = energy_generated

    calculate_percentages()
    print('Data Updated Successfully!')

def display_menu():
    #Display the main menu options.
    print('\n' + '='*60)
    print('ELECTRICITY GENERATION MIX CALCULATOR V1.2.1')
    print('='*60)
    print('1. List of electricity generation data')
    print('2. Add electricity generation data')
    print('3. Remove electricity data')
    print('4. Update electricity data')
    print('5. Track the percentage of electricity generated by source')
    print('6. Track the percentage of electricity by green energy')
    print('7. Track the percentage of electricity by intermittency')
    print('8. Exit program')
    print('='*60)

def run_program():
    #Main program function that runs the application.
    global data
    
    print('Welcome to Electricity Generation Mix Calculator!')
    print('Lets track sustainable energy transition progress...')
    
    # Calculate initial percentages
    calculate_percentages()
    
    while True:
        display_menu()
        choice = input('Choose menu (1-8): ')
            
        if choice == '1':
                list_generation_data()
        elif choice == '2':
                add_generation_data()
        elif choice == '3':
                remove_generation_data()
        elif choice == '4':
                update_generation_data()        
        elif choice == '5':
                track_percentage_by_source()
        elif choice == '6':
                track_green_energy_percentage()
        elif choice == '7':
                track_intermittency_percentage()
        elif choice == '8':
                print('\n Thank you for using Electricity Generation Mix Calculator!')
                print('   Lets support green energy transition for better future!') 
                break
        else:
                print('Error: Invalid choice! Please choose 1-8.')
            
            # Pause before showing menu again
        input('\nPress Enter to continue...')
run_program()