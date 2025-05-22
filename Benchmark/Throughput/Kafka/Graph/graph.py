# Importar dependencias
import json
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los archivos JSON
files = {
    "prod_2to1": "../tool_throughput_e2b_test_results_prod_2to1.json",
    "prod_1to1": "../tool_throughput_e2b_test_results_prod_1to1.json",
    "prod2_2to1": "../tool_throughput_e2b_test_results_prod2_2to1.json",
    "cons_2to1": "../tool_throughput_e2b_test_results_cons_2to1.json",
    "cons_1to1": "../tool_throughput_e2b_test_results_cons_1to1.json"
}

# Leer los datos y convertirlos a DataFrames
dataframes = {}
for key, path in files.items():
    with open(path, "r") as file:
        data = json.load(file)
        df = pd.DataFrame(data).T
        df.index = df.index.astype(int)  # Convertir los tamaños de mensaje a enteros
        df = df.sort_index()  # Asegurar que los tamaños estén ordenados
        df["throughput_Mbps"] = df["throughput_MBps"] * 8  # Convertir MBps a Mbps
        dataframes[key] = df

# Crear la grafica
plt.figure(figsize=(14, 10))

# Estilo para las lineas de cada categoria
styles = {
    "prod_1to1": {"label": "Producer (1 to 1)", "linestyle": "-", "color": "blue"},
    "cons_1to1": {"label": "Consumer (1 to 1)", "linestyle": "-", "color": "green"},
    "prod_2to1": {"label": "Producer 1 (2 to 1)", "linestyle": "--", "color": "blue"},
    "prod2_2to1": {"label": "Producer 2 (2 to 1)", "linestyle": "--", "color": "orange"},
    "cons_2to1": {"label": "Consumer (2 to 1)", "linestyle": "--", "color": "green"}
}

# Orden especifico para la leyenda
plot_order = ["prod_1to1", "cons_1to1", "prod_2to1", "prod2_2to1", "cons_2to1"]

# Graficar cada conjunto de datos en el orden deseado
for key in plot_order:
    df = dataframes[key]
    plt.plot(
        df.index,  # Tamanhos de mensaje
        df["throughput_Mbps"],  # Throughput en Mbps
        label=styles[key]["label"],
        linestyle=styles[key]["linestyle"],
        color=styles[key]["color"]
    )

# Configurar la gráfica
plt.xscale("log")
plt.xticks(df.index, df.index, rotation=45)
plt.xlabel("Message Size (bytes)", fontsize=12)
plt.ylabel("Throughput (Mbps)", fontsize=12)
plt.title("Throughput Comparison: Producers and Consumers", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which="major", linestyle="--", linewidth=0.5)
plt.tight_layout()

# Guardar la gráfica como PNG
plt.savefig("throughput_comparison_styled.png")
