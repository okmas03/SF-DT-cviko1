import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("vgsales.csv")

### 1. uloha 
dfs_90s = df [(df['Year'] >= 1990) & (df['Year'] < 2000)]

genre_counts = dfs_90s['Genre'].value_counts()

plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("četnostmi žánrů 1990-2000")
plt.xlabel("Žánr")
plt.ylabel("Počet her")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
#plt.savefig("uloha1.png", dpi=150)


### 2. uloha
corr = df["NA_Sales"].corr(df["EU_Sales"])
corr_np = np.corrcoef(df["NA_Sales"], df["EU_Sales"])[0, 1]
print(f"Uloha 2")
print(f"Korelace (pandas): {corr:.6f}")
print(f"Korelace (numpy): {corr_np:.6f}")




#### 3. uloha
df_years = df [(df['Year'] >= 1985) & (df['Year'] < 2010)]

yearly_corr = df_years.groupby('Year').apply(
    lambda g: g['NA_Sales'].corr(g['EU_Sales'])
)

plt.figure(figsize=(10, 6))
yearly_corr.plot(marker='o', linestyle='-', color='skyblue')
plt.title(" Korelace mezi prodeji v Severní Americe a Evropě podle roku")
plt.xlabel("Rok")
plt.ylabel("Korelace")
plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.savefig("uloha3.png", dpi=150)


#### 4. uloha
sports =df[df['Genre'] == 'Sports'].copy()
sports['Diff'] = sports['NA_Sales'] - sports['EU_Sales']

print(f"Uloha 4")

###zakladni statisticke udaje
print(sports['Diff'].describe())

min_row = sports.loc[sports['Diff'].idxmin()]
max_row = sports.loc[sports['Diff'].idxmax()]

print(f"\n Minimum: {min_row['Diff']}, Hra: {min_row['Name']}, Rok: {min_row['Year']:.0f}")
print(f"Maximum: {max_row['Diff']}, Hra: {max_row['Name']}, Rok: {max_row['Year']:.0f}")
print(f"\n Průměrný rozdíl: {sports['Diff'].mean():.3f}")
print(f"Směrodatná odchylka rozdílu: {sports['Diff'].std():.3f}")


### 5.1
###Zobrazte graf 10 vydavatelů s nejvíce vydanými hrami mezi lety 2000 (včetně) a 2010 (vyjma).
df_00s =df[(df['Year'] >= 2000) & (df['Year'] < 2010)]
top_publishers = df_00s['Publisher'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_publishers.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Top 10 vydavatelů her mezi lety 2000 a 2010")
plt.xlabel("Vydavatel")
plt.ylabel("Počet her")
plt.xticks(rotation=45, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.savefig("uloha5_1.png", dpi=150)


###5.2
###Zobrazte v grafu korelační koeficient mezi prodeji v NA a JP pro jednotlivé žánry.
genre_corr = df.groupby('Genre').apply(
    lambda g: g['NA_Sales'].corr(g['JP_Sales'])
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
genre_corr.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("Korelační koeficient mezi prodeji v NA a JP podle žánru")
plt.xlabel("Žánr")
plt.ylabel("Korelace")
plt.xticks(rotation=45, ha="right")
plt.grid(True, alpha=0.3)
plt.tight_layout()
#plt.savefig("uloha5_2.png", dpi=150)

###5.3
###Jaké jsou základní statistické údaje rozdílu v prodejích JP a NA pro žánr "Role-Playing"? U minima a maxima zjistěte, o jaké hry se jedná.
rpg = df[df['Genre'] == 'Role-Playing'].copy()
rpg['Diff'] = rpg['JP_Sales'] - rpg['NA_Sales']

print(f"Uloha 5.3")
print(rpg['Diff'].describe())

min_row = rpg.loc[rpg['Diff'].idxmin()]
max_row = rpg.loc[rpg['Diff'].idxmax()]

print(f"\n Minimum: {min_row['Diff']}, Hra: {min_row['Name']}, Rok: {min_row['Year']:.0f}")
print(f"Maximum: {max_row['Diff']}, Hra: {max_row['Name']}, Rok: {max_row['Year']:.0f}")
print(f"\n Průměrný rozdíl: {rpg['Diff'].mean():.3f}")
print(f"Směrodatná odchylka rozdílu: {rpg['Diff'].std():.3f}")


plt.show()