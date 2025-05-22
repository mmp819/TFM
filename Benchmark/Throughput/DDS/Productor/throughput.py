# Importar dependencias
import subprocess
import enum
import argparse

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
    63000]        # Maximo tamanho permitido por UDP para el TEST ~ 64KB aprox.

# Modos admitidos en la prueba
RELIABILITIES = ["", "-bestEffort"] # Reliable / Best Effort

# Ruta hacia el ejecutable de la herramienta
RTI_PERF_TOOL = ("~/rti_workspace/7.3.0/utilities/perftest/4.1/bin/"
    "x64Linux4gcc7.3.0/release/perftest_cpp"
)

# Iteraciones
ITER = 1000000

class Reliability(enum.Enum):
    RELIABLE = 0
    BEST_EFFORT = 1

def execute_producer(payload_size, reliability, domain, multiPub, nic):
    # Ejecuta un productor DDS.

    # Params:
    #    payload_size (int): Tamanho del payload en Bytes.
    #    reliability (Reliability): Reliability mode.
    #    domain (int): Domain ID.
    #    multiPub (string): Null --> Single Pub. 
    #    nic: Interfaz de salida.
    # Returns:
    #    stdout (str): Standard output of the command.

    if multiPub:
        cmd = (f"{RTI_PERF_TOOL} -pub -dataLen {payload_size} -batchSize 6400 "
            f"-numIter {ITER} -domain {domain} -nic {nic} -sendQueueSize 32 " 
            f"{RELIABILITIES[reliability]} -noPrint -pidMultiPubTest {multiPub} "
            "-numSubscribers 1"
        )
    else:
        cmd = (f"{RTI_PERF_TOOL} -pub -dataLen {payload_size} -batchSize 6400 "
            f"-numIter {ITER} -domain {domain} -nic {nic} -sendQueueSize 32 " 
            f"{RELIABILITIES[reliability]} -noPrint ")
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process.stdout

def main():
    domain = 1
    parser = argparse.ArgumentParser(description="Throughput test for DDS.")
    parser.add_argument("nic", help="Producer network interface.")
    parser.add_argument("--multiPub", metavar="ID", help="Execute test whit 2 publishers mode.")
    args = parser.parse_args()

    for mode in Reliability:
        for payload_size in PAYLOAD_SIZES:
            print(f"\n\nProducer sending {payload_size} B / {payload_size / 1024} KB - Domain {domain}\n")
            execute_producer(payload_size, mode.value, domain, args.multiPub, args.nic)
            domain = domain + 1
        break

if __name__ == "__main__":
    main()
