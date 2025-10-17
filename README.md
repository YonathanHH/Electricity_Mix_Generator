![Electricity Mix Generator Logo_V2](https://drive.google.com/file/d/1mT0KBoB9rmvLQeightQkmCa984zUJ-NJ/view?usp=sharing)

A Python-based application designed to track, analyze, and visualize electricity generation data across different regions and energy sources.

# Project Overview

The **Electricity Generation Mix Calculator** is a comprehensive tool that enables users to monitor and analyze electricity generation data for various regions (cities, provinces, countries, or international). The application provides insights into energy mix composition and tracks the progress of green energy transition.

## Purpose & Impact

### Why This Project Matters
- **Energy Transition Monitoring**: Track progress towards renewable energy goals
- **Policy Support**: Provide data-driven insights for governmental energy planning
- **Diversification Analysis**: Help understand regional energy portfolio composition
- **Environmental Impact**: Monitor the shift towards cleaner energy sources

### Target Users
- **Government Bodies**: Regional and national energy planning agencies
- **Power Companies**: Electricity generation companies requiring data management
- **Research Institutions**: Academic and policy research organizations
- **Environmental Organizations**: Groups monitoring clean energy progress

##  Features

### Core Functionality
1. **Data Management**
   - List all electricity generation data with comprehensive details
   - Add new electricity generation records
   - Remove existing electricity data entries
   - Update existing electricity data entries (Only applicable towards name of powerplants and energy generated)

2. **Analytics & Insights**
   - Track percentage breakdown by energy source type
   - Calculate green energy percentage for sustainability metrics
   - Regional energy mix visualization
   - Energy intermittency analysis

3. **User-Friendly Interface**
   - Interactive menu-driven system
   - Intuitive data input process
   - Clear data presentation in tabular format

## Data Structure

The application manages electricity generation data with the following attributes:

| Field | Description | Type |
|-------|-------------|------|
| ID | Unique identifier | Integer |
| Location | Power plant location (City/Region) | String |
| Power Plant | Name of the electricity generation facility | String |
| Energy Type | Source of energy generation | String (User Input) |
| Energy Generated | Amount of electricity produced | Float (MWh) |
| Green Energy | Environmental classification | Boolean |
| Percentage | Share of total generation | Float (%) |
| Intermittent Energy | Stable energy classification | Boolean |

### Supported Energy Types
- **Renewable Sources** 
  - Geothermal
  - Biomass  
  - Hydro
  - Wind (Intermittent)
  - Solar (Intermittent)
  - Nuclear

- **Conventional Sources**
  - Diesel
  - Coal
  - Gas

## Technical Specifications

### Requirements
- Python 3.6+
- No external dependencies (uses built-in Python libraries)

# Run the application
python main.py

## How to Use

### Main Menu Options
1. **List Generation Data**: View all recorded electricity generation data
2. **Add New Data**: Input new power plant generation information
3. **Remove Data**: Delete existing records by index or clear data
4. **Update Data**: Updating existing data
5. **Source Analysis**: View percentage breakdown by energy type
6. **Green Energy Metrics**: Calculate renewable energy percentage
7. **Intermittent Energy Metrics**: Calculate intermittent energy percentage
8. **Exit**: Close the application

### Adding New Data
The application will prompt for:
- **Location**: Where is the power plant located?
- **Plant Name**: What is the name of the power plant?
- **Energy Type**: Select from available energy sources
- **Generation Amount**: How much energy is produced (MWh)?

*Green energy classification and percentage calculations are automated.*

### Updating data
- **Location**: Input new location data - blank for None
- **New Generation**: Input new production rate

### Deleting data
Input the index of data!

## Sustainability Focus

This project aligns with global sustainability goals by:
- Promoting transparency in energy generation reporting
- Facilitating renewable energy transition tracking
- Supporting evidence-based energy policy decisions
- Encouraging regional green energy development

## Sample Data Format

```
ID | Location | Power Plant    | Energy Type | Generated (MWh) | Green Energy | Percentage
---|----------|----------------|-------------|-----------------|--------------|------------
0  | Bandung  | Patuha         | Geothermal  | 40              | True         | 21%
1  | Bandung  | Takuban Perahu | Geothermal  | 40              | True         | 21%
2  | Cikarang | Cikarang I     | Coal        | 40              | False        | 21%
3  | Cikarang | Cikarang II    | Gas         | 60              | False        | 32%
4  | Cirebon  | Kuningan       | Biomass     | 10              | True         | 5%
```

## Limitiation
- The program solely focus only for simple energy tracking and green energy tracking not suitable for advanced energy modelling
- Lacks import or export data features
- Lacks of graphical or map visualitation features

## Contributing

This project is part of a capstone initiative focusing on sustainable energy analysis. Contributions that enhance functionality while maintaining the core scope are welcome.

### Development Guidelines
- Follow python best practices.
- Add comment for reduced confusion.
- Must follow initial purposes: for green energy transition!

### Future development
- Integration to CSV files to store data more efficiently
- Data plotting using Matplotlib or Seaborn for better analytics
- Integration with geography libraries (example:geopandas) for GIS analysis

## Adding more sustainability features 
- LCOE Analysis for energy financial modelling
- Adding energy storage function for intermittent sources (Solar and Wind)
- Adding the features to track who received the electricity (Residential or Industrial)

## License

This project is developed as part of an academic capstone program in Data Science Bootcamp Purwadhika.

## Author

**Yonathan Hary Hutagalung**  
*Jakarta 12760*
*Sustainable Energy Science Graduate*
*Purwadhika Data Science Student*

---

*This application contributes to the global transition towards sustainable energy by providing tools for transparent energy generation monitoring and analysis.*
