import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

jumlah_data = 100

# generate 5 variabel input acak
fitur1 = np.random.uniform(0, 100, jumlah_data)
fitur2 = np.random.uniform(0, 100, jumlah_data)
fitur3 = np.random.uniform(0, 100, jumlah_data)
fitur4 = np.random.uniform(0, 100, jumlah_data)
fitur5 = np.random.uniform(0, 100, jumlah_data)

# memmbuat variabel output berdasarkan kombinasi 5 variabel
Y = (
    0.3 * fitur1 +
    0.2 * fitur2 +
    0.15 * fitur3 +
    0.2 * fitur4 +
    0.15 * fitur5 +
    np.random.normal(0, 5, jumlah_data)
)

# Membuat DataFrame
data = pd.DataFrame({
    "fitur1": fitur1,
    "fitur2": fitur2,
    "fitur3": fitur3,
    "fitur4": fitur4,
    "fitur5": fitur5,
    "Y": Y
})

# Menampilkan 10 data pertama
print("Dataset:")
print(data.head(10))

# Statistik dataset
print("\nStatistik Dataset:")
print(data.describe())


#scatter plot
plt.figure(figsize=(8, 6))

plt.scatter(data["fitur1"], data["Y"], alpha=0.7)

plt.title("Scatter Plot fitur 1 terhadap Output Y")
plt.xlabel("Variabel X1")
plt.ylabel("Output Y")
plt.grid(True)

plt.show()

#histogram
plt.figure(figsize=(8, 6))

plt.hist(data["Y"], bins=15, edgecolor="black")

plt.title("Distribusi Output Y")
plt.xlabel("Nilai Output Y")
plt.ylabel("Frekuensi")
plt.grid(True)

plt.show()


# Box Plot
plt.figure(figsize=(8, 6))

data.boxplot(column=["X1", "X2", "X3", "X4", "X5", "Y"])

plt.title("Box Plot Variabel Input dan Output")
plt.xlabel("Variabel")
plt.ylabel("Nilai")

plt.show()