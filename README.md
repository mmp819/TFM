# TFM
Material desarrollado y empleado a lo largo del Trabajo de Fin de Máster: *Evaluación de sistemas de distribución para la automatización de aplicaciones industriales inteligentes*.

------------------------------------------

## Resumen:

La transición de la Industria 4.0 al IoT Continuum refleja un cambio fundamental en los modelos de procesamiento de datos, que pasan de estar centrados en la nube a distribuirse progresivamente hacia el *edge* y los dispositivos, con el objetivo de reducir la latencia, aumentar la resiliencia y habilitar capacidades de decisión en tiempo real a lo largo de toda la arquitectura. Esta continuidad operativa plantea importantes retos en términos de interoperabilidad, latencia y rendimiento.

En este contexto, tecnologías como DDS (Data Distribution Service) y Apache Kafka han demostrado ser eficaces, aunque en escenarios diferentes. DDS destaca por sus capacidades en entornos distribuidos con requisitos estrictos de comunicación en tiempo real, mientras que Kafka es ampliamente utilizado para procesar grandes volúmenes de datos en arquitecturas en la nube. Por lo tanto, la coexistencia de ambas tecnologías en un mismo sistema resulta un desafío.

Este trabajo propone una arquitectura, capaz de integrar DDS y Kafka, combinando sus fortalezas para facilitar la comunicación entre sistemas heterogéneos. A través de un caso de uso basado en datos sensóricos simulados de vehículos inteligentes, se implementa una solución completa que conecta dispositivos embebidos y ubicados en el *edge* con plataformas que pudieran encontrarse en la nube, con un despliegue automatizado. Además, se incorporan mecanismos de monitorización y se analizan métricas de rendimiento, lo que permite evaluar la viabilidad de la propuesta en escenarios industriales.

------------------------------------------
## Memoria:

*Pendiente de publicación*

------------------------------------------

## Estructura del repositorio:
* **Benchmark**: Código utilizado para la ejecución automatizada de tests reducidos de rendimiento para Kafka/DDS. Se encuentra organizado en función de las métricas:
  - Latencia
  - *Throughput*  
A su vez, para cada métrica, se puede estudiar el material ofrecido en función del *middleware* empleado:
  - DDS
  - Kafka  
También incluye las imágenes de las figuras generadas, la colección completa de resultados en JSON y el código empleado en la generación de las figuras.
* **Dataset**: Recoge la sección empleada del *dataset* y el código correspondiente a su procesado y los CSV resultantes para cada vehículo.
* **Deploy_Scripts**: *Scripts* utilizados para la automatización de la instalación de dependencias necesarias, preparación de entornos y ejecución de vehiculos.
* **Grafana**: Recopila los *dashborads* empleados para la visualización de métricas, así como muestras en bruto obtenidas desde Prometheus.
* **Simulation**: Código utilizado para la ejecución del caso de uso simulado, así como la configuración de los servicios de enrutamiento y monitorización. Se divide en los siguientes directorios.
  - Aggregator: Agregación de información de dominios y configuración de enrutamiento entre dominios.
  - Bridge: Configuración de enrutamiento entre DDS y Kafka.
  - DataTypes: Tipos de datos que se utilizan en el caso de uso.
  - Monitoring: *Exporters*, *dashboards* de Grafana y captura de métricas desde *endpoints* por Prometheus.
  - VehicleSimulation: Código encargado de simular la publicación de datos por un vehículo.

------------------------------------------

## Arquitectura y solución software empleada:


![](Arquitectura-SolucionSwPropuesta.png)

------------------------------------------

## Fuentes de datos:
* **Datos DeepSense6G - Scenario 36**: https://www.deepsense6g.net/scenarios36-39

------------------------------------------

## Contacto:
* **Autor**: Mario Martín Pérez (mario.martinperez@unican.es)
