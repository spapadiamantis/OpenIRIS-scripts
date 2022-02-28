import pandas as pd

df = pd.read_excel('bookings20220224093151.xlsx')
users_df = pd.read_csv('department_membership_24_02_2022_14_54.csv')


grouped_df = df.groupby(['User','Resource','Group'])
grouped_df = grouped_df[["User","Resource","Group","Duration"]]


out_df = grouped_df.sum()

#out_df['Nom'] = out_df['User'].map(users_df.set_index('User')['Name'])

out_df = out_df.rename(columns={"User":"Utilisateur","Resource":"Machine utilisée","Group":"Equipe","Duration":"Nb d'heure"})

out_df.to_csv('stats_reservation.csv')
