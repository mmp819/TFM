from prometheus_client import start_http_server, Gauge
from RoutingServiceMonitoring import RTI_Service_Monitoring_Periodic as Periodic
from RoutingServiceMonitoring import RTI_Service_Monitoring_ResourceKind as Kind

import time
import rti.connextdds as dds
import argparse

# Objetivo de monitorizacion
TOPIC_NAME = "rti/service/monitoring/periodic"

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
    parser.add_argument("--domain", type=int, required=True)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    participant = dds.DomainParticipant(args.domain)
    topic = dds.Topic(participant, TOPIC_NAME, Periodic)

    qos = dds.DataReaderQos()
    qos.data_representation = dds.DataRepresentation([dds.DataRepresentation.XCDR,
                                                      dds.DataRepresentation.XCDR2])
    qos.durability.kind = dds.DurabilityKind.TRANSIENT_LOCAL

    reader = dds.DataReader(participant, topic, qos)

    start_http_server(args.port)

    while True:
        for sample in reader.take():
            if not sample.info.valid:
                continue
            data = sample.data
            union = data.value
            kind = union.discriminator
            
            # LECTURA DE GUID
            # guid = data.object_guid.value
            # guid_str = ''.join(f'{b:02x}' for b in guid)
            # print("GUID del recurso:", guid_str)	

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

        time.sleep(3) # Actualizar cada tres segundos

main()

