# Importar dependencias
import json
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos JSON
reliable_path = "../producer_results_reliable.json"
best_effort_path = "../producer_results_bestEffort.json"

with open(reliable_path, "r") as file:
    reliable_data = json.load(file)

with open(best_effort_path, "r") as file:
    best_effort_data = json.load(file)

# Convertir los datos JSON a DataFrames
reliable_df = pd.DataFrame(reliable_data).T
best_effort_df = pd.DataFrame(best_effort_data).T

# Convertir las latencias de ms a microsegundos
reliable_df *= 1000
best_effort_df *= 1000

# Agregar una columna identificadora para facilitar el trazado
reliable_df["Type"] = "Reliable"
best_effort_df["Type"] = "Best Effort"

# Agregar el tamanho del payload como columna
reliable_df["Size"] = reliable_df.index.astype(int)
best_effort_df["Size"] = best_effort_df.index.astype(int)

# Combinar los datos para comparar
merged_df = pd.concat([reliable_df, best_effort_df])

# Crear grafica
plt.figure(figsize=(12, 8))
plt.plot(
    merged_df[merged_df["Type"] == "Reliable"]["Size"],
    merged_df[merged_df["Type"] == "Reliable"]["latency_avg_ms"],
    label="Reliable - Latency Avg",
    marker='o'
)
plt.plot(
    merged_df[merged_df["Type"] == "Best Effort"]["Size"],
    merged_df[merged_df["Type"] == "Best Effort"]["latency_avg_ms"],
    label="Best Effort - Latency Avg",
    linestyle="--",
    marker='x'
)

# Configurar la grafica
plt.xscale("log")
plt.yscale("log")
plt.xticks(merged_df["Size"].unique(), merged_df["Size"].unique(), rotation=45)
plt.xlabel("Message Size (bytes)", fontsize=12)
plt.ylabel("Latency (microseconds)", fontsize=12)
plt.title("Latency Comparison: Reliable vs Best Effort", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="major", linestyle="--", linewidth=0.5)
plt.tight_layout()

# Guardar como PNG
plt.savefig("latency_comparison.png")
