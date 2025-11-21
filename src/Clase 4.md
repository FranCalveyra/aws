# Clase 4

## Servicios de cómputo

Amazon EC2

![Imagen 2-1](images/clase_4_page2_img1.png)

![Imagen 2-2](images/clase_4_page2_img2.png)

![Imagen 2-3](images/clase_4_page2_img3.png)

### Objetivos

- Identificar cómo usar Amazon Elastic Compute Cloud (Amazon EC2) en una

arquitectura.

- Explicar el valor de usar Amazon Machine Images (AMI) para acelerar la creación y la

repetibilidad de la infraestructura.

- Recomendar tipos de instancias de EC2 según los requerimientos.

- Recomendar soluciones de almacenamiento para Amazon EC2.

- Reconocer cómo configurar instancias de Amazon EC2 con datos de usuario.

- Describir las opciones de precios de EC2 y hacer recomendaciones basadas en el costo.

- Lanzar una instancia de Amazon EC2.

- Utilizar los principios de AWS Well-Architected Framework al diseñar una capa de

cómputo con Amazon EC2.

![Imagen 3-1](images/clase_4_page3_img1.png)

![Imagen 3-2](images/clase_4_page3_img2.png)

![Imagen 3-3](images/clase_4_page3_img3.png)

### Opciones de cómputo en tiempo de ejecución de AWS

Diferentes servicios de cómputo para varios casos de uso

Servidores

Máquinas virtuales Platform as a

Contenedores Virtuales Serverless

(VMs) Service (PaaS)

### Privados(VPS)

Amazon Elastic Amazon Elastic Amazon Lightsail AWS Elastic AWS Lambda

Compute Cloud Container Service Beanstalk

(Amazon EC2) (Amazon ECS)

Amazon Elastic AWS Fargate

Kubernetes Service

(Amazon EKS)

![Imagen 4-1](images/clase_4_page4_img1.png)

![Imagen 4-2](images/clase_4_page4_img2.png)

![Imagen 4-3](images/clase_4_page4_img3.png)

![Imagen 4-4](images/clase_4_page4_img4.png)

![Imagen 4-5](images/clase_4_page4_img5.png)

![Imagen 4-6](images/clase_4_page4_img6.png)

![Imagen 4-7](images/clase_4_page4_img7.png)

![Imagen 4-8](images/clase_4_page4_img8.png)

![Imagen 4-9](images/clase_4_page4_img9.png)

![Imagen 4-10](images/clase_4_page4_img10.png)

### Servicios de cómputo

### Cada categoría de servicio ofrece distintos niveles de control

de infraestructura y velocidad de despliegue de aplicaciones

### VMs Contenedores VPS PaaS Serverless

Mayor control y personalización de la infraestructura

Despliegues de aplicaciones más rápidos

![Imagen 5-1](images/clase_4_page5_img1.png)

![Imagen 5-2](images/clase_4_page5_img2.png)

![Imagen 5-3](images/clase_4_page5_img3.png)

### Amazon EC2

- Proporciona máquinas virtuales

(servidores) en la nube.

- Aprovisiona servidores en minutos.

- Puede aumentar o reducir

automáticamente la capacidad según

sea necesario.

- Permite pagar sólo por la capacidad

que se utiliza.

![Imagen 6-1](images/clase_4_page6_img1.png)

![Imagen 6-2](images/clase_4_page6_img2.png)

![Imagen 6-3](images/clase_4_page6_img3.png)

![Imagen 6-4](images/clase_4_page6_img4.png)

### Amazon EC2

Una instancia EC2 es una VM que corre en un servidor físico

![Imagen 7-1](images/clase_4_page7_img1.png)

![Imagen 7-2](images/clase_4_page7_img2.png)

![Imagen 7-3](images/clase_4_page7_img3.png)

Amazon EC2

Casos de uso

Siempre que se necesite:

- Control completo de sus recursos de cómputo,

incluyendo sistema operative y tipo de

procesador.

- Opciones para optimizar sus costos de

cómputo

- Instancias On-Demand , reservadas y Spot

- Savings Plans

- Capacidad para correr cualquier tipo de

carga de trabajo

- Sitios Web simples

- Aplicaciones empresariales

- Aplicaciones de inteligencia artificial

generativa

![Imagen 8-1](images/clase_4_page8_img1.png)

![Imagen 8-2](images/clase_4_page8_img2.png)

![Imagen 8-3](images/clase_4_page8_img3.png)

Amazon EC2

Pasos para aprovisionar una instancia

![Imagen 9-1](images/clase_4_page9_img1.png)

![Imagen 9-2](images/clase_4_page9_img2.png)

![Imagen 9-3](images/clase_4_page9_img3.png)

Amazon Machine Image (AMI)

Una AMI provee la información necesaria para

lanzar una instancia, incluyendo:

- Un template para el volumen raíz: contiene el

sistema operativo anfitrión y opcionalmente

otro software instalado

- Permisos: Controla quién puede acceder la AMI

- Mapeos a dispositivos de bloque: Especifica los

volúmenes de almacenamiento conectados a

la instancia

![Imagen 10-1](images/clase_4_page10_img1.png)

![Imagen 10-2](images/clase_4_page10_img2.png)

![Imagen 10-3](images/clase_4_page10_img3.png)

![Imagen 10-4](images/clase_4_page10_img4.png)

Amazon Machine Image (AMI)

Beneficios

Repetibilidad Reusabilidad Recuperabilidad

### Una AMI se puede usar en Se puede crear una AMI a

Las instancias lanzadas con la

forma repetida para lanzar partir de una instancia

misma AMI están configuradas

instancias con eficiencia y configurada como un

de forma idéntica.

precisión. backup que se puede

restaurar.

Se puede reemplazar una

instancia que falló lanzando

una nueva desde la misma

## AMI.

![Imagen 11-1](images/clase_4_page11_img1.png)

![Imagen 11-2](images/clase_4_page11_img2.png)

![Imagen 11-3](images/clase_4_page11_img3.png)

![Imagen 11-4](images/clase_4_page11_img4.png)

![Imagen 11-5](images/clase_4_page11_img5.png)

![Imagen 11-6](images/clase_4_page11_img6.png)

Amazon Machine Image (AMI)

Selección

### Criterios AMI source

Región Quick Start: AMIs con Linux y Microsoft Windows

provistas por AWS.

Sistema Operativo

My AMIs: AMIs creadas por el usuario.

Tipo de almacenamiento del dispositivo raíz

AWS Marketplace: templates pre-configurados

Arquitectura

por terceros.

Tipo de virtualización: para mejor desempeño,

Community AMIs: AMIs compartidas por otros.

use AMIs con tipo de virtualización Hardware

Usar bajo su propio riesgo.

Virtual Machine (HVM)

![Imagen 12-1](images/clase_4_page12_img1.png)

![Imagen 12-2](images/clase_4_page12_img2.png)

![Imagen 12-3](images/clase_4_page12_img3.png)

### Instancias store-backed vs Amazon EBS-backed AMI

### Characteristic Amazon EBS-Backed Instance Instance Store-Backed Instance

Boot time for the instance Boots faster Takes longer to boot

Maximum size of root device 16 TiB 10 GiB

Cannot be in a stopped state;

Ability to stop the instance Can stop the instance

instances are running or terminated

### Can’t change the instance type

Ability to change the instance Can change the instance type by

because the instance can’t be

type stopping instance

stopped

You are charged for instance usage,

### You are charged for instance usage

Instance charges EBS volume usage, and storing your

and storing your AMI in Amazon S3

AMI as an EBS snapshot

Use case Persistent storage Temporary storage

![Imagen 13-1](images/clase_4_page13_img1.png)

![Imagen 13-2](images/clase_4_page13_img2.png)

![Imagen 13-3](images/clase_4_page13_img3.png)

Amazon EC2

Ciclo de vida de una instancia

![Imagen 14-1](images/clase_4_page14_img1.png)

![Imagen 14-2](images/clase_4_page14_img2.png)

![Imagen 14-3](images/clase_4_page14_img3.png)

![Imagen 14-4](images/clase_4_page14_img4.png)

Creación de una AMI

![Imagen 15-1](images/clase_4_page15_img1.png)

![Imagen 15-2](images/clase_4_page15_img2.png)

![Imagen 15-3](images/clase_4_page15_img3.png)

![Imagen 15-4](images/clase_4_page15_img4.png)

### EC2 Image Builder

EC2 Image Builder automatiza la creación, gestión e implementación

de imágenes de VMs.

- Brinda una interfaz gráfica para crear pipelines de creación de

imágenes

- Crea y mantiene AMIs de Amazon EC2 e imágenes de VM on-prem.

- Produce imágenes seguras, validadas y actualizadas

- Asegura el control de versiones

![Imagen 16-1](images/clase_4_page16_img1.png)

![Imagen 16-2](images/clase_4_page16_img2.png)

![Imagen 16-3](images/clase_4_page16_img3.png)

![Imagen 16-4](images/clase_4_page16_img4.png)

Amazon EC2

### Configuración del tipo de instancia

El tipo de instancia de EC2 define la configuración de CPU, memoria, almacenamiento y

performance de red.

Network

Instance type vCPU Memory Storage

performance

m5d.large 2 4 GiB 1 x 50 NVMe SSD Up to 10 Gbps

m5d.xlarge 4 8 GiB 1 x 100 NVMe SSD Up to 10 Gbps

m5d.8xlarge 32 128 GiB 2 x 600 NVMe SSD 10 Gbps

![Imagen 17-1](images/clase_4_page17_img1.png)

![Imagen 17-2](images/clase_4_page17_img2.png)

![Imagen 17-3](images/clase_4_page17_img3.png)

Amazon EC2

Nombres de los tipos de instancias

### Componentes de los nombres

- Familia

- Generación

- Familia de procesador

- Capacidades adicionales

- Tamaño

![Imagen 18-1](images/clase_4_page18_img1.png)

![Imagen 18-2](images/clase_4_page18_img2.png)

![Imagen 18-3](images/clase_4_page18_img3.png)

![Imagen 18-4](images/clase_4_page18_img4.png)

Amazon EC2

### Tipos de instancias según carga de trabajo

### Tipo Ejemplos de cargas Ejemplos de tipos de instancia

Instancias de propósito Servidores de aplicación o Web M7, Mac, M6, M5, M4, T4, T3, T2

general Aplicaciones empresariales

Servidores para juegos

### Ambientes para desarrollo o prueba

Instancias optimizadas Procesamiento por lotes C7, C6, C5, C4

para cómputo Aplicaciones analíticas distribuidas

### High performance computing (HPC)

Instancias optimizadas Bases de datos de alto rendimiento I4, Im4, Is4, I3, D2, D3, H1

para almacenamiento Analítica en tiempo real

### Cargas transaccionales

Memory optimized In-memory caches R7, R6, R5, R4, X2, X1, Z1

instance types Bases de datos de alto rendimiento

### Aplicaciones analíticas “Big Data”

Instancias con Machine learning, inteligencia artificial (IA) P5, P4, P3, P2, DL1, Trn1, Inf2, Inf1, G5, G4,

aceleración de cómputo HPC G3, F1, VT1

### Instancias optimizadas Cargas de aprendizaje profundo Hpc7, Hpc6

para High performance Cargas de HPC intensivas en cómputo

computing (HPC)

![Imagen 19-1](images/clase_4_page19_img1.png)

![Imagen 19-2](images/clase_4_page19_img2.png)

![Imagen 19-3](images/clase_4_page19_img3.png)

Amazon EC2

### Selección de la instancia más adecuada

### Con 270 tipos de instancia disponibles, ¿cómo seleccionar el adecuado?

- Considere los requerimientos tanto de desempeño como de costo.

- Use los recursos disponibles para obtener recomendaciones.

### Tarea Solución

En la consola de EC2, use la página de Tipos de Instancia para filtrar según

Creación de

las características seleccionadas.

una nueva

Recomendación: La última generación de cada familia generalmente

instancia

tiene la mejor relación costo/rendimiento.

Optimización Puede obtener recomendaciones para optimizar el tipo de instancia

de una mediante AWS Compute Optimizer.

instancia Puede evaluar recomendaciones y modificar la instancia de acuerdo a

existente ellas.

![Imagen 20-1](images/clase_4_page20_img1.png)

![Imagen 20-2](images/clase_4_page20_img2.png)

![Imagen 20-3](images/clase_4_page20_img3.png)

AWS Compute Optimizer

Recomienda el tipo y tamaño

de instancia, y configuración

de grupo de Auto Scaling

óptimos

Analiza patrones de carga de

trabajo y hace

recomendaciones.

Clasifica los hallazgos en las

instancias como

aprovisionamiento insuficiente,

excesivo, optimizado o

Ninguno

![Imagen 21-1](images/clase_4_page21_img1.png)

![Imagen 21-2](images/clase_4_page21_img2.png)

![Imagen 21-3](images/clase_4_page21_img3.png)

![Imagen 21-4](images/clase_4_page21_img4.png)

Actividad

Selección de tipos de instancia

![Imagen 22-1](images/clase_4_page22_img1.png)

![Imagen 22-2](images/clase_4_page22_img2.png)

![Imagen 22-3](images/clase_4_page22_img3.png)

Actividad

### Consigna

Elegir el tipo de instancia EC2 adecuado para cada uno de

los casos de uso de ejemplo.

Usar la información en

https://aws.amazon.com/ec2/instance-types/

![Imagen 23-1](images/clase_4_page23_img1.png)

![Imagen 23-2](images/clase_4_page23_img2.png)

![Imagen 23-3](images/clase_4_page23_img3.png)

![Imagen 23-4](images/clase_4_page23_img4.png)

Actividad

Casos

Familias de instancias

Carga de trabajo

Bases de datos transaccionales

## C M I P

Entornos de desarrollo pequeños

Inf2 R T

Servidores de juegos

In-memory caches

Generación de imágenes y video

Machine learning

Procesamiento batch

![Imagen 24-1](images/clase_4_page24_img1.png)

![Imagen 24-2](images/clase_4_page24_img2.png)

![Imagen 24-3](images/clase_4_page24_img3.png)

Actividad

Respuestas

Carga de trabajo Familia de instancias

Bases de datos transaccionales I

Entornos de desarrollo pequeños T

Servidores de juegos M

In-memory caches R

Generación de imágenes y video Inf2

Machine learning P

Procesamiento batch C

![Imagen 25-1](images/clase_4_page25_img1.png)

![Imagen 25-2](images/clase_4_page25_img2.png)

![Imagen 25-3](images/clase_4_page25_img3.png)

### Puntos clave

Un tipo de instancia EC2 define una configuración de

características de rendimiento de CPU, memoria,

almacenamiento y red.

### Como recomendación, elija tipos de instancias de

nueva generación en una familia porque generalmente

tienen mejores relaciones precio-rendimiento.

Utilice la página Tipos de instancia en la consola de

### Amazon EC2 y AWS Compute Optimizer para encontrar

el tipo de instancia adecuado para su carga de trabajo.

![Imagen 26-1](images/clase_4_page26_img1.png)

![Imagen 26-2](images/clase_4_page26_img2.png)

![Imagen 26-3](images/clase_4_page26_img3.png)

![Imagen 26-4](images/clase_4_page26_img4.png)

### Almacenamiento en instancias EC2

### Recurso de Volumen raíz Volúmenes de Volúmenes de datos que Volúmenes de datos

almacenamiento de datos para una sola se pueden acceder que se pueden acceder

EC2 instancia desde varias instancias desde varias instancias

de Linux de Windows

Amazon EBS

Sí Sí No No

(Sólo SSD)

Instance store

Sí Sí No No

Amazon Elastic File

System (Amazon EFS) No No Sí No

[Linux]

Amazon FSx for

No No No Sí

### Windows File Server

Una instancia EC2 siempre va a tener un volumen raíz, y opcionalmente uno o más volúmenes de

datos.

![Imagen 27-1](images/clase_4_page27_img1.png)

![Imagen 27-2](images/clase_4_page27_img2.png)

![Imagen 27-3](images/clase_4_page27_img3.png)

### Instance stores

### Un instance store proporciona almacenamiento no persistente a una instancia. El

volumen de datos se almacena en el mismo servidor físico donde se ejecuta la

instancia.

Características

Almacenamiento temporario orientado a bloque

### Usa HDD o SSD

Los datos del instance store se pierden cuando la

instancia es detenida o terminada.

Ejemplos de caso de uso

Buffers

Cache

Datos temporarios

![Imagen 28-1](images/clase_4_page28_img1.png)

![Imagen 28-2](images/clase_4_page28_img2.png)

![Imagen 28-3](images/clase_4_page28_img3.png)

![Imagen 28-4](images/clase_4_page28_img4.png)

### Amazon EBS

Los volúmenes Amazon EBS proveen almacenamiento persistente conectado por

red a instancias EC2.

Características

Almacenamiento persistente en bloques

Puede conectarse a cualquier instancia en la

misma Zona de Disponibilidad

Usa HDD o SSD

Puede estar cifrado

### Soporta snapshots que son persistidos en S3

Los datos persisten independientemente de la

vida de la instancia.

Ejemplos de caso de uso

Bases de datos stand-alone

Almacenamiento de datos de aplicación

![Imagen 29-1](images/clase_4_page29_img1.png)

![Imagen 29-2](images/clase_4_page29_img2.png)

![Imagen 29-3](images/clase_4_page29_img3.png)

Amazon EBS

### Volúmenes respaldados por HDD

### Los volúmenes respaldados por HDD de Amazon EBS funcionan

bien cuando el foco está en el rendimiento (throughput).

### Tipo de volumen Descripción Casos de uso

- Tipo de volumen de bajo • Cargas de streaming

### Throughput Optimized costo • Big data

HDD (st1) • Diseñado para cargas de • Data warehouses

trabajo de alto • Procesamiento de logs

rendimiento y acceso • No puede ser un volumen de boot

frecuente

- Volumen HDD de menor • Almacenamiento orientado al

### Cold HDD (sc1) costo throughput para grandes volúmenes

- Diseñado para cargas de de datos de acceso poco frecuente

trabajo con acceso • Casos de uso donde el menor costo

menos frecuente de almacenamiento es importante

- No puede ser un volumen de boot

![Imagen 30-1](images/clase_4_page30_img1.png)

![Imagen 30-2](images/clase_4_page30_img2.png)

### Instancias optimizadas para EBS

Algunos tipos de instancia EC2 pueden ser EBS-optimized

### Beneficios

Proporciona una conexión de red dedicada a

los volúmenes EBS conectados.

Aumenta el rendimiento de E/S.

Se consigue un rendimiento adicional si se

utiliza una instancia basada en el sistema

Amazon EC2 Nitro.

Uso

Para los tipos de instancias EBS-optimized, la

optimización está habilitada de forma

predeterminada

Para otros tipos de instancias compatibles, la

optimización debe habilitarse manualmente

![Imagen 31-1](images/clase_4_page31_img1.png)

![Imagen 31-2](images/clase_4_page31_img2.png)

![Imagen 31-3](images/clase_4_page31_img3.png)

Instancias EC2

### Sistemas de archivos compartidos

### ¿Qué sucede si tenemos varias instancias que deben usar el mismo almacenamiento?

No es una opción No es la opción ideal Mejor opción

Amazon EBS Amazon S3 Amazon EFS Amazon FSx for

Windows File

(Linux)

### Server (Windows)

### Se conecta solo a una Amazon S3: Es una opción, Amazon EFS and Amazon FSx

instancia pero no es ideal for Windows File Server: ambos

satisfacen el requerimiento

![Imagen 32-1](images/clase_4_page32_img1.png)

![Imagen 32-2](images/clase_4_page32_img2.png)

![Imagen 32-3](images/clase_4_page32_img3.png)

![Imagen 32-4](images/clase_4_page32_img4.png)

![Imagen 32-5](images/clase_4_page32_img5.png)

![Imagen 32-6](images/clase_4_page32_img6.png)

![Imagen 32-7](images/clase_4_page32_img7.png)

![Imagen 32-8](images/clase_4_page32_img8.png)

![Imagen 32-9](images/clase_4_page32_img9.png)

![Imagen 32-10](images/clase_4_page32_img10.png)

Amazon Elastic File System

### Amazon EFS

Proporciona almacenamiento de sistema de archivos para cargas de

trabajo basadas en Linux.

Sistema de archivos elástico totalmente gestionado.

Se escala automáticamente a medida que se añaden o eliminan archivos.

Petabytes de capacidad.

Soporta los protocolos de Network File Systems (NFS).

Monta el sistema de archivos en la instancia EC2.

Compatible con todas las AMI basadas en Linux para Amazon EC2.

![Imagen 33-1](images/clase_4_page33_img1.png)

![Imagen 33-2](images/clase_4_page33_img2.png)

![Imagen 33-3](images/clase_4_page33_img3.png)

![Imagen 33-4](images/clase_4_page33_img4.png)

Amazon EFS

Casos de uso

Algunos ejemplos de aplicaciones y cargas de

trabajo comunes para Amazon EFS incluyen:

- Home directories

- Sistema de archivos para aplicaciones

empresariales

- Pruebas y desarrollo de aplicaciones

- Copias de seguridad de bases de datos

- Servidores web y gestión de contenido

- Flujos de trabajo multimedia

Ejemplo de comando para montar el file • Análiticos de big data

system en cada uno de las instancias

$ sudo mount -t nfs4 mount-target-DNS:/ ~/efs-

mount-point

![Imagen 34-1](images/clase_4_page34_img1.png)

![Imagen 34-2](images/clase_4_page34_img2.png)

![Imagen 34-3](images/clase_4_page34_img3.png)

![Imagen 34-4](images/clase_4_page34_img4.png)

Amazon EFS

Standard class storage

![Imagen 35-1](images/clase_4_page35_img1.png)

![Imagen 35-2](images/clase_4_page35_img2.png)

![Imagen 35-3](images/clase_4_page35_img3.png)

![Imagen 35-4](images/clase_4_page35_img4.png)

Amazon EFS

One-zone class storage

![Imagen 36-1](images/clase_4_page36_img1.png)

![Imagen 36-2](images/clase_4_page36_img2.png)

![Imagen 36-3](images/clase_4_page36_img3.png)

![Imagen 36-4](images/clase_4_page36_img4.png)

Amazon FSx

### For Windows file server

### Proporciona almacenamiento de sistema de archivos compartido

totalmente administrado para instancias EC2 de Microsoft

Windows.

Compatibilidad nativa con Microsoft Windows.

### Sistema de archivos NTFS

Utiliza el protocolo nativo Server Message Block (SMB) versión 2.0 a

3.1.1.

Espacios de nombres y replicación DFS de Distributed File System

## (DFS).

Se integra con Microsoft Active Directory y admite listas de control

de acceso (ACL) de Windows.

Respaldado por almacenamiento SSD de alto rendimiento.

![Imagen 37-1](images/clase_4_page37_img1.png)

![Imagen 37-2](images/clase_4_page37_img2.png)

![Imagen 37-3](images/clase_4_page37_img3.png)

![Imagen 37-4](images/clase_4_page37_img4.png)

Amazon FSx

Casos de uso

### Home directories

Cargas de trabajo de lift-and-shift de aplicaciones

Workflows de medios y entretenimiento

Análisis de datos (Data analytics)

Servicios web y gestión de contenido

Entornos de desarrollo de software

![Imagen 38-1](images/clase_4_page38_img1.png)

![Imagen 38-2](images/clase_4_page38_img2.png)

![Imagen 38-3](images/clase_4_page38_img3.png)

![Imagen 38-4](images/clase_4_page38_img4.png)

Almacenamiento para instancias EC2

### Resumen

### Las opciones de almacenamiento para instancias EC2 incluyen el instance

store, Amazon EBS, Amazon EFS y Amazon FSx para Windows File Server.

Para un volumen raíz, utilice Amazon EBS con respaldo SSD.

Para un volumen de datos que solo atienda una instancia, utilice el instance

store o el almacenamiento de Amazon EBS.

Para un volumen de datos que atienda varias instancias de Linux, utilice

Amazon EFS.

### Para un volumen de datos que atienda varias instancias de Microsoft

Windows, utilice Amazon FSx para Windows File Server.

![Imagen 39-1](images/clase_4_page39_img1.png)

![Imagen 39-2](images/clase_4_page39_img2.png)

![Imagen 39-3](images/clase_4_page39_img3.png)

Configuración de EC2

Otras consideraciones

![Imagen 40-1](images/clase_4_page40_img1.png)

![Imagen 40-2](images/clase_4_page40_img2.png)

![Imagen 40-3](images/clase_4_page40_img3.png)

### EC2 instance user data

### Cuando se inicia una instancia EC2, se puede especificar datos de

usuario para ejecutar un script de inicialización (shell script o

directiva cloud-init).

User data

#!/bin/bash

yum update –y

service httpd start

Su AMI

chkconfig httpd on Instancia EC2 en

ejecución

![Imagen 41-1](images/clase_4_page41_img1.png)

![Imagen 41-2](images/clase_4_page41_img2.png)

![Imagen 41-3](images/clase_4_page41_img3.png)

![Imagen 41-4](images/clase_4_page41_img4.png)

![Imagen 41-5](images/clase_4_page41_img5.png)

### Recuperación de metadatos de la instancia

Los metadatos de una instancia son información sobre ella.

Se puede acceder a ellos desde su instancia en esta URL:

http://169.254.169.254/latest/meta-data/

Se pueden recuperar desde un script de datos de usuario.

#!/bin/bash

yum update –y

hostname = $(curl -s http://169.254.169.254/latest/meta-data/public-hostname)

User data

Su AMI Instancia

EC2 en

Metadato Valor

ejecución

instance-id i-1234567890abcdef0

mac 00-1B-63-84-45-E6

public-hostname ec2-203-0-113-25.compute-1.amazonaws.com

public-ipv4 67.202.51.223

local-ipv4 10.251.50.12

![Imagen 42-1](images/clase_4_page42_img1.png)

![Imagen 42-2](images/clase_4_page42_img2.png)

![Imagen 42-3](images/clase_4_page42_img3.png)

![Imagen 42-4](images/clase_4_page42_img4.png)

![Imagen 42-5](images/clase_4_page42_img5.png)

Datos de usuario en instancias en ejecución

![Imagen 43-1](images/clase_4_page43_img1.png)

![Imagen 43-2](images/clase_4_page43_img2.png)

![Imagen 43-3](images/clase_4_page43_img3.png)

![Imagen 43-4](images/clase_4_page43_img4.png)

Ejecución manual de comandos

Buenas prácticas

Manually run additional

commands to configure

Best

instance

practice Instance

User data is updated New

Original

Copy user data initialization is

user data

user data

correct

Web server A Web server A New web server

Manually run additional

Not best

commands to configure

practice

instance

Instance

Original User data is not updated Original user

Copy user data initialization is

data

user data

not correct

Web server B Web server B New web server

![Imagen 44-1](images/clase_4_page44_img1.png)

![Imagen 44-2](images/clase_4_page44_img2.png)

Modelos de implementación de AMI

### AMI básica Silver AMI Golden AMI

AMI base AWS Managed Services (AMS) Customized immutable AMIs

provided mutable AMIs

AMI configuradas solo con SO Configurations fully baked into the

Configurations half baked into the AMI

Totalmente configurables y

## AMI

actualizables All instances using the same

Some configurations need to be golden AMI behave the same

Tiempo de generación más corto

done manually or by user data

Shorter boot times but increases

scripts

Arranque más lento

build times

Provides a balance between boot

Shorter lifespan of the AMI

speed and build time

![Imagen 45-1](images/clase_4_page45_img1.png)

![Imagen 45-2](images/clase_4_page45_img2.png)

![Imagen 45-3](images/clase_4_page45_img3.png)

![Imagen 45-4](images/clase_4_page45_img4.png)

![Imagen 45-5](images/clase_4_page45_img5.png)

![Imagen 45-6](images/clase_4_page45_img6.png)

![Imagen 45-7](images/clase_4_page45_img7.png)

![Imagen 45-8](images/clase_4_page45_img8.png)

![Imagen 45-9](images/clase_4_page45_img9.png)

![Imagen 45-10](images/clase_4_page45_img10.png)

![Imagen 45-11](images/clase_4_page45_img11.png)

![Imagen 45-12](images/clase_4_page45_img12.png)

![Imagen 45-13](images/clase_4_page45_img13.png)

![Imagen 45-14](images/clase_4_page45_img14.png)

### Modelos de implementación de AMI

Los Placement groups brindan control sobre dónde se ejecuta un grupo de instancias

interdependientes en una zona de disponibilidad.

### Beneficios Limitaciones Estrategias

Aumenta el rendimiento de Una instancia solo se Cluster

la red entre instancias. puede lanzar en un

Partition

placement group a la vez

Reduce los fallos

Spread

correlacionados o Las instancias con un

simultáneos. tenancy de host no se

pueden lanzar en un

placement group

![Imagen 46-1](images/clase_4_page46_img1.png)

![Imagen 46-2](images/clase_4_page46_img2.png)

![Imagen 46-3](images/clase_4_page46_img3.png)

![Imagen 46-4](images/clase_4_page46_img4.png)

![Imagen 46-5](images/clase_4_page46_img5.png)

![Imagen 46-6](images/clase_4_page46_img6.png)

## EC2

Opciones de precios

![Imagen 47-1](images/clase_4_page47_img1.png)

![Imagen 47-2](images/clase_4_page47_img2.png)

![Imagen 47-3](images/clase_4_page47_img3.png)

AWS Free Tier: Amazon EC2

12 meses gratis

750 horas por mes de instancias t4g.small dependiendo de la

región

750 horas por mes de instancias Linux, RHEL, o SLES t2.micro o

t3.micro dependiendo de la región

750 horas por mes de instancias Windows t2.micro o t3.micro

dependiendo de la región

![Imagen 48-1](images/clase_4_page48_img1.png)

![Imagen 48-2](images/clase_4_page48_img2.png)

![Imagen 48-3](images/clase_4_page48_img3.png)

![Imagen 48-4](images/clase_4_page48_img4.png)

Amazon EC2

### Modelos de precios

Amazon EC2 ofrece las siguientes estrategias de compra para ayudar a optimizar sus

costos según sus necesidades:

Modelos de compra Modelos de Capacidad Modelos Dedicados

reservada

### El énfasis está en El énfasis está en El énfasis está en

proporcionar grandes proporcionar instancias proporcionar hardware

ahorros a través de reservadas para garantizar dedicado que ayude a

diferentes casos de uso. que estén disponibles cumplir con requisitos de

cuando se necesiten. cumplimiento y

regulatorios.

![Imagen 49-1](images/clase_4_page49_img1.png)

![Imagen 49-2](images/clase_4_page49_img2.png)

![Imagen 49-3](images/clase_4_page49_img3.png)

![Imagen 49-4](images/clase_4_page49_img4.png)

![Imagen 49-5](images/clase_4_page49_img5.png)

Amazon EC2

Modelos de compra

### On-Demand Reservadas Savings Plans Amazon EC2 Spot

### Se paga la capacidad de Se compromete uso por 1 Mismos descuentos que Capacidad de Amazon

cómputo por segundo o o 3 años a cambio de un para instancias reservadas. EC2 ociosa con ahorros

por hora sin compromisos descuento significativo substanciales sobre los

### Mayor flexibilidad a

a largo plazo. sobre los precios on- precios On-Demand.

cambio de un compromiso

demand.

Recomendado para: de $/hora Recomendado para:

Recomendado para:

- Cargas de trabajo con Recomendado para: • Cargas tolerantes a

picos • Cargas de trabajo fallas

- Todas las cargas de

comprometidas

- Cargas de trabajo de trabajo de Amazon EC2 • Cargas flexibles

experimentación • Cargas de trabajo

- Cargas de trabajo de • Cargas sin estado

estables

Amazon EC2 que

requieran flexibilidad en

el uso comprometido

![Imagen 50-1](images/clase_4_page50_img1.png)

![Imagen 50-2](images/clase_4_page50_img2.png)

Amazon EC2

### Reservas de capacidad

Las reservas de capacidad le permiten reservar capacidad de cómputo para instancias de Amazon

EC2 en una zona de disponibilidad específica.

### On-Demand Capacity Reservations Amazon EC2 Capacity Blocks for ML

### Esto garantiza que siempre tendrá acceso a la Se reservan instancias de GPU para una fecha

capacidad de EC2 cuando la necesite, futura para ejecutar cargas de trabajo de

durante el tiempo que la necesite. aprendizaje automático (ML).

Casos de uso recomendados: Casos de uso recomendados:

- Cargas de trabajo que deben cumplir con • Entrenamiento y ajuste de modelos de ML

los requisitos normativos de alta • Ejecución de experimentos y creación de

disponibilidad prototipos

- Cargas de trabajo que requieren garantía • Planificación para futuros aumentos

de capacidad repentinos de la demanda de aplicaciones

de ML

![Imagen 51-1](images/clase_4_page51_img1.png)

![Imagen 51-2](images/clase_4_page51_img2.png)

Amazon EC2

### Opciones dedicadas

### Las opciones dedicadas de Amazon EC2 brindan capacidad de instancia EC2

en servidores físicos dedicados para su uso (hardware single-tenant).

Instancias dedicadas Hosts dedicados

Facturación por host

Facturación por instancia

Visibilidad de sockets, núcleos e ID de host

Ubicación automática de instancias

Afinidad entre un host y una instancia

Aísla los hosts donde se ejecutan sus instancias

Ubicación de instancias específica

Aumento de capacidad mediante una

solicitud de asignación

Permite usar las licencias de software

vinculadas al servidor y cumplir con requisitos

de cumplimiento

![Imagen 52-1](images/clase_4_page52_img1.png)

![Imagen 52-2](images/clase_4_page52_img2.png)

Amazon EC2

### Guía de optimización de costos

Para optimizar el costo de las instancias de Amazon EC2, debemos

combinar las opciones de compra disponibles.

Escale usando Spot Instances para cargas

que pueden tolerar fallas, flexibles o

stateless.

Use instancias On-Demand for cargas

Cantidad

nuevas o stateful con picos

de

instancias

Use Reserved Instances o Savings Plans

para cargas conocidas y estables

tiempo

![Imagen 53-1](images/clase_4_page53_img1.png)

![Imagen 53-2](images/clase_4_page53_img2.png)

![Imagen 53-3](images/clase_4_page53_img3.png)

Well-Architected Framework

Aplicación en soluciones de cómputo

![Imagen 54-1](images/clase_4_page54_img1.png)

![Imagen 54-2](images/clase_4_page54_img2.png)

![Imagen 54-3](images/clase_4_page54_img3.png)

Well-Architected Framework

Pilares

![Imagen 55-1](images/clase_4_page55_img1.png)

![Imagen 55-2](images/clase_4_page55_img2.png)

![Imagen 55-3](images/clase_4_page55_img3.png)

![Imagen 55-4](images/clase_4_page55_img4.png)

![Imagen 55-5](images/clase_4_page55_img5.png)

![Imagen 55-6](images/clase_4_page55_img6.png)

### Well-Architected Framework

Protección de la infraestructura – Protección del cómputo

Automatice la protección de los recursos

de cómputo.

![Imagen 56-1](images/clase_4_page56_img1.png)

![Imagen 56-2](images/clase_4_page56_img2.png)

![Imagen 56-3](images/clase_4_page56_img3.png)

### Well-Architected Framework

Protección de la infraestructura – Protección de redes

Controle el tráfico en todas las capas.

![Imagen 57-1](images/clase_4_page57_img1.png)

![Imagen 57-2](images/clase_4_page57_img2.png)

![Imagen 57-3](images/clase_4_page57_img3.png)

Well-Architected Framework

Performance

Escale las mejores opciones de cómputo para su

carga de trabajo.

Performance

efficency

Configure y dimensione adecuadamente los

recursos de cómputo.

![Imagen 58-1](images/clase_4_page58_img1.png)

![Imagen 58-2](images/clase_4_page58_img2.png)

Well-Architected Framework

Optimización de costos

Seleccione recursos del tipo, tamaño y

cantidad correctos.

Seleccione el mejor modelo de precios.

![Imagen 59-1](images/clase_4_page59_img1.png)

![Imagen 59-2](images/clase_4_page59_img2.png)

![Imagen 59-3](images/clase_4_page59_img3.png)

Well-Architected Framework

Hardware y servicios

Utilizar la mínima cantidad de hardware

para satisfacer sus necesidades.

Usar tipos de instancia con el menor

impacto.

Sustainability

Usar servicios gerenciados.

![Imagen 60-1](images/clase_4_page60_img1.png)

![Imagen 60-2](images/clase_4_page60_img2.png)

Muchas gracias.

www.austral.edu.ar

![Imagen 61-1](images/clase_4_page61_img1.png)

![Imagen 61-2](images/clase_4_page61_img2.png)

![Imagen 61-3](images/clase_4_page61_img3.png)
