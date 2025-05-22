# Importar dependencias.
import json
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos JSON
e2e_path = "../tool_latency_e2e_test_results.json"

with open(e2e_path, "r") as file:
    e2e_data = json.load(file)

# Convertir los datos JSON a DataFrames y pasar a microsegundos
e2e_df = pd.DataFrame(e2e_data).T
e2e_df *= 1000

# Agregar una columna identificadora para facilitar el trazado
e2e_df["Type"] = "End-to-End"

# Agregar el tamanho del payload como columna
e2e_df["Size"] = e2e_df.index.astype(int)

# Crear la grafica
plt.figure(figsize=(12, 8))

# Pintar las latencias promedio para End-to-End
plt.plot(
    e2e_df[e2e_df["Type"] == "End-to-End"]["Size"],
    e2e_df[e2e_df["Type"] == "End-to-End"]["latency_avg_ms"],
    label="End-to-End - Latency Avg",
    marker='o'
)

# Configurar la grafica
plt.xscale("log")
plt.yscale("log")
plt.xticks(e2e_df["Size"].unique(), e2e_df["Size"].unique(), rotation=45)
plt.xlabel("Message Size (bytes)", fontsize=12)
plt.ylabel("Latency (microseconds)", fontsize=12)
plt.title("Latency Comparison: End-to-End", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="major", linestyle="--", linewidth=0.5)
plt.tight_layout()

# Guardar la grafica como PNG
plt.savefig("latency_kafka_e2e.png")
