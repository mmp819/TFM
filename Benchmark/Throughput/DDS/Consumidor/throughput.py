# Importar dependencias
import subprocess
import enum
import argparse
import json

# Tamanhos de payload a probar
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
    63000]        # Max size UDP allowed on TEST ~ 64KB almost

# Modos admitidos en la prueba
RELIABILITIES = ["", "-bestEffort"] # Reliable / Best Effort

# Ruta hacia el ejecutable de la herramienta
RTI_PERF_TOOL = ("~/rti_workspace/7.3.0/utilities/perftest/4.1/bin/"
    "x64Linux4gcc7.3.0/release/perftest_cpp"
)

class Reliability(enum.Enum):
    RELIABLE = 0
    BEST_EFFORT = 1

def execute_consumer(reliability, domain, multiPub, payload_size, nic):
    # Ejecuta un consumidor DDS.

    # Params:
    #    reliability (Reliability): Reliability mode.
    #    domain (int): Domain ID.
    #    multiPub (string): Null --> Single Pub.
    #    payload_size (int): Tamanho del payload en Bytes.
    #    nic: Interfaz de salida.  
    # Returns:
    #    stdout (str): Standard output of the command.

    cmd = ""
    if multiPub:
        cmd = (f"{RTI_PERF_TOOL} -sub {RELIABILITIES[reliability.value]} "
            f"-noPrint -domain {domain} -nic {nic} -dataLen {payload_size} "
            "-numPublishers 2"
        )
    else:
        cmd = (f"{RTI_PERF_TOOL} -sub {RELIABILITIES[reliability.value]} "
            f"-noPrint -domain {domain} -nic {nic} -dataLen {payload_size} "
        )
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process.stdout

def parse_output(output):
    # Procesa el output originado por el consumidor.

    # Params:
    #    output (str): Output a procesar.
    # Returns:
    #    result (dict): Diccionario con las estadisticas de throughput.
    
    for line in output.split("\n"):
        if not line.startswith("Sample Size"):
            fields = line.split(", ")
            result = {"throughput_MBps": float(fields[3].strip()),
                      "total_samples": float(fields[1].strip()),
                      "percentage_lost_samples": float(fields[5].strip())}
            return result
    print("ERROR WHILE PARSING")

def main():
    parser = argparse.ArgumentParser(description="Throughput test for DDS.")
    parser.add_argument("nic", help="Consumer network interface.")
    parser.add_argument("--multiPub", action="store_true", help="Execute test whit 2 publishers mode.")
    args = parser.parse_args()
    results = {}

    domain = 1
    for payload_size in PAYLOAD_SIZES:
        print(f"Executing consumer of {payload_size} B / {payload_size / 1024} KB with reliability. - Domain {domain}")
        output = execute_consumer(Reliability.RELIABLE, domain, args.multiPub, payload_size, args.nic)
        print(output)
        domain = domain + 1
        results[payload_size] = parse_output(output)
    
    with open(f"../consumer_results_reliability.json", "w") as file:
        json.dump(results, file, indent=4)
    """
    for payload_size in PAYLOAD_SIZES:
        print(f"Executing consumer of {payload_size} B / {payload_size / 1024} KB with best effort. - Domain {domain}")
        output = execute_consumer(Reliability.BEST_EFFORT, domain, args.multiPub, payload_size, args.nic)
        print(output)
        domain = domain + 1
        results[payload_size] = parse_output(output)

    with open(f"../producer_results_bestEffort.json", "w") as file:
        json.dump(results, file, indent=4)
    """
if __name__ == "__main__":
    main()  
