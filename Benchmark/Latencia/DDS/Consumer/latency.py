# Importar dependencias
import subprocess
import enum
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

# Ruta hacia el ejecutable de la herramienta
RTI_PERF_TOOL = ("~/rti_workspace/7.3.0/utilities/perftest/4.1/bin/"
    "x64Linux4gcc7.3.0/release/perftest_cpp"
)

class Reliability(enum.Enum):
    RELIABLE = 0
    BEST_EFFORT = 1

def execute_consumer(reliability, domain):
    # Ejecuta un consumidor DDS.
    # Params:
    #    reliability (Reliability): 0 -> RELIABLE / 1 -> BEST_EFFORT
    #    domain (int): Domain ID.
    
    # Returns:
    #    stdout (str): Output del comando.
    
    cmd = (f"{RTI_PERF_TOOL} -sub {RELIABILITIES[reliability.value]} "
           f"-noPrint -domain {domain} -nic {NIC}"
    )
    process = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
    return process.stdout

def main():
    domain = 1
    for size in PAYLOAD_SIZES:
        print(f"Executing consumer of {size} B / {size / 1024} KB with reliability. - Domain {domain}")
        output = execute_consumer(Reliability.RELIABLE, domain)
        print(output)
        domain = domain + 1
    
    for size in PAYLOAD_SIZES:
        print(f"Executing consumer of {size} B / {size / 1024} KB with best effort. - Domain {domain}")
        output = execute_consumer(Reliability.BEST_EFFORT, domain)
        print(output)
        domain = domain + 1

if __name__ == "__main__":
    main()    
