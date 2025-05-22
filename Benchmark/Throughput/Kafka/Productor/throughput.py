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
BATCH = 6400
LINGER = 100

# Paths de interes
KAFKA_TOOL_PATH = ("~/kafka_2.13-3.9.0/bin/kafka-producer-perf-test.sh"
    )
KAFA_TOPICS_PATH = ("~/kafka_2.13-3.9.0/bin/kafka-topics.sh"
    )

def execute_producer(payload_size, bs_server, topic_number):
    # Ejecuta el comando asignado al test de throughput de Kafka.

    # Params:
    #    payload_size (int): Tamanho del payload en Bytes.
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    process (CompletedProcess[str]): Informacion de salida del comando.

    cmd = (f"{KAFKA_TOOL_PATH} --topic {TOPIC + str(topic_number)} --throughput -1 "
        f"--record-size {payload_size} --num-records {NUM_MESSAGES} "
        f"--producer-props bootstrap.servers={bs_server} acks=1 batch.size={BATCH} "
        f"linger.ms={LINGER}"
    ) 
    
    """
    cmd = (f"{KAFKA_TOOL_PATH} --topic {TOPIC + str(topic_number)} --throughput -1 "
        f"--record-size {payload_size} --num-records {NUM_MESSAGES} "
        f"--producer-props bootstrap.servers={bs_server} "
    )"""
    
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process

def tool_throughput_broker(payload_size, bs_server, topic_number):
    # Llama a la ejecucion del test de throughput provisto por Kafka.

    # Params:
    #    payload_size (int): Tamanho del payload en Bytes.
    #    bs_server (string): <IP:PORT> del servidor Bootstrap.
    #    topic_number (int): Identificador o nombre del topico.
    # Returns:
    #    stdout (str): Output del comando.

    output = execute_producer(payload_size, bs_server, topic_number)
    if output.stderr:
        print(f"Producer performance tool test ERROR: {output.stderr}")
        return None
    
    return output.stdout

def parser_throughput_e2b(output):
    # Procesa el output proveniente de la ejecucion del test.
    # Params:
    #    output (str): Output a procesar.
    # Returns:
    #    result (dict): Estadisticas de throughput.

    result = {}
    lineas = output.split("\n")
    for linea in lineas:
        if "records/sec" in linea:
            start = linea.find("(") + 1
            end = linea.find(" MB/sec)")
            if start > 0 and end > start:
                throughput = linea[start:end].replace(",", ".")
                result = {"throughput_MBps": float(throughput)}
                break
    return result

def delete_topic(bs_server, topic):
    # Elimina un topico de Kafka.

    # Params:
    #     bs_server (string): <IP:PORT> del servidor Bootstrap.
    #     topic (str): Nombre (numero) del topico.
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
    #    topic (str): Nombre (numero) del topico.
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
        create_topic(bootstrap_server, TOPIC + str(i))

    print("Starting THROUGHPUT-TEST...")
    results = {}
    topic_n = 0
    
    print("\nStarting throughput test...")
    for payload_size in PAYLOAD_SIZES:
        print(f"\nProducer sending {payload_size} B or {payload_size / 1024} KB - Topic {TOPIC + str(topic_n)}\n")
        output = tool_throughput_broker(payload_size, bootstrap_server, topic_n)
        results[payload_size] = parser_throughput_e2b(output)
        topic_n = topic_n + 1
        print(results[payload_size])
        time.sleep(5)
    with open("tool_throughput_e2b_test_results_prod.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nCleaning topics...")
    for i in range(len(PAYLOAD_SIZES)):
        print(f"\nCleaning topic {TOPIC + str(i)}...")
        delete_topic(bootstrap_server, TOPIC + str(i))
        create_topic(bootstrap_server, TOPIC + str(i))

if __name__ == "__main__":
    main()  
