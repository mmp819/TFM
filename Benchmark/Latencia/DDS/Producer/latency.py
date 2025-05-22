# Importar dependencias
import enum
import subprocess
import json
import sys

# Interfaz de red
NIC = sys.argv[1]

# Tamanhos de Payload a probar
PAYLOAD_SIZES = [
    32,           # 32B
    64,           # 64B
    128,          # 128B
    256,          # 256B
    512,          # 512B
    1024,         # 1KB
    2048,         # 2KB
    4096,         # 4KB
    8192,         # 8KB
    16384,        # 16KB
    32768,        # 32KB
    63000]        # Maximo tamanho permitido por UDP para el TEST ~ 64KB aprox.


# Modos admitidos en la prueba
RELIABILITIES = ["", "-bestEffort"] # Reliable / Best Effort

# Tiempo de ejecucion
TIME = 5 # Seconds

# Ruta hacia el ejecutable de la herramienta
RTI_PERF_TOOL = ("~/rti_workspace/7.3.0/utilities/perftest/4.1/bin/"
    "x64Linux4gcc7.3.0/release/perftest_cpp"
)

class Reliability(enum.Enum):
    RELIABLE = 0
    BEST_EFFORT = 1

def execute_producer(payload_size, reliability, domain):
    # Ejecuta un productor DDS.
    # Params:
    #   payload_size (int): Tamanho en Bytes.
    #   reliability (Reliability): 0 -> RELIABLE / 1 -> BEST_EFFORT
    #   domain (int): Domain ID.
    
    # Returns:
    #   stdout (str): Output del comando.

    # Construccion de comando
    cmd = (f"{RTI_PERF_TOOL} -pub -latencyTest -dataLen {payload_size} "
           f"-executionTime {TIME} -domain {domain} -nic {NIC} " 
           f"{RELIABILITIES[reliability]} -noPrint ")
    # Ejecucion
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process.stdout

def parse_output(output): 
    # Procesa el output proveniente de un productor DDS.
    # Params:
    #   output (str): Output a procesar.
    
    # Returns:
    #   result (dict): Diccionario con estadisticas de latencias.
    
    for line in output.split("\n"):
        if not line.startswith("Sample Size"):
            fields = line.split(", ")
            result = {
                "latency_avg_ms": float(fields[1].strip()) / 1000.0,
                "latency_max_ms": float(fields[4].strip()) / 1000.0,
                "latency_min_ms": float(fields[3].strip()) / 1000.0,
                "latency_p50_ms": float(fields[5].strip()) / 1000.0,
                "latency_p90_ms": float(fields[6].strip()) / 1000.0,
                "latency_p99_ms": float(fields[7].strip()) / 1000.0,
                "latency_p9999_ms": float(fields[8].strip()) / 1000.0
            }
            return result
    print("ERROR WHILE PARSING")

def main():
    domain = 1
    results = {}
    for payload_size in PAYLOAD_SIZES:
        print(f"Producer sending {payload_size} B / {payload_size / 1024} KB with reliability. - Domain {domain}")
        results[payload_size] = parse_output(execute_producer(payload_size, Reliability.RELIABLE.value, domain))
        print(results[payload_size])
        domain = domain + 1
    with open(f"../producer_results_reliable.json", "w") as file:
        json.dump(results, file, indent=4)
    
    for payload_size in PAYLOAD_SIZES:
        print(f"Producer sending {payload_size} B / {payload_size / 1024} KB with best effort. - Domain {domain}")
        results[payload_size] = parse_output(execute_producer(payload_size, Reliability.BEST_EFFORT.value, domain))
        print(results[payload_size])
        domain = domain + 1
    with open(f"../producer_results_bestEffort.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    main()
