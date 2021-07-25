# IMPORT PACKAGES
import seaborn as sns
import sklearn as sk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# IMPORT DATA
stardf = pd.read_csv("D:\KaggleData\Data\stars.csv")

# LOOK AT FIRST 5 ROWS OF DATA AND LAST 5 ROWS OF DATA
print(stardf.head())
print(stardf.tail())

# CHECK DATA TYPES
print(stardf.dtypes)

# TOTAL ROWS AND COLUMNS
print(stardf.shape)

# CHECK FOR DUPLICATE ROWS
duplicatedf = stardf[stardf.duplicated()]
print("Number of duplicate rows:", duplicatedf.shape)

# NO DUPLICATES
# CHECK FOR MISSING OR NULL VALUES
print(stardf.isnull().sum())

# NO NULL VALUES
# TAKE OUT NON NUMERICAL DATA
stardf1 = stardf.drop(['Color'], axis=1)
stardf2 = stardf1.drop(['Spectral_Class'], axis=1)

print(stardf.shape)
print(stardf2.shape)

# SET UP SNS STANDARD AESTHETICS FOR PLOTS
sns.set()

# CREATE A BOXPLOT FOR EACH COLUMN
sns.boxplot(x=stardf2['Temperature'])
plt.show()

sns.boxplot(x=stardf2['L'])
plt.show()

sns.boxplot(x=stardf2['R'])
plt.show()

sns.boxplot(x=stardf2['A_M'])
plt.show()

sns.boxplot(x=stardf2['Type'])
plt.show()

# SET BIN ARGUMENT
n_obs = len(stardf2)

n_bins = round(np.sqrt(n_obs), 0)

print(n_bins)

# CREATE HISTOGRAMS FOR EACH COLUMN
plt.hist(stardf2['Temperature'], density=True, bins=15)
plt.show()

plt.hist(stardf2['L'], density=True, bins=15)
plt.show()

plt.hist(stardf2['R'], density=True, bins=15)
plt.show()

plt.hist(stardf2['A_M'], density=True, bins=15)
plt.show()

plt.hist(stardf2['Type'], density=True, bins=5)
plt.show()

# CREATE A BSWARM PLOT FOR EACH COLUMN
sns.swarmplot(x = 'Type', y = 'Temperature', data = stardf2, size = 1.5)
plt.show()

sns.swarmplot(x = 'Type', y = 'L', data = stardf2, size = 1.5)
plt.show()

sns.swarmplot(x = 'Type', y = 'R', data = stardf2, size = 1.5)
plt.show()

sns.swarmplot(x = 'Type', y = 'A_M', data = stardf2, size = 1.5)
plt.show()

# WORKING ON FOR LOOP BELOW BUT IT DOESNT WORK. WILL FIGURE IT OUT

#for column in stardf2:
#	columnSeriesObj = stardf2[column]
#	plt.hist(columnSeriesObj.values, density=True)

#plt.show()

# ALL DATA IS HEAVILY LEFT SKEWED EXCEPT FOR A_M WHICH APPEARS TO BE BIMODAL

# CREATE A CORRELATION MATRIX
c = stardf2.corr()
print(c)

# CREATE SCATTERPLOTS FOR EACH VARIABLE AS WELL
plt.scatter(stardf2['Temperature'], stardf2['Type'])
plt.show()

plt.scatter(stardf2['L'], stardf2['Type'])
plt.show()

plt.scatter(stardf2['R'], stardf2['Type'])
plt.show()

plt.scatter(stardf2['A_M'], stardf2['Type'])
plt.show()

# FIND SUMMARY STATISTICS
print(stardf2.describe())