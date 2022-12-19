import pandas as pd

data_csv = pd.read_csv('recs2009_public.csv')
data = pd.DataFrame(data_csv)
liste = ['DOEID', 'KWHSPH', 'KWHWTH', 'KWHOTH', 'KWHCOL', 'KWHRFG', 'BTULPSPH', 'BTULPWTH', 'BTULPOTH', 'BTUNGSPH', 'BTUNGWTH', 'BTUNGOTH', 'BTUFOSPH', 'BTUFOWTH', 'BTUFOOTH', 'BTUKERSPH', 'BTUKERWTH', 'BTUKEROTH', 'BTUELSPH', 'BTUELWTH', 'BTUELOTH', 'GALLONLPSPH', 'GALLONLPWTH', 'GALLONLPOTH', 'GALLONFOSPH', 'GALLONFOWTH', 'GALLONFOOTH', 'GALLONKERSPH', 'GALLONKERWTH', 'GALLONKEROTH', 'CUFEETNGSPH', 'CUFEETNGWTH', 'CUFEETNGOTH', 'BTUELCOL', 'BTUELRFG', 'BTUWOOD']

kwh_liste = ['DOEID']
btu_liste = ['DOEID']
gallon_liste = ['DOEID']
cufeet_liste = ['DOEID']

for label in liste:
    if "KWH" in  label:
        kwh_liste.append(label)
    if 'BTU' in label:
        btu_liste.append(label)
    if 'GALLON' in label:
        gallon_liste.append(label)
    if 'CUFEET' in label:
        cufeet_liste.append(label)
    else:
        None


columns = ['ID', 'PURPOSE', 'TYPE', 'KWH', 'BTU', 'GALLON', 'CUFEET', 'TOTAL_SQUARE']
"""
energy['ID'] = ""
energy['PURPOSE'] = ""
energy['TYPE'] = ""
energy['KWH'] = ""
energy['BTU'] = ""
energy['GALLON'] = ""
energy['CUFEET'] = ""
energy['TOTAL_SQUARE'] = """""

purpose = ['Space heating','Air Conditioning', 'Water heating', 'Refridgerators', 'Other']


"""for i in range(0, len(data_short)*len(purpose)):
    for type in purpose:
        energy.at[i, 'ID'] = data_short.loc[i, 'DOEID'] """

kwh_df = data[kwh_liste]
btu_df = data[btu_liste]
gallon_df = data[gallon_liste]
cufeet_df = data[cufeet_liste]

kwh_df = kwh_df.melt(id_vars='DOEID', var_name='Purpose of Usage', value_name = 'KWH' )
btu_df = btu_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name = 'BTU' )
gallon_df = gallon_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name = 'GALLON' )
cufeet_df = cufeet_df.melt(id_vars='DOEID', var_name='Purpose_of_Usage', value_name = 'CUBIC FEET' )


  