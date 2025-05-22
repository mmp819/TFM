# Importar dependencias
import subprocess
import sys
import json
import time 

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

# Paramemtros del test
NUM_MESSAGES = 100000
TOPIC = "throughput-test-"
FETCH_SIZE = 204800 # DDS -> Queue x Batch

# Paths de interes
KAFKA_TOOL_PATH = ("~/kafka_2.13-3.9.0/bin/kafka-consumer-perf-test.sh"
)

def execute_consumer(bs_server, topic_number):
    # Ejecuta el comando asignado al test de throughput de Kafka.

    # Params:
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    process (CompletedProcess[str]): Informacion de salida del comando.
    cmd = (f"{KAFKA_TOOL_PATH} --topic {TOPIC + str(topic_number)} "
        f"--messages {NUM_MESSAGES} --bootstrap-server {bs_server} "
        f"--group {TOPIC + str(topic_number)} --fetch-size {FETCH_SIZE}"
    )
    
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process

def tool_throughput_broker(bs_server, topic_number):
    # Llama a la ejecucion del test de throughput provisto por Kafka.

    # Params:
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    stdout (str): Output del comando.
    
    output = execute_consumer(bs_server, topic_number)
    if output.stderr:
        print(f"Consumer performance tool test ERROR: {output.stderr}")
        return None
    
    return output.stdout

def parse_output(output):
    # Procesa el output proveniente de la ejecucion del test.
    # Params:
    #    output (str): Output a procesar.
    # Returns:
    #    result (dict): Estadisticas de throughput.

    result = {}
    lineas = output.split("\n")
    for linea in lineas:
        if not linea.startswith("start.time"):
            fields = linea.split(", ")
            result = {"throughput_MBps": float(fields[3].strip().replace(",", ".")),
                      "total_samples": float(fields[4].strip().replace(",", "."))}
            return result
    print("ERRROR WHILE PARSING")


def main():
    print("Starting THROUGHPUT-TEST...")
    topic_n = 0
    results = {}
    bootstrap_server = sys.argv[1]
    for payload_size in PAYLOAD_SIZES:
        print(f"\nConsumer receiving {payload_size} B / {payload_size / 1024} KB - Topic {TOPIC + str(topic_n)}\n")
        output = tool_throughput_broker(bootstrap_server, topic_n)
        topic_n = topic_n + 1
        print(output)
        results[payload_size] = parse_output(output)
        time.sleep(5)
        

    with open("tool_throughput_e2b_test_results_cons.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    main()  
