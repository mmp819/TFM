import rti.connextdds as dds
import time

from vehicle_data import VehicleSimulation

AGGREGATION_PERIOD = 5.0  # Segundos
DOP_LIMIT_FILTER = 5.0    # Limite de calidad
AGGREGATION_DOMAIN = 10
STATE_TOPIC = "VehicleState"
AGGREGATION_TOPIC = "AggregatedVehicleData"

sector_data = {}

def aggregate_and_publish(writer):
    # Agrega los datos disponibles por sector y los publica en el topico
    # correspondiente.
    #
    # Params:
    #   - writer: DataWriter encargado de la publicacion.
    # Returns:
    #   Void
    timestamp = time.time()
    for sector_id in list(sector_data.keys()):  # Para cada sector registrado
        samples = sector_data[sector_id]
        if not samples:
            continue
        
        # Calcular agregados
        speeds = [sample.speed for sample in samples]
        vehicle_ids = set(sample.vehicle_id for sample in samples)
        avg_speed = sum(speeds) / len(speeds)
        vehicle_count = len(vehicle_ids)
        congestion = vehicle_count / 10.0 # Formula simplificada
        
        # Publicar agregados
        aggregation = VehicleSimulation.AggregatedData(
            sector_id = sector_id,
            avg_speed = avg_speed,
            vehicle_count = vehicle_count,
            congestion_lvl = congestion,
            timestamp = timestamp
        )
        writer.write(aggregation)
        # Mensaje util para debug o depositar en .log
        print(f"Datos agregados - Sector {sector_id}: {vehicle_count} vehiculos | \
              Velocidad (Avg): {avg_speed:.2f} km/h | Atasco (Lvl): {congestion:.2f}")
        
        # Vaciar datos del sector
        sector_data[sector_id] = []

def main():

    # Definicion de entidades
    participant = dds.DomainParticipant(AGGREGATION_DOMAIN)
    state_topic = dds.Topic(participant, STATE_TOPIC, VehicleSimulation.VehicleState)
    aggregation_topic = dds.Topic(participant, AGGREGATION_TOPIC, VehicleSimulation.AggregatedVehicleData)

    reader = dds.DataReader(participant.implicit_subscriber, state_topic)
    writer = dds.DataWriter(participant.implicit_publisher, aggregation_topic)

    t_0 = time.time()

    while True:
        for data in reader.take():
            if data.info.valid:
                sample = data.data
                # Descartar muestra si no es fiable
                if (sample.gps_pdop > DOP_LIMIT_FILTER or
                    sample.gps_hdop > DOP_LIMIT_FILTER or 
                    sample.gps_vdop > DOP_LIMIT_FILTER):
                    continue

                if sample.sector_id not in sector_data: # Crear registro del sector si no existe
                    sector_data[sample.sector_id] = [] 

                sector_data[sample.sector_id].append(sample)
        
        if (time.time() - t_0 >= AGGREGATION_PERIOD):
            aggregate_and_publish(writer)
            t_0 = time.time()

if __name__ == "__main__":
    main()
