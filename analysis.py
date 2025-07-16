import pandas as pd

# Chemin vers le fichier CSV dans le repo
file_path = "data/SuperMarket Analysis.csv"

# Charger les données
df = pd.read_csv(file_path)

# Afficher les 5 premières lignes
print("✅ Aperçu des données :")
print(df.head())

# Statistiques descriptives
print("\n📊 Statistiques descriptives :")
print(df.describe())

# Répartition des ventes par ville
print("\n🗺️ Répartition des ventes par ville :")
print(df["City"].value_counts())
