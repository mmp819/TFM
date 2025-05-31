from prometheus_client import start_http_server, Gauge
from ServiceMonitoring import RTI_Service_Monitoring_Periodic as Periodic
from ServiceMonitoring import RTI_Service_Monitoring_Config as Config
from ServiceMonitoring import RTI_Service_Monitoring_ResourceKind as Kind

import time
import rti.connextdds as dds
import argparse

# Objetivo de monitorizacion

TOPIC_PERIODIC = "rti/service/monitoring/periodic"
TOPIC_CONFIG = "rti/service/monitoring/config"

# Diccionario GUID - Nombre
guid_name = {}

def guid_to_str(guid_bytes):
    # Convierte el identificador a un formato legible en String.
    # Params:
    #   - guid_bytes: GUID a convertir.
    # Returns:
    # GUID en formato String.
    return ''.join(f'{b:02x}' for b in guid_bytes)


# Definicion de metricas de Prometheus
# HOST - ROUTING SERVICE
cpu_usage = Gauge("rti_routing_service_cpu", "CPU Usage (%)", ["instance"])
free_mem = Gauge("rti_routing_service_mem_free", "Free Memory (KB)", ["instance"])
free_swap = Gauge("rti_routing_service_swap_free", "Free Swap (KB)", ["instance"])
uptime = Gauge("rti_routing_service_uptime", "Uptime (Seconds)", ["instance"])

# DOMAIN ROUTE
domain_route_in_samples = Gauge("rti_domain_route_input_samples", 
                                "Input samples/s", ["domain_route"])
domain_route_in_bytes = Gauge("rti_domain_route_input_bytes",
                              "Input bytes/s", ["domain_route"])
domain_route_out_samples = Gauge("rti_domain_route_output_samples",
                                 "Ouput samples/s", ["domain_route"])
domain_route_out_bytes = Gauge("rti_domain_route_output_bytes"
                               "Output bytes/s", ["domain_route"])
domain_route_latency = Gauge("rti_domain_route_latency",
                             "Avg. Latency (ms)", ["domain_route"])

# ROUTE (TOPIC)
route_in_samples = Gauge("rti_route_input_samples",
                         "Input samples/s", ["route"])
route_in_bytes = Gauge("rti_route_input_bytes",
                       "Input bytes/s", ["route"])
route_out_samples = Gauge("rti_route_output_samples", 
                          "Output samples/s", ["route"])
route_out_bytes = Gauge("rti_route_output_bytes",
                        "Output bytes/s", ["route"])
route_latency = Gauge("rti_route_latency",
                    "Latency (ms)", ["route"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--domain", type=int, required=True) # Dominio a exportar
    parser.add_argument("--port", type=int, default=8000) # Puerto donde exponer metricas
    args = parser.parse_args()

    participant = dds.DomainParticipant(args.domain)

    qos = dds.DataReaderQos()
    qos.data_representation = dds.DataRepresentation([dds.DataRepresentation.XCDR,
                                                      dds.DataRepresentation.XCDR2])
    qos.durability.kind = dds.DurabilityKind.TRANSIENT_LOCAL

    topic_periodic = dds.Topic(participant, TOPIC_PERIODIC, Periodic)
    topic_config = dds.Topic(participant, TOPIC_CONFIG, Config)    

    reader_periodic = dds.DataReader(participant, topic_periodic, qos)
    reader_config = dds.DataReader(participant, topic_config, qos)

    start_http_server(args.port)

    while True:

        # Cargar o actualizar las equivalencias entre GUIDs y nombres de recursos
        for sample in reader_config.take():
            if not sample.info.valid:
                continue
            data = sample.data
            guid = guid_to_str(data.object_guid.value)
            try:
                name = data.value.value.resource_id

            except Exception:
                name = f"<none_name_kind:{data.value.discriminator}>"
            guid_name[guid] = name

        # Cargar o actualizar metricas
        for sample in reader_periodic.take():
            if not sample.info.valid:
                continue
            data = sample.data
            guid = guid_to_str(data.object_guid.value)
            name = guid_name.get(guid, guid)
            union = data.value
            kind = union.discriminator
            try: 
                if kind == Kind.ROUTING_SERVICE:
                    metrics = union.routing_service.host
                    cpu_usage.labels(instance=name).set(metrics.cpu_usage_percentage.publication_period_metrics.mean)
                    free_mem.labels(instance=name).set(metrics.free_memory_kb.publication_period_metrics.mean)
                    free_swap.labels(instance=name).set(metrics.free_swap_memory_kb.publication_period_metrics.mean)
                    uptime.labels(instance=name).set(metrics.uptime_sec.publication_period_metrics.mean)

                elif kind == Kind.ROUTING_DOMAIN_ROUTE:
                    metrics = data.resource_data.routing_domain_route
                    domain_route_in_samples.labels(domain_route=name).set(metrics.in_samples_per_sec.publication_period_metrics.mean)
                    domain_route_in_bytes.labels(domain_route=name).set(metrics.in_bytes_per_sec.publication_period_metrics.mean)
                    domain_route_out_samples.labels(domain_route=name).set(metrics.output_samples_per_sec.publication_period_metrics.mean)
                    domain_route_out_bytes.labels(domain_route=name).set(metrics.output_bytes_per_sec.publication_period_metrics.mean)
                    domain_route_latency.labels(domain_route=name).set(metrics.latency_millisec.publication_period_metrics.mean)

                elif kind == Kind.ROUTING_ROUTE:
                    metrics = data.resource_data.routing_route
                    route_in_samples.labels(route=name).set(metrics.in_samples_per_sec.publication_period_metrics.mean)
                    route_in_bytes.labels(route=name).set(metrics.in_bytes_per_sec.publication_period_metrics.mean)
                    route_out_samples.labels(route=name).set(metrics.output_samples_per_sec.publication_period_metrics.mean)
                    route_out_bytes.labels(route=name).set(metrics.output_bytes_per_sec.publication_period_metrics.mean)
                    route_latency.labels(route=name).set(metrics.latency_millisec.publication_period_metrics.mean)
            except Exception as e:
                print(f"Error con la muestra de {kind}:{name}: {e}")

        time.sleep(3) # Actualizar cada tres segundos

if __name__ == "__main__":
    main()

