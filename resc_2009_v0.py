import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
data_csv = pd.read_csv('recs2009_public.csv')
data = pd.DataFrame(data_csv)


data_csv = pd.read_csv('public_layout.csv')


#renaming columns
type_of_energy = ['LPG Propane', 'Natural Gas', 'Fuel Oil', 'Kerosene', 'Wood'] #row'lar bunlar olcak
purpose_of_usage = ['Space heating', 'Secondary Space heating','Air Conditioning', 'Water heating', 'Refridgerators', 'Appliances, Electronics, Lighting and Miscellaneous uses']  #row'lar bunlar olcak

space_heating= 'SPH'
water_heating= 'WTH'
other_purposes = 'OTH'
air_conditioning = 'COL'
refrigerator = 'RFG'

kwh  = 'KWH'
btu = 'BTU'
cubic_feet = 'CUFEET'
gallon = 'GALLON'



lpg_propane = 'LP'
natural_gas = 'NG'
fossil = 'FO'
kerosene = 'KER'
electricity = 'EL'

electricity_kwh_list = []
unit_energy = ['BTU', 'GALLON']
type_of_energy=['LP', 'NG', 'FO', 'KER', 'EL']
purpose_list = ['SPH', 'WTH', 'OTH']
energy_var_list = []

info = pd.read_csv('public_layout.csv')
info_df = pd.DataFrame(info)
data = pd.read_csv('recs2009_public.csv')
df = pd.DataFrame(data)

energy_var_list=['DOEID', 'KWHSPH', 'KWHWTH', 'KWHOTH', 'KWHCOL', 'KWHRFG', 'BTULPSPH', 'BTULPWTH', 'BTULPOTH', 'BTUNGSPH', 'BTUNGWTH', 'BTUNGOTH', 'BTUFOSPH', 'BTUFOWTH', 'BTUFOOTH', 'BTUKERSPH', 'BTUKERWTH', 'BTUKEROTH', 'BTUELSPH', 'BTUELWTH', 'BTUELOTH', 'GALLONLPSPH', 'GALLONLPWTH', 'GALLONLPOTH', 'GALLONFOSPH', 'GALLONFOWTH', 'GALLONFOOTH', 'GALLONKERSPH', 'GALLONKERWTH', 'GALLONKEROTH', 'CUFEETNGSPH', 'CUFEETNGWTH', 'CUFEETNGOTH', 'BTUELCOL', 'BTUELRFG', 'BTUWOOD']
df_recs = df[energy_var_list]

"""for i in range(0, len(df_recs['DOEID'])):
    for column in energy_var_list[1:]:
        new_row=df_recs["Purpose"][i]
        if ((df_recs[column][i]>0) & ('SPH' in column)) == True:
           df_recs["Purpose"][i] = df_recs["Purpose"][i].replace('a', "Space Heating")
        elif ((df_recs[column][i]>0) & ('WTH' in column))== True:
            df_recs["Purpose"][i] = df_recs["Purpose"][i].replace('a', "Water Heating")
        elif ((df_recs[column][i]>0) & ('COL' in column))== True:
            df_recs["Purpose"][i] =df_recs["Purpose"][i].replace('a', "Air Conditioner")
        elif ((df_recs[column][i]>0) & ('RFG' in column))== True:
            df_recs["Purpose"][i] =df_recs["Purpose"][i].replace('a', "Refridgator")
        elif ((df_recs[column][i]>0) & ('OTH' in column))== True:
            df_recs["Purpose"][i] =df_recs["Purpose"][i].replace('a', "Other")
        else:
            None
"""
df_recs = df_recs[['DOEID','BTULPSPH', 'BTULPWTH', 'BTULPOTH', 'BTUNGSPH', 'BTUNGWTH', 'BTUNGOTH', 'BTUFOSPH', 'BTUFOWTH', 'BTUFOOTH', 'BTUKERSPH', 'BTUKERWTH', 'BTUKEROTH', 'BTUELSPH', 'BTUELWTH', 'BTUELOTH', 'GALLONLPSPH', 'GALLONLPWTH', 'GALLONLPOTH', 'GALLONFOSPH', 'GALLONFOWTH', 'GALLONFOOTH', 'GALLONKERSPH', 'GALLONKERWTH', 'GALLONKEROTH', 'CUFEETNGSPH', 'CUFEETNGWTH', 'CUFEETNGOTH', 'BTUELCOL', 'BTUELRFG', 'BTUWOOD', 'KWHSPH', 'KWHWTH', 'KWHOTH', 'KWHCOL', 'KWHRFG']]


"""
print(df_recs.head())

for i in range(0, len(df_recs['DOEID'])):
    for column in energy_var_list[1:]:
        new_row=df_recs["Purpose"][i]
        if ((df_recs[column][i]>0) & ('SPH' in column)) == True:
           new_row = new_row.replace('a', "Space Heating")
        elif ((df_recs[column][i]>0) & ('WTH' in column))== True:
            new_row = new_row.replace('a', "Water Heating")
        elif ((df_recs[column][i]>0) & ('COL' in column))== True:
            new_row =new_row.replace('a', "Air Conditioner")
        elif ((df_recs[column][i]>0) & ('RFG' in column)) == True:
            new_row =new_row.replace('a', "Refridgator")
        elif ((df_recs[column][i]>0) & ('OTH' in column))== True:
            new_row =new_row.replace('a', "Other")
        else:
            None   """

"""
# df_recs DataFrame'ine yeni sütunlar ekleyin
df_recs["ID"] = df_recs["DOEID"]
# df_recs DataFrame'ini kullanarak yeni sütunlar oluşturun
df_recs["ID"] = df_recs["DOEID"]
df_recs["Energy Unit"] = ""
df_recs["Energy Type"] = ""
df_recs["Purpose"] = ""
#df_recs["Purpose"] = ""

# df_recs DataFrame'inde gezinerek sütunları doldurun


df_recs["Energy Unit"] = df_recs.filter(regex="BTU").columns[0].split("BTU")[1]
df_recs["Energy Type"] = df_recs.filter(regex="EL").columns[0].split("EL")[0]
df_recs["Energy Type"] = df_recs.filter(regex="OTH").columns[0].split("OTH")[0]
#df_recs["Purpose"] = df_recs.filter(regex="COL").columns[0].split("COL")[0]

print(df_recs.head())

"""

columns = ['ID', 'PURPOSE', 'TYPE', 'KWH', 'BTU', 'GALLON', 'CUFEET', 'TOTAL_SQUARE']
energy = pd.dataframe()

energy['ID'] = ""
energy['PURPOSE'] = ""
energy['TYPE'] = ""
energy['KWH'] = ""
energy['BTU'] = ""
energy['GALLON'] = ""
energy['CUFEET'] = ""
energy['TOTAL_SQUARE'] = ""

