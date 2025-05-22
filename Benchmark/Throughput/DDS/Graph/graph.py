import json
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos JSON
consumer_2to1_path = "../consumer_results_2to1.json"
consumer_1to1_path = "../consumer_results_1to1.json"

with open(consumer_2to1_path, "r") as file:
    consumer_2to1_data = json.load(file)

with open(consumer_1to1_path, "r") as file:
    consumer_1to1_data = json.load(file)

# Convertir los datos JSON a DataFrames
consumer_2to1_df = pd.DataFrame(consumer_2to1_data).T
consumer_1to1_df = pd.DataFrame(consumer_1to1_data).T

# Interpretar los valores como Mbps
consumer_2to1_df.rename(columns={"throughput_MBps": "throughput_Mbps"}, inplace=True)
consumer_1to1_df.rename(columns={"throughput_MBps": "throughput_Mbps"}, inplace=True)

# Agregar una columna identificadora para facilitar el trazado
consumer_2to1_df["Type"] = "2 to 1"
consumer_1to1_df["Type"] = "1 to 1"

# Agregar el tamanho del payload como columna
consumer_2to1_df["Size"] = consumer_2to1_df.index.astype(int)
consumer_1to1_df["Size"] = consumer_1to1_df.index.astype(int)

# Combinar los datos para comparacion
merged_df = pd.concat([consumer_2to1_df, consumer_1to1_df])

# Crear la grafica
plt.figure(figsize=(12, 8))
plt.plot(
    merged_df[merged_df["Type"] == "2 to 1"]["Size"],
    merged_df[merged_df["Type"] == "2 to 1"]["throughput_Mbps"],
    label="2 to 1 - Throughput",
    marker='o'
)
plt.plot(
    merged_df[merged_df["Type"] == "1 to 1"]["Size"],
    merged_df[merged_df["Type"] == "1 to 1"]["throughput_Mbps"],
    label="1 to 1 - Throughput",
    linestyle="--",
    marker='x'
)

# Configurar la grafica
plt.xscale("log")
plt.xticks(merged_df["Size"].unique(), merged_df["Size"].unique(), rotation=45)
plt.xlabel("Message Size (bytes)", fontsize=12)
plt.ylabel("Throughput (Mbps)", fontsize=12)
plt.title("Throughput Comparison: 2 to 1 vs 1 to 1", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="major", linestyle="--", linewidth=0.5)
plt.tight_layout()

# Guardar la grafica como PNG
plt.savefig("throughput_comparison.png")
