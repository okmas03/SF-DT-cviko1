# Cvičenie 1 – Analýza predajov videohier

Skript [cviko1.py](cviko1.py) analyzuje dataset [vgsales.csv](vgsales.csv), ktorý obsahuje predaje videohier (v miliónoch kusov) podľa regiónov. Dôležité stĺpce:

| Stĺpec      | Význam                              |
|-------------|-------------------------------------|
| `Name`      | názov hry                           |
| `Year`      | rok vydania                         |
| `Genre`     | žáner hry                           |
| `NA_Sales`  | predaje v Severnej Amerike (mil.)   |
| `EU_Sales`  | predaje v Európe (mil.)             |

## Spustenie

```bash
pip install pandas matplotlib numpy
python3 cviko1.py
```

Skript vypíše výsledky do terminálu a na konci (`plt.show()`) otvorí okná s grafmi.

Na začiatku sa načítajú knižnice a dataset:

```python
df = pd.read_csv("vgsales.csv")
```

Celý dataset je potom uložený v DataFrame `df`.

---

## Úloha 1 – Početnosť žánrov v 90. rokoch

**Cieľ:** zistiť, koľko hier jednotlivých žánrov vyšlo v rokoch 1990–1999, a zobraziť to v stĺpcovom grafe.

```python
dfs_90s = df[(df['Year'] >= 1990) & (df['Year'] < 2000)]
genre_counts = dfs_90s['Genre'].value_counts()
```

1. **Filtrovanie:** vyberieme iba riadky, kde je rok vydania od 1990 (vrátane) do 2000 (bez roku 2000). Dve podmienky sa spájajú operátorom `&` a každá musí byť v zátvorkách.
2. **Počítanie:** `value_counts()` spočíta, koľkokrát sa každý žáner v stĺpci `Genre` vyskytuje. Výsledok je zoradený od najčastejšieho žánru.
3. **Graf:** `genre_counts.plot(kind='bar', ...)` vykreslí stĺpcový graf. Popisky osi X sú otočené o 45°, aby sa neprekrývali, a `tight_layout()` upraví okraje tak, aby sa popisky zmestili.

---

## Úloha 2 – Korelácia predajov v Severnej Amerike a Európe

**Cieľ:** vypočítať, ako silno spolu súvisia predaje v Severnej Amerike (`NA_Sales`) a v Európe (`EU_Sales`).

```python
corr = df["NA_Sales"].corr(df["EU_Sales"])
corr_np = np.corrcoef(df["NA_Sales"], df["EU_Sales"])[0, 1]
```

Korelácia sa počíta dvoma spôsobmi, aby sa dali výsledky porovnať:

- **pandas:** `Series.corr()` vráti Pearsonov korelačný koeficient priamo ako jedno číslo.
- **NumPy:** `np.corrcoef()` vráti korelačnú **maticu** 2×2. Na diagonále sú jednotky (korelácia premennej so sebou samou) a mimo diagonály je hľadaná hodnota, preto sa berie prvok `[0, 1]`.

**Výsledok:** obe metódy dávajú rovnakú hodnotu **≈ 0,768**. Ide o silnú kladnú koreláciu: hry, ktoré sa dobre predávajú v Severnej Amerike, sa väčšinou dobre predávajú aj v Európe.

---

## Úloha 3 – Vývoj korelácie podľa rokov

**Cieľ:** zistiť, ako sa korelácia medzi predajmi v Severnej Amerike a Európe menila v jednotlivých rokoch 1985–2009.

```python
df_years = df[(df['Year'] >= 1985) & (df['Year'] < 2010)]

yearly_corr = df_years.groupby('Year').apply(
    lambda g: g['NA_Sales'].corr(g['EU_Sales'])
)
```

1. **Filtrovanie:** ponecháme hry vydané od roku 1985 do roku 2009.
2. **Zoskupenie:** `groupby('Year')` rozdelí dáta na skupiny, jednu pre každý rok.
3. **Výpočet pre každú skupinu:** `apply` s funkciou `lambda` spočíta koreláciu `NA_Sales` a `EU_Sales` zvlášť pre každý rok. Výsledkom je Series, kde index je rok a hodnota je korelácia.
4. **Graf:** čiarový graf s bodmi (`marker='o'`) ukazuje, ako sa korelácia v čase mení. Mriežka (`grid`) uľahčuje odčítanie hodnôt.

---

## Úloha 4 – Rozdiel predajov športových hier (NA − EU)

**Cieľ:** pre hry žánru *Sports* vypočítať rozdiel medzi predajmi v Severnej Amerike a v Európe a popísať ho základnými štatistikami.

```python
sports = df[df['Genre'] == 'Sports'].copy()
sports['Diff'] = sports['NA_Sales'] - sports['EU_Sales']
```

1. **Filtrovanie:** vyberieme iba športové hry. `.copy()` vytvorí samostatnú kópiu, aby pandas pri pridaní nového stĺpca nevypisoval varovanie `SettingWithCopyWarning`.
2. **Nový stĺpec `Diff`:** kladná hodnota znamená, že hra sa viac predávala v Severnej Amerike, záporná znamená, že sa viac predávala v Európe.
3. **Základné štatistiky:** `describe()` vypíše počet, priemer, smerodajnú odchýlku, minimum, kvartily (25 %, 50 %, 75 %) a maximum.
4. **Extrémy:** `idxmin()` a `idxmax()` vrátia index riadku s najmenším a najväčším rozdielom. Cez `loc` z neho vytiahneme názov hry a rok.
5. **Priemer a smerodajná odchýlka** sa vypíšu ešte raz samostatne, zaokrúhlené na 3 desatinné miesta.

**Výsledky:**

| Ukazovateľ             | Hodnota                                   |
|------------------------|-------------------------------------------|
| Počet športových hier  | 2 346                                     |
| Priemerný rozdiel      | 0,131 mil.                                |
| Smerodajná odchýlka    | 0,548 mil.                                |
| Minimum                | −4,95 mil. – *FIFA 16* (2015)             |
| Maximum                | 12,47 mil. – *Wii Sports* (2006)          |

Športové hry sa teda v priemere predávajú o niečo lepšie v Severnej Amerike. Najväčšiu prevahu v Európe má *FIFA 16*, čo zodpovedá popularite futbalu v Európe.

---

## Úloha 5 (5.1, 5.2, 5.3)

Zatiaľ nie je vypracovaná; v skripte sú pripravené iba prázdne sekcie.
