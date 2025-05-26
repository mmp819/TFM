# Dependencias
import pandas as pd
import numpy as np
import os

# Constantes y directorios
INPUT_DIR = "vehicles_csv"
DELTA_FILTER = 0.0003
HZ = 10.0
INTERVAL = 1.0 / HZ

def create_window(lat, lon):
	# Params:
	#	lat: Latitud.
	#	lon: Longitud.
	# Return: Lista de 4 coordenadas, que definen un rectangulo de proximidad en torno al vehiculo.
	
	return [
		lat - DELTA_FILTER,
		lat + DELTA_FILTER,
		lon - DELTA_FILTER,
		lon + DELTA_FILTER
	]
	
def main():
	vehicles = {}
	for file in os.listdir(INPUT_DIR):
		df = pd.read_csv(os.path.join(INPUT_DIR, file))
		vehicles[file] = df
		
	# Verificar que existen cambios de sector
	print("Verificando si existen cambios de sector...")
	for v, df in vehicles.items():
		sectors = df["sector_id"].dropna().unique()
		if len(sectors) > 1:
			print(f"El vehiculo {v} circula por los sectores {sectors}")
			
	# Verificar si existen filas solo con timestamp (errores en la toma a 10Hz)
	print("Verificando si existen filas que solo tengan timestamp...")
	for v, df in vehicles.items():
		rows = df.drop(columns=["timestamp"]).isna().all(axis=1).sum()
		if rows > 0:
			print(f"El vehiculo {v} tiene {rows} filas vacias")
			
	# Verificar si existe una frecuencia constante de 10Hz entre muestras
	print("Verificando que la frecuencia de las muestras es constante...")
	for v, df in vehicles.items():
		timestamps = df["timestamp"].values
		diffs = np.diff(timestamps)
		if np.allclose(diffs, INTERVAL, atol=1e-2):
			print(f"Dataset del vehiculo {v}: OK")
		else:
			print(f"Dataset del vehiculo {v}: Errores")
	
	# Verificar que existen casos de proximidad entre vehiculos
	print("Verificando que pueden existir comunicaciones por proximidad...")
	vehicles_id = list(vehicles.keys())
	positions = {
		vehicle: df.dropna(subset=["gps_latitude", "gps_longitude"])[["gps_latitude", "gps_longitude"]].mean()
		for vehicle, df in vehicles.items()
	}
	
	for i in range(len(vehicles_id)):
		for j in range(i + 1, len(vehicles_id)):
		    v1, v2 = vehicles_id[i], vehicles_id[j]
		    lat1, lon1 = positions[v1]
		    lat2, lon2 = positions[v2]
		    win = create_window(lat1, lon1)
		    if win[0] <= lat2 <= win[1] and win[2] <= lon2 <= win[3]:
		        print(f"{v1} cercano con {v2}")

main()

