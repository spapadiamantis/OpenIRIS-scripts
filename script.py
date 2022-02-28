import pandas as pd
import glob


# Make file lists
filenames = glob.glob("*bookings*.xlsx")
filenames.sort()
book_file = filenames[-1]

filenames = glob.glob("*department*.csv")
filenames.sort()
user_file = filenames[-1]

df = pd.read_excel(book_file)
users_df = pd.read_csv(user_file,skiprows=[0])
print(users_df)


grouped_df = df.groupby(['User','Resource','Group'])
grouped_df = grouped_df[["User","Resource","Group","Duration"]]


out_df = grouped_df.sum()
out_df = out_df.reset_index()
dataTypeSeries = users_df.dtypes
print(users_df.set_index('Email')['Name'])

out_df['Nom'] = out_df['User'].replace(users_df.set_index('Email')['Name'])

out_df = out_df.rename(columns={"User":"Utilisateur","Resource":"Machine utilisée","Group":"Equipe","Duration":"Nb d'heure"})

out_df.to_csv('stats_reservation.csv')
