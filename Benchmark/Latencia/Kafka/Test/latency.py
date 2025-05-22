# Importar dependencias
import subprocess
import sys 
import json
import time

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
    63000]        # Max size UDP allowed on TEST ~ 64KB almost

# Numero de mensajes
NUM_MESSAGES = 10000
# Topico
TOPIC = "latency-test-"
# Paths de interes para la ejecucion del test
KAFKA_TOOL_E2E_PATH = ("~/kafka_2.13-3.9.0/bin/kafka-e2e-latency.sh "
    )
KAFA_TOPICS_PATH = ("~/kafka_2.13-3.9.0/bin/kafka-topics.sh "
    )

def execute_e2e(payload_size, bs_server, topic_number):
    # Ejecuta el comando asignado al test de latencia end to end de Kafka.

    # Params:
    #    payload_size (int): Tamanho del payload en Bytes.
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    process (CompletedProcess[str]): Informacion de salida del comando.
    
    cmd = (
        f"{KAFKA_TOOL_E2E_PATH} {bs_server} {TOPIC + str(topic_number)} {payload_size} 1 {NUM_MESSAGES}"
    )
    
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process

def tool_ping_e2e(payload_size, bs_server, topic_number):
    # Llama a la ejecucion del test de latencia E2E provisto por Kafka.

    # Params:
    #    payload_size (int): Tamanho del payload en Bytes.
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    stdout (str): Output del comando.
    

    output = execute_e2e(payload_size, bs_server, topic_number)
    if output.stderr:
        print(f"E2E performance tool test ERROR: {output.stderr}")
        return None
    return output.stdout

def parser_tool_e2e(output):
    # Procesa el output proveniente de la ejecucion del test.
    # Params:
    #    output (str): Output a procesar.
    # Returns:
    #    result (dict): Diccionario con las estadisticas de latencias.
    
    lines = output.split("\n")
    avg_ms = 0.0
    p50_ms = 0.0
    p99_ms = 0.0
    p999_ms = 0.0
    for line in lines:
        if "Avg latency" in line:
            avg_ms = float(line.split()[2].replace(",", "."))
        elif "Percentiles" in line:
            p50_ms = float(line.split()[3].replace(",", "."))
            p99_ms = float(line.split()[6].replace(",", "."))
            p999_ms = float(line.split()[9].replace(",", "."))
    result = {
        'latency_avg_ms': avg_ms,
        'latency_p50_ms': p50_ms,
        'latency_p99_ms': p99_ms,
        'latency_p999_ms': p999_ms
    }
    
    return result

def delete_topic(bs_server, topic):
    # Elimina un topico de Kafka.

    # Params:
    #     bs_server (string): <IP:PORT> del servidor Bootstrap.
    #     topic_number (str): Nombre (numero) del topico.
    # Returns:
    #    stdout (str): Output del comando.
    #    stderr (str): Posible output de error del comando.
    
    cmd = (f"{KAFA_TOPICS_PATH} --bootstrap-server {bs_server} --delete --topic {topic}")

    try: 
        output = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode("utf-8"), output.stderr.decode("utf-8")
    except subprocess.CalledProcessError as e:
        if "does not exist" not in e.stderr.decode('utf-8'):
            print(f"ERROR executing command: {cmd}\n{e.stderr.decode('utf-8')}")
        return None, e.stderr.decode("utf-8")
    
def create_topic(bs_server, topic):
    # Crea un topico de Kafka.

    # Params:
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (str): Nombre (numero) del topico.
    # Returns:
    #    stdout (str): Output del comando.
    #    stderr (str): Posible output de error del comando.
    
    cmd = (f"{KAFA_TOPICS_PATH} --bootstrap-server {bs_server} --create --topic {topic} --partitions 1 --replication-factor 1")

    try: 
        output = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.stdout.decode("utf-8"), output.stderr.decode("utf-8")
    except subprocess.CalledProcessError as e:
        if "does not exist" not in e.stderr.decode('utf-8'):
            print(f"ERROR executing command: {cmd}\n{e.stderr.decode('utf-8')}")
        return None, e.stderr.decode("utf-8")

def main():
    bootstrap_server = sys.argv[1]
    print("\nCleaning topics...")
    for i in range(len(PAYLOAD_SIZES)):
        print(f"\nCleaning topic {TOPIC + str(i)}...")
        delete_topic(bootstrap_server, TOPIC + str(i))
        time.sleep(1)
        create_topic(bootstrap_server, TOPIC + str(i))

    print("\nStarting E2E test...")
    topic_n = 0
    for payload_size in PAYLOAD_SIZES:
        print(f"\nProducer sending {payload_size} B / {payload_size / 1024} KB - Topic {TOPIC + str(topic_n)}\n")
        output = tool_ping_e2e(payload_size, bootstrap_server, topic_n)
        results[payload_size] = parser_tool_e2e(output)
        print(results[payload_size])
    with open("../tool_latency_e2e_test_results.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    main()  
