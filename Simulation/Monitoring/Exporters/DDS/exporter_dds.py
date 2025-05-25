from prometheus_client import start_http_server, Gauge
from ServiceMonitoring import RTI_Service_Monitoring_Periodic as PeriodicType
from ServiceMonitoring import RTI_Service_Monitoring_ResourceKind as Kind

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
    topic = dds.Topic(participant, TOPIC_NAME, PeriodicType)

    qos = dds.DataReaderQos()
    qos.data_representation = dds.DataRepresentation([dds.DataRepresentation.XCDR,
                                                      dds.DataRepresentation.XCDR2])
    qos.durability.kind = dds.DurabilityKind.TRANSIENT_LOCAL

    reader = dds.DataReader(participant.implicit_subscriber, topic, qos)

    start_http_server(args.port)

    while True:
        for sample in reader.take():
            if not sample.info.valid:
                continue
            data = sample.data
            kind = data.resource.kind
            name = data.resource.name

            if kind == Kind.ROUTING_SERVICE:
                m = data.resource_data.routing_service.host_metrics
                cpu_usage.labels(instance=name).set(m.cpu_usage_percentage)
                free_mem.labels(instance=name).set(m.free_memory_kb)
                free_swap.labels(instance=name).set(m.free_swap_memory_kb)
                uptime.labels(instance=name).set(m.uptime_sec)

            elif kind == Kind.ROUTING_DOMAIN_ROUTE:
                m = data.resource_data.routing_domain_route
                domain_route_in_samples.labels(domain_route=name).set(m.in_samples_per_sec)
                domain_route_in_bytes.labels(domain_route=name).set(m.in_bytes_per_sec)
                domain_route_out_samples.labels(domain_route=name).set(m.output_samples_per_sec)
                domain_route_out_bytes.labels(domain_route=name).set(m.output_bytes_per_sec)
                domain_route_latency.labels(domain_route=name).set(m.latency_millisec)

            elif kind == Kind.ROUTING_ROUTE:
                m = data.resource_data.routing_route
                route_in_samples.labels(route=name).set(m.in_samples_per_sec)
                route_in_bytes.labels(route=name).set(m.in_bytes_per_sec)
                route_out_samples.labels(route=name).set(m.output_samples_per_sec)
                route_out_bytes.labels(route=name).set(m.output_bytes_per_sec)
                route_latency.labels(route=name).set(m.latency_millisec)

        time.sleep(3) # Actualizar cada tres segundos

main()

