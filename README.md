# Residential Energy Consumption Data Analysis

## Project Overview

This project focuses on analyzing data from the Residential Energy Consumption Survey (RECS).
The goal is to clean, organize, and prepare the data for a comprehensive analysis of energy consumption patterns in different regions and for different purposes. Two CSV files are merged to create a comprehensive dataset that helps in understanding energy usage more effectively.

## Dataset Information
Source: recs2009_public.csv -- downloadable here (https://www.eia.gov/consumption/residential/)
Primary Attributes:
  DOEID: Unique Identifier for each household.
  KWH, BTU, GALLON, CUFEET: Energy consumption metrics.
  Purpose_of_Usage: Purpose for which energy is used (e.g., Space Heating, Water Heating, Refrigerator, etc.).
  Type: Type of energy source used (e.g., Electricity (EL), Natural Gas (NG), etc.).


## Project Structure
### 1. Data Organization and Cleaning:
Separate columns containing different energy sources like KWH, BTU, GALLON, and CUFEET into separate lists.
Melt each energy data into a long format for ease of analysis.
Rename and categorize energy usage types for better clarity.
### 2. Merging and Aggregating Data:
Merge the cleaned data from different energy sources.
Remove rows with zero values in all columns (indicating no consumption).
### 3. Final Dataset Preparation:
Add USESOLAR information to the final dataset.
Combine all the relevant energy data into a single comprehensive DataFrame.


## Code
import pandas as pd
import re
import numpy as np

# Load the data
data_csv = pd.read_csv('recs2009_public.csv')
data = pd.DataFrame(data_csv)

# Define the column lists based on energy sources
liste = ['DOEID', 'KWHSPH', 'KWHWTH', 'KWHOTH', 'KWHCOL', 'KWHRFG', 'BTULPSPH', 'BTULPWTH', 'BTULPOTH', 
         'BTUNGSPH', 'BTUNGWTH', 'BTUNGOTH', 'BTUFOSPH', 'BTUFOWTH', 'BTUFOOTH', 'BTUKERSPH', 
         'BTUKERWTH', 'BTUKEROTH', 'BTUELSPH', 'BTUELWTH', 'BTUELOTH', 'GALLONLPSPH', 'GALLONLPWTH', 
         'GALLONLPOTH', 'GALLONFOSPH', 'GALLONFOWTH', 'GALLONFOOTH', 'GALLONKERSPH', 'GALLONKERWTH', 
         'GALLONKEROTH', 'CUFEETNGSPH', 'CUFEETNGWTH', 'CUFEETNGOTH', 'BTUELCOL', 'BTUELRFG', 'BTUWOOD']

# Organize the columns into separate lists based on energy source
kwh_liste = ['DOEID']
btu_liste = ['DOEID']
gallon_liste = ['DOEID']
cufeet_liste = ['DOEID']

for label in liste:
    if "KWH" in label:
        kwh_liste.append(label)
    if 'BTU' in label:
        btu_liste.append(label)
    if 'GALLON' in label:
        gallon_liste.append(label)
    if 'CUFEET' in label:
        cufeet_liste.append(label)

# Create separate DataFrames for each energy source
kwh_df = data[kwh_liste]
btu_df = data[btu_liste]
gallon_df = data[gallon_liste]
cufeet_df = data[cufeet_liste]
solar_user = data[['DOEID', 'USESOLAR']]

# Melt each DataFrame into a long format
kwh_df = kwh_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name='KWH')
btu_df = btu_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name='BTU')
gallon_df = gallon_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name='GALLON')
cufeet_df = cufeet_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name='CUBIC_FEET')

# Process BTU Data
btu_df['Purpose_of_Usage'] = btu_df.Purpose_of_Usage.str[3:]
btu_df['Purpose'] = btu_df.Purpose_of_Usage.str[-3:]
btu_df['Type'] = btu_df.Purpose_of_Usage.str[:-3]
btu_df = btu_df[['DOEID', 'Purpose', 'Type', 'BTU']]
btu_df = btu_df.replace({
    'Purpose': {'OOD': 'WOOD', 'SPH': 'Space Heating', 'WTH': 'Water Heating', 'OTH': 'Other',
                'RFG': 'Refrigerator', 'COL': 'Air Conditioner'}
})

# Process Cubic Feet Data
cufeet_df['Purpose_of_Usage'] = cufeet_df.Purpose_of_Usage.str[6:]
cufeet_df['Purpose'] = cufeet_df.Purpose_of_Usage.str[-3:]
cufeet_df['Type'] = cufeet_df.Purpose_of_Usage.str[:-3]
cufeet_df = cufeet_df[['DOEID', 'Type', 'Purpose', 'CUBIC_FEET']]
cufeet_df = cufeet_df.replace({
    'Purpose': {'OOD': 'WOOD', 'SPH': 'Space Heating', 'WTH': 'Water Heating', 'OTH': 'Other',
                'RFG': 'Refrigerator', 'COL': 'Air Conditioner'}
})

# Process Gallon Data
gallon_df['Purpose_of_Usage'] = gallon_df.Purpose_of_Usage.str[6:]
gallon_df['Type'] = gallon_df.Purpose_of_Usage.str[:-3]
gallon_df['Purpose'] = gallon_df.Purpose_of_Usage.str[-3:]
gallon_df = gallon_df[['DOEID', 'Purpose', 'Type', 'GALLON']]
gallon_df = gallon_df.replace({
    'Purpose': {'OOD': 'WOOD', 'SPH': 'Space Heating', 'WTH': 'Water Heating', 'OTH': 'Other',
                'RFG': 'Refrigerator', 'COL': 'Air Conditioner'}
})

# Process KWH Data
kwh_df['Purpose'] = kwh_df.Purpose_of_Usage.str[-3:]
kwh_df['Type'] = 'EL'
kwh_df = kwh_df[['DOEID', 'Purpose', 'Type', 'KWH']]
kwh_df = kwh_df.replace({
    'Purpose': {'OOD': 'WOOD', 'SPH': 'Space Heating', 'WTH': 'Water Heating', 'OTH': 'Other',
                'RFG': 'Refrigerator', 'COL': 'Air Conditioner'}
})

# Merge the cleaned data frames
btu_kwh = pd.merge(btu_df, kwh_df, on=['DOEID', 'Purpose', 'Type'], how='outer')
gallon_cufeet = pd.merge(gallon_df, cufeet_df, on=['DOEID', 'Purpose', 'Type'], how='outer')
total = pd.merge(btu_kwh, gallon_cufeet, on=['DOEID', 'Purpose', 'Type'], how='outer')
total = total.fillna(0)
total = total.drop(total[((total['BTU'] == 0) & (total['KWH'] == 0) & (total['GALLON'] == 0) & (total['CUBIC_FEET'] == 0))].index)

# Add solar user data
total_and_solar = pd.merge(total, solar_user, on='DOEID', how='outer')

# Final dataset
total_and_solar



## Resulting Dataset
The final dataset total_and_solar contains the following columns:

DOEID: Unique Identifier
Purpose: Purpose of energy usage (e.g., Space Heating, Water Heating, Refrigerator, etc.)
Type: Type of energy source (e.g., Electricity (EL), Natural Gas (NG), etc.)
BTU: Energy consumption in BTU
KWH: Energy consumption in Kilowatt-Hour
GALLON: Energy consumption in Gallons
CUBIC_FEET: Energy consumption in Cubic Feet
USESOLAR: Whether solar energy is used

### Example Data:
DOEID  Purpose           Type  BTU       KWH      GALLON  CUBIC_FEET  USESOLAR
1      Refrigerator      EL    5170.899  1515.504  0.0     0.000      0
1      Air Conditioner  EL    10470.729  3068.795  0.0     0.000      0
...


## Conclusion
The data from the Residential Energy Consumption Survey (RECS) has been meticulously cleaned and processed to ensure accuracy and consistency. The dataset is now well-prepared and ready for comprehensive analysis, offering valuable insights into energy consumption patterns across different regions and household types.







