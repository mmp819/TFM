import pandas as pd
import numpy as np
from geopy.distance import geodesic
import os

# Constantes y directorios
INPUT = "dataset.csv"           # CSV a procesar
OUTPUT_DIR = "vehicles_csv"     # Directorio de salida
NUM_VEHICLES = 11
NUM_SECTORS = 4
LAT_OFFSET = 0.00008
LON_OFFSET = 0.00012
TIME_OFFSET = 2.0
INTERVAL_S = 1.0 / 10.0         # 1s / 10Hz

def calculate_sector(lat, sector_bounds):
    # Asigna una muestra a un sector concreto en funcion de su latitud.

    # Params:
    #   - lat: Latitud en base a la que asignar el sector.
    #   - sector_bounds: Latitudes limites de los sectores.
    # Returns:
    #   Sector asignado.

    for i in range(NUM_SECTORS):
        if sector_bounds[i] <= lat < sector_bounds[i + 1]:
           return i
    return NUM_SECTORS - 1

def shift_time(timestamp, i):
    # Ajustar el timestamp con un determinado desfase en funcion del vehiculo.

    # Params:
    #   - timestamp: Timestamp original
    #   - i: Numero de vehiculo/ID
    # Returns:
    #   Timestamp ajustado en segundos.

    h, m, s_us = timestamp.split('-') # Separa los valores en Horas, Minutos, Segundos-Microsegundos: Original (12-34-56.123456)
    s, us = map(float, s_us.split('.'))
    total = int(h) * 3600 + int(m) * 60 + s + us / 1e6
    return total + i * TIME_OFFSET

def complete_lost_samples(df):
    # Completar el dataset si falta alguna muestra, insertando una fila solo con el timestamp.
    #
    # Params:
    #   - df: Dataframe.
    # Returns: Dataframe modificado.
    df = df.sort_values("timestamp").reset_index(drop=True)
    output_rows = []

    for i in range(len(df) - 1):
        output_rows.append(df.iloc[i])
        t0 = df.iloc[i]["timestamp"]
        t1 = df.iloc[i + 1]["timestamp"]
        while t1 - t0 > INTERVAL_S:
            t0 += INTERVAL_S
            empty_row = {col: np.nan for col in df.columns}
            empty_row["timestamp"] = t0
            output_rows.append(pd.Series(empty_row))

    output_rows.append(df.iloc[-1])
    return pd.DataFrame(output_rows).reset_index(drop=True)


def main():
    # Columnas a conservar
    columns_needed = [
        "timestamp", "unit1_gps1_lat", "unit1_gps1_lon", "unit1_gps1_altitude",
        "unit1_gps1_hdop", "unit1_gps1_pdop", "unit1_gps1_vdop"
    ]

    # Cargar datos
    df_0 = pd.read_csv(INPUT)[columns_needed].copy()
    df_0.columns = ["timestamp", "gps_latitude", "gps_longitude", "gps_altitude", "gps_hdop", "gps_pdop", "gps_vdop"]

    # Calcular los sectores a simular
    min_lat = df_0["gps_latitude"].min()
    max_lat = df_0["gps_latitude"].max()
    sector_bounds = np.linspace(min_lat, max_lat, NUM_SECTORS + 1) # Limites totales

    # Procesado de vehiculos
    for i in range(NUM_VEHICLES):
        vehicle_id = f"veh_{i+1:02}"
        df = df_0.copy()

        # Desfase por vehiculo
        df["gps_latitude"] += i * LAT_OFFSET
        df["gps_longitude"] += i * LON_OFFSET
        df["timestamp"] = df["timestamp"].apply(lambda ts: shift_time(ts, i))

        # Calcular velocidad entre puntos
        df["speed"] = 0.0
        for j in range(1, len(df)):
            pos1 = (df.at[j-1, "gps_latitude"], df.at[j-1, "gps_longitude"])
            pos2 = (df.at[j, "gps_latitude"], df.at[j, "gps_longitude"])
            d = geodesic(pos1, pos2).meters
            df.at[j, "speed"] = d * 10  # 10Hz (Velocidad = Distancia / Tiempo (* Hz))

        # Asignar sector
        df["sector_id"] = df["gps_latitude"].apply(lambda lat: calculate_sector(lat, sector_bounds))
        df["vehicle_id"] = vehicle_id

        # Guardar archivo por vehículo
        df = complete_lost_samples(df)
        new_columns = ["vehicle_id", "timestamp", "gps_latitude", "gps_longitude", "gps_altitude", "gps_hdop", "gps_pdop", "gps_vdop", "speed", "sector_id"]
        df[new_columns].to_csv(f"{OUTPUT_DIR}/{vehicle_id}.csv", index=False)

    print("Dataset procesado.")

main()