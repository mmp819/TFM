# Dependencias
import rti.connextdds as dds
import csv
import time
import sys


# Tipos generados con RTI
from vehicle_data import VehicleSimulation

DELTA_FILTER = 0.0003
STATE_TOPIC = "Vehicle_State"
FILTERED_STATE_TOPIC = "Filtered_" + STATE_TOPIC
	
def create_window(lat, lon):
	# Params:
	#	lat: Latitud.
	#	lon: Longitud.
	# Return: Lista de 4 coordenadas, que definen un rectangulo de proximidad en torno al vehiculo.
	
	return [
		str(lat - DELTA_FILTER),
		str(lat + DELTA_FILTER),
		str(lon - DELTA_FILTER),
		str(lon + DELTA_FILTER)
	]
	
def create_entities(domain, filter_parameters):
	# Params:
	#	domain: Dominio en el que se establece la comunicacion.
	#	filter_parameters: Parametros aplicados en el filtro de lectura.
	# Return: Entidades necesarias para escribir y leer datos en DDS.

	# Crear DomainParticipant
	participant = dds.DomainParticipant(domain)
	
	# Crear entidades de publicacion
	topic = dds.Topic(participant, STATE_TOPIC, VehicleSimulation.VehicleState)
	writer = dds.DataWriter(participant.implicit_publisher, topic)
	
	# Crear entidades de consumo
	filter_expression = "gps_latitude > %0 AND gps_latitude < %1 AND gps_longitude > %2\
		AND gps_longitude < %3"
	ftr = dds.Filter(filter_expression, filter_parameters)
	filtered_topic = dds.ContentFilteredTopic(topic, "Filtered_Vehicle_State", ftr)
	reader = dds.DataReader(participant.implicit_subscriber, filtered_topic)
	
	return participant, writer, reader
	
def simulate_vehicle(csv_file):
	# Simula un vehiculo en movimiento, a partir de los datos incluidos en un fichero CSV.
	
	with open(csv_file, newline='') as csv_data:
		reader_csv = csv.DictReader(csv_data)
		rows = list(reader_csv)
	
	sector = int(float(rows[0]['sector_id']))
	vehicle_id = rows[0]['vehicle_id']
	lat = float(rows[0]['gps_latitude'])
	lon = float(rows[0]['gps_longitude'])
	filter_parameters = create_window(lat, lon)
	participant, writer, reader = create_entities(sector, filter_parameters)
    
	t0_real = time.time()
	t0_dataset = float(rows[0]['timestamp'])
    
	for row in rows:
		if not row['sector_id']: # No pudo tomarse muestra para dicho timestamp
			continue
		timestamp_dataset = float(row['timestamp'])
		sleep_time = (timestamp_dataset - t0_dataset) - (time.time() - t0_real)
		if sleep_time > 0:
			time.sleep(sleep_time)
		
		new_sector = int(float(row['sector_id']))
		lat = float(row['gps_latitude'])
		lon = float(row['gps_longitude'])
		filter_parameters = create_window(lat, lon)
	
		if sector != new_sector: # Cambio de sector
			participant.close()   		
			participant, writer, reader = create_entities(new_sector, filter_parameters)
			sector = new_sector
    	
		if reader.filter_parameters != filter_parameters: # Actualizar solo si es necesario
			reader.filter_parameters = filter_parameters
    	
    	# Crea la muestra a escribir en DDS
		sample = VehicleSimulation.VehicleState(
			vehicle_id = vehicle_id,
    		timestamp = timestamp_dataset,
    		gps_latitude = lat,
    		gps_longitude = lon,
    		gps_altitude = float(row['gps_altitude']),
    		gps_hdop = float(row['gps_hdop']),
    		gps_pdop = float(row['gps_pdop']),
    		gps_vop = float(row['gps_vdop']),
    		speed = float(row['speed'])
    	)
    	
    	# Escribe la muestra
		writer.write(sample)
    	
    	# Comprobar vehiculos cercanos - Posible aviso
		for data in reader.take():
			if data.info.valid and data.data.vehicle_id != vehicle_id:
				neighbour = data.data
				reliability_1 = sample.gps_pdop > 5.0 or sample.gps_hdop > 5.0 or sample.gps_vdop > 5.0
				reliability_2 = neighbour.gps_pdop > 5.0 or neighbour.gps_hdop > 5.0 or neighbour.gps_vdop > 5.0
				if reliability_1 or reliability_2:
					print(f"POSIBLE [{vehicle_id}] CERCANO A : {data.data.vehicle_id} EN ({data.data.gps_latitude}, {data.data.gps_longitude})")
				else:
					print(f"[{vehicle_id}] CERCANO A : {data.data.vehicle_id} EN ({data.data.gps_latitude}, {data.data.gps_longitude})")
	
simulate_vehicle(sys.argv[1])
	
	
