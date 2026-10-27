from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import os

print("Folder Python berjalan:")
print(os.getcwd())

print("\nIsi folder:")
print(os.listdir())

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "data1.csv"

data = pd.read_csv(csv_path)

print(data.columns)

pctid_pilihan = 60

data_pilihan = data[data["pctid"] == pctid_pilihan].copy()
data_pilihan["data"] = range(len(data_pilihan))

plt.figure(figsize=(12, 6))

plt.plot(data_pilihan["data"], data_pilihan["x"], label="Vibrasi X")

plt.plot(data_pilihan["data"], data_pilihan["y"], label="Vibrasi Y")

plt.plot(data_pilihan["data"], data_pilihan["z"], label="Vibrasi Z")


plt.title(f"Data Vibrasi Akselerometer pada Kecepatan {pctid_pilihan}%")

plt.xlabel("Data")
plt.ylabel("Nilai Vibrasi")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()