# Clase 6

## Servicios de red

![Imagen 2-1](images/clase_6_page2_img1.png)

![Imagen 2-2](images/clase_6_page2_img2.png)

![Imagen 2-3](images/clase_6_page2_img3.png)

### Objetivos

- Explicar el rol de una red privada virtual (VPC) en AWS

- Identificar los componentes de una VPC que se conectan a

internet.

- Aislar y proteger recursos dentro del entorno de red

- Crear y monitorear una VPC con subredes, un internet Gateway,

tablas de ruteo y un grupo de seguridad

- Aplicar los principios del AWS Well-Architected Framework para

planificar y crear un entorno de red

![Imagen 3-1](images/clase_6_page3_img1.png)

![Imagen 3-2](images/clase_6_page3_img2.png)

![Imagen 3-3](images/clase_6_page3_img3.png)

Infraestructura física de AWS

### Componentes y jerarquía

### Los data centers de AWS tienen miles de servidores organizados en racks. Cada

rack tiene routers de red y switches que direccionan el tráfico.

Los data centers se agrupan en AWS Cloud

Availability Zones (AZs).

### Region A Region B

### Las AZs se conectan en redes que

tienen una latencia <10 Availability Zone A1 Availability Zone B1

milisegundos.

Las AZs están agrupadas en Availability Zone A2 Availability Zone B2

regiones.

La latencia entre una región y otra Availability Zone A3 Availability Zone B3

es de decenas de milisegundos

![Imagen 4-1](images/clase_6_page4_img1.png)

![Imagen 4-2](images/clase_6_page4_img2.png)

![Imagen 4-3](images/clase_6_page4_img3.png)

![Imagen 4-4](images/clase_6_page4_img4.png)

![Imagen 4-5](images/clase_6_page4_img5.png)

![Imagen 4-6](images/clase_6_page4_img6.png)

Aislar recursos en una cuenta AWS

AWS Cloud

AWS account

### Region

Availability Zone 1 Availability Zone 2 Availability Zone 3

Default Amazon VPC

EC2 instance 1 EC2 instance 2 EC2 instance 3

![Imagen 5-1](images/clase_6_page5_img1.png)

![Imagen 5-2](images/clase_6_page5_img2.png)

![Imagen 5-3](images/clase_6_page5_img3.png)

![Imagen 5-4](images/clase_6_page5_img4.png)

![Imagen 5-5](images/clase_6_page5_img5.png)

![Imagen 5-6](images/clase_6_page5_img6.png)

![Imagen 5-7](images/clase_6_page5_img7.png)

![Imagen 5-8](images/clase_6_page5_img8.png)

![Imagen 5-9](images/clase_6_page5_img9.png)

![Imagen 5-10](images/clase_6_page5_img10.png)

### Amazon Virtual Private Cloud

Es una red virtual definida por código, aislada

lógicamente, similar a una red de un data center

tradicional.

### Pertenece a una región

Se puede personalizar para controlar el tráfico entrante y

saliente.

### Se dimensiona mediante un rango de direcciones IP

privadas: bloque CIDR (Classless Inter-Domain Routing

Amazon VPC

block)

![Imagen 6-1](images/clase_6_page6_img1.png)

![Imagen 6-2](images/clase_6_page6_img2.png)

![Imagen 6-3](images/clase_6_page6_img3.png)

![Imagen 6-4](images/clase_6_page6_img4.png)

Tabla de rutas principal

Amazon VPC 10.0.0.0/16

Availability Zone

Main VPC route table

Destination Target

Subnet_A 10.0.0.0/20

10.0.0.0/16 local

EC2 instance A

Private IP address: 10.0.0.5

Main VPC

route table

Subnet_B 10.0.128.0/20

EC2 instance B

Private IP address: 10.0.134.60

![Imagen 7-1](images/clase_6_page7_img1.png)

![Imagen 7-2](images/clase_6_page7_img2.png)

![Imagen 7-3](images/clase_6_page7_img3.png)

![Imagen 7-4](images/clase_6_page7_img4.png)

![Imagen 7-5](images/clase_6_page7_img5.png)

![Imagen 7-6](images/clase_6_page7_img6.png)

![Imagen 7-7](images/clase_6_page7_img7.png)

![Imagen 7-8](images/clase_6_page7_img8.png)

Subredes públicas

Amazon VPC 10.0.0.0/16

Availability Zone

Una subred pública con un

internet gateway asociado

Public subnet 10.0.0.0/20

permite acceso directo a

internet.

Cada instancia de una subred

EC2 instance Public subnet Internet

pública necesita una IP pública

Private IP address: 10.0.0.5 route table gateway

y una privada para accede a

Public IP address: 198.51.102.7

internet.

Public subnet route table

Main VPC route table

Destination Target

Destination Target

10.0.0.0/16 local

10.0.0.0/16 local

0.0.0.0/0 Internet gateway ID

![Imagen 8-1](images/clase_6_page8_img1.png)

![Imagen 8-2](images/clase_6_page8_img2.png)

![Imagen 8-3](images/clase_6_page8_img3.png)

![Imagen 8-4](images/clase_6_page8_img4.png)

![Imagen 8-5](images/clase_6_page8_img5.png)

![Imagen 8-6](images/clase_6_page8_img6.png)

![Imagen 8-7](images/clase_6_page8_img7.png)

![Imagen 8-8](images/clase_6_page8_img8.png)

![Imagen 8-9](images/clase_6_page8_img9.png)

Direcciones IP elásticas

Amazon VPC 10.0.0.0/16

Availability Zone 1

Public subnet 10.0.0.0/20

Public subnet Internet

EC2 instance Public Elastic

route table gateway

Private IP address: IP address:

10.0.0.5 198.51.100.2

### Una dirección IP elástica es una dirección pública y estática

asociada a una instancia. Una dirección IP elástica se puede

transferir a una nueva instancia.

![Imagen 9-1](images/clase_6_page9_img1.png)

![Imagen 9-2](images/clase_6_page9_img2.png)

![Imagen 9-3](images/clase_6_page9_img3.png)

![Imagen 9-4](images/clase_6_page9_img4.png)

![Imagen 9-5](images/clase_6_page9_img5.png)

![Imagen 9-6](images/clase_6_page9_img6.png)

![Imagen 9-7](images/clase_6_page9_img7.png)

![Imagen 9-8](images/clase_6_page9_img8.png)

![Imagen 9-9](images/clase_6_page9_img9.png)

![Imagen 9-10](images/clase_6_page9_img10.png)

Subredes privadas

Amazon VPC 10.0.0.0/16

Availability Zone

Private subnet 10.0.128.0/20

Una subred privada no

tiene acceso directo a

Private subnet

internet. EC2 instance

route table

Private IP address: 10.0.128.17

Main VPC route table Private subnet route table

Destination Target Destination Target

10.0.0.0/16 local 10.0.0.0/16 local

![Imagen 10-1](images/clase_6_page10_img1.png)

![Imagen 10-2](images/clase_6_page10_img2.png)

![Imagen 10-3](images/clase_6_page10_img3.png)

![Imagen 10-4](images/clase_6_page10_img4.png)

![Imagen 10-5](images/clase_6_page10_img5.png)

![Imagen 10-6](images/clase_6_page10_img6.png)

![Imagen 10-7](images/clase_6_page10_img7.png)

![Imagen 10-8](images/clase_6_page10_img8.png)

NAT IP mapping

Solicitud Respuesta

1 2

IP de origen 10.0.0.17 IP de origen 89.89.0.100

Solicitud Respuesta

4 3

### IP de destino 10.0.0.17 IP de destino 89.89.0.100

### Servidor de origen Dispositivo NAT Servidor de destino

Private IP: 10.0.0.17 Public IP: 89.89.0.100 Public IP: 190.50.20.87

![Imagen 11-1](images/clase_6_page11_img1.png)

![Imagen 11-2](images/clase_6_page11_img2.png)

![Imagen 11-3](images/clase_6_page11_img3.png)

![Imagen 11-4](images/clase_6_page11_img4.png)

![Imagen 11-5](images/clase_6_page11_img5.png)

![Imagen 11-6](images/clase_6_page11_img6.png)

![Imagen 11-7](images/clase_6_page11_img7.png)

![Imagen 11-8](images/clase_6_page11_img8.png)

![Imagen 11-9](images/clase_6_page11_img9.png)

![Imagen 11-10](images/clase_6_page11_img10.png)

Conexión de subredes privadas a internet

Amazon VPC 10.0.0.0/16

### Availability Zone

Public subnet 10.0.0.0/20 Private subnet 10.0.128.0/20

NAT gateway EC2 application instance 1

Internet Tabla de rutas Tabla de rutas

gateway de la subred de la subred

pública EC2 NAT device instance privada EC2 application instance 2

Tabla de rutas de la subred pública Tabla de rutas de la subred privada

Destino Objetivo Destino Objetivo

10.0.0.0/16 local 10.0.0.0/16 local

0.0.0.0/0 Internet gateway ID 0.0.0.0/0 NAT gateway ID

![Imagen 12-1](images/clase_6_page12_img1.png)

![Imagen 12-2](images/clase_6_page12_img2.png)

![Imagen 12-3](images/clase_6_page12_img3.png)

![Imagen 12-4](images/clase_6_page12_img4.png)

![Imagen 12-5](images/clase_6_page12_img5.png)

![Imagen 12-6](images/clase_6_page12_img6.png)

![Imagen 12-7](images/clase_6_page12_img7.png)

![Imagen 12-8](images/clase_6_page12_img8.png)

![Imagen 12-9](images/clase_6_page12_img9.png)

![Imagen 12-10](images/clase_6_page12_img10.png)

![Imagen 12-11](images/clase_6_page12_img11.png)

![Imagen 12-12](images/clase_6_page12_img12.png)

![Imagen 12-13](images/clase_6_page12_img13.png)

Actividad

Selección de subredes

![Imagen 13-1](images/clase_6_page13_img1.png)

![Imagen 13-2](images/clase_6_page13_img2.png)

![Imagen 13-3](images/clase_6_page13_img3.png)

Actividad

### Consigna

¿En qué subred se implementa cada uno de estos servicios?

Instancias que ejecutan Un NAT gateway o una

procesos batch instancia NAT

Instancias que ejecutan Instancias de bases de

aplicaciones web datos

![Imagen 14-1](images/clase_6_page14_img1.png)

![Imagen 14-2](images/clase_6_page14_img2.png)

![Imagen 14-3](images/clase_6_page14_img3.png)

![Imagen 14-4](images/clase_6_page14_img4.png)

![Imagen 14-5](images/clase_6_page14_img5.png)

![Imagen 14-6](images/clase_6_page14_img6.png)

![Imagen 14-7](images/clase_6_page14_img7.png)

Actividad

### Consigna

¿En qué subred se implementa cada uno de estos servicios?

### Instancias de bases de datos Subred privada

### Un NAT gateway o una instancia NAT Subred privada

### Instancias que ejecutan aplicaciones web Pública o privada

Instancias que ejecutan procesos batch Subred pública

![Imagen 15-1](images/clase_6_page15_img1.png)

![Imagen 15-2](images/clase_6_page15_img2.png)

![Imagen 15-3](images/clase_6_page15_img3.png)

![Imagen 15-4](images/clase_6_page15_img4.png)

![Imagen 15-5](images/clase_6_page15_img5.png)

![Imagen 15-6](images/clase_6_page15_img6.png)

![Imagen 15-7](images/clase_6_page15_img7.png)

### Resumen

Una VPC es una red virtual, aislada lógicamente, definida por

código.

Una subred pública con un internet Gateway brinda acceso a

internet.

Una subred privada no tiene acceso directo a internet.

Un NAT Gateway permite que los recursos de una subred privada

se conecten a internet.

Las IP elásticas son direcciones estáticas, que se pueden transferir

de una instancia a otra.

![Imagen 16-1](images/clase_6_page16_img1.png)

![Imagen 16-2](images/clase_6_page16_img2.png)

![Imagen 16-3](images/clase_6_page16_img3.png)

Recursos de red

Seguridad

![Imagen 17-1](images/clase_6_page17_img1.png)

![Imagen 17-2](images/clase_6_page17_img2.png)

![Imagen 17-3](images/clase_6_page17_img3.png)

Capas de seguridad de defensa

Amazon VPC

Public subnet

Security group

EC2 instance

Security group

Internet

Public subnet route Network

gateway

table ACL

Client

application

### EC2 instance

Protocolo de red Capa de tabla Capa de Capa de Capa de security

segura de rutas Network ACL subred group

![Imagen 18-1](images/clase_6_page18_img1.png)

![Imagen 18-2](images/clase_6_page18_img2.png)

![Imagen 18-3](images/clase_6_page18_img3.png)

![Imagen 18-4](images/clase_6_page18_img4.png)

![Imagen 18-5](images/clase_6_page18_img5.png)

![Imagen 18-6](images/clase_6_page18_img6.png)

![Imagen 18-7](images/clase_6_page18_img7.png)

![Imagen 18-8](images/clase_6_page18_img8.png)

![Imagen 18-9](images/clase_6_page18_img9.png)

![Imagen 18-10](images/clase_6_page18_img10.png)

![Imagen 18-11](images/clase_6_page18_img11.png)

![Imagen 18-12](images/clase_6_page18_img12.png)

![Imagen 18-13](images/clase_6_page18_img13.png)

![Imagen 18-14](images/clase_6_page18_img14.png)

![Imagen 18-15](images/clase_6_page18_img15.png)

![Imagen 18-16](images/clase_6_page18_img16.png)

![Imagen 18-17](images/clase_6_page18_img17.png)

![Imagen 18-18](images/clase_6_page18_img18.png)

![Imagen 18-19](images/clase_6_page18_img19.png)

![Imagen 18-20](images/clase_6_page18_img20.png)

![Imagen 18-21](images/clase_6_page18_img21.png)

![Imagen 18-22](images/clase_6_page18_img22.png)

Security groups y ACLs

### Private subnet

Los security groups

funcionan como la llave

de un departamento:

dejan pasar a quien la

Security group

tenga.

Las ACLs protegen las

EC2 application

Network ACL

subredes como el portero

instance

de un edificio: deja entrar

a quienes viven allí.

![Imagen 19-1](images/clase_6_page19_img1.png)

![Imagen 19-2](images/clase_6_page19_img2.png)

![Imagen 19-3](images/clase_6_page19_img3.png)

![Imagen 19-4](images/clase_6_page19_img4.png)

![Imagen 19-5](images/clase_6_page19_img5.png)

![Imagen 19-6](images/clase_6_page19_img6.png)

![Imagen 19-7](images/clase_6_page19_img7.png)

![Imagen 19-8](images/clase_6_page19_img8.png)

![Imagen 19-9](images/clase_6_page19_img9.png)

![Imagen 19-10](images/clase_6_page19_img10.png)

![Imagen 19-11](images/clase_6_page19_img11.png)

![Imagen 19-12](images/clase_6_page19_img12.png)

![Imagen 19-13](images/clase_6_page19_img13.png)

![Imagen 19-14](images/clase_6_page19_img14.png)

![Imagen 19-15](images/clase_6_page19_img15.png)

Security groups

Son stateful.

Actúan al nivel de una instancia o una interfaz de red.

Se pueden aplicar en múltiples AZ.

Se definen reglas para permitir tráfico, protocolos y rangos de

puertos.

Los recursos que tienen los mismos requisitos de seguridad

deberían asociarse al mismo security group.

![Imagen 20-1](images/clase_6_page20_img1.png)

![Imagen 20-2](images/clase_6_page20_img2.png)

![Imagen 20-3](images/clase_6_page20_img3.png)

Grupos de seguridad

Amazon VPC

Availability Zone 1 Availability Zone 2

Private subnet 1 Private subnet 2

Security group

EC2 application EC2 application

instance 1 instance 2

Inbound security group rule

Source Traffic type Protocol Port range

Load balancer security group ID HTTPS TCP 443

![Imagen 21-1](images/clase_6_page21_img1.png)

![Imagen 21-2](images/clase_6_page21_img2.png)

![Imagen 21-3](images/clase_6_page21_img3.png)

![Imagen 21-4](images/clase_6_page21_img4.png)

![Imagen 21-5](images/clase_6_page21_img5.png)

![Imagen 21-6](images/clase_6_page21_img6.png)

![Imagen 21-7](images/clase_6_page21_img7.png)

![Imagen 21-8](images/clase_6_page21_img8.png)

Network ACLs

### Funcionan como firewalls stateless

Controlan el tráfico entrante y saliente de una o más

subredes

Una subred puede tener una única ACL

### Una ACL se puede aplicar a varias subredes

Las reglas entrantes y salientes pueden permitir o denegar el

tráfico

Deniegan por default el tráfico no incluido en otras reglas

![Imagen 22-1](images/clase_6_page22_img1.png)

![Imagen 22-2](images/clase_6_page22_img2.png)

![Imagen 22-3](images/clase_6_page22_img3.png)

![Imagen 22-4](images/clase_6_page22_img4.png)

Network ACL

Amazon VPC

Availability Zone 1

Private subnet

Route table Network ACL Business application

### EC2 instance

Rule number Source Traffic type Protocol Port range Deny or allow

Inbound ACL rules

100 188.7.55.9/32 HTTPS TCP 443 Allow

* 0.0.0.0/0 All traffic All All Deny

Outbound ACL rules

100 0.0.0.0/0 HTTPS TCP 443 Allow

* 0.0.0.0/0 All traffic All All Deny

![Imagen 23-1](images/clase_6_page23_img1.png)

![Imagen 23-2](images/clase_6_page23_img2.png)

![Imagen 23-3](images/clase_6_page23_img3.png)

![Imagen 23-4](images/clase_6_page23_img4.png)

![Imagen 23-5](images/clase_6_page23_img5.png)

![Imagen 23-6](images/clase_6_page23_img6.png)

![Imagen 23-7](images/clase_6_page23_img7.png)

![Imagen 23-8](images/clase_6_page23_img8.png)

Network ACLs

### Funcionan como firewalls stateless

Controlan el tráfico entrante y saliente de una o más

subredes

Una subred puede tener una única ACL

### Una ACL se puede aplicar a varias subredes

Las reglas entrantes y salientes pueden permitir o denegar el

tráfico

Deniegan por default el tráfico no incluido en otras reglas

![Imagen 24-1](images/clase_6_page24_img1.png)

![Imagen 24-2](images/clase_6_page24_img2.png)

![Imagen 24-3](images/clase_6_page24_img3.png)

![Imagen 24-4](images/clase_6_page24_img4.png)

Network ACL vs Security groups

### Security groups Network ACLs

### Operan a nivel de recursos Opera a nivel de la subred

### El tráfico de Especifica reglas que permiten o

Permiten tráfico Se aplican las

respuesta se deniegan tráfico

reglas de las

permite

### ACL al tráfico de

automáticamen Las reglas son stateful Las reglas son stateless.

respuesta

te.

### Las reglas se evalúan en orden. La

Se evalúan todas las reglas evaluación termina cuando se aplica una

regla

Ningún tráfico entrante está permitido Todo el tráfico entrante está permitido

por default por default

Todo el tráfico saliente está permitido Todo el tráfico saliente está permitido

por default por default

![Imagen 25-1](images/clase_6_page25_img1.png)

![Imagen 25-2](images/clase_6_page25_img2.png)

![Imagen 25-3](images/clase_6_page25_img3.png)

![Imagen 25-4](images/clase_6_page25_img4.png)

![Imagen 25-5](images/clase_6_page25_img5.png)

![Imagen 25-6](images/clase_6_page25_img6.png)

![Imagen 25-7](images/clase_6_page25_img7.png)

### Firewalls de red

Brinda funciones de firewall de red y servicio de IDS/IPS

### Para proteger los recursos de una subred, se puede

dirigir el tráfico externo a través de un AWS Network

Firewall

Amazon VPC 10.0.0.0/16

Availability Zone 1

Firewall subnet Private subnet

10.0.64.0/20 10.0.128.0/20

EC2 application instance

Route AWS Network Route

table 1 Firewall endpoint table 2

![Imagen 26-1](images/clase_6_page26_img1.png)

![Imagen 26-2](images/clase_6_page26_img2.png)

![Imagen 26-3](images/clase_6_page26_img3.png)

![Imagen 26-4](images/clase_6_page26_img4.png)

![Imagen 26-5](images/clase_6_page26_img5.png)

![Imagen 26-6](images/clase_6_page26_img6.png)

![Imagen 26-7](images/clase_6_page26_img7.png)

![Imagen 26-8](images/clase_6_page26_img8.png)

![Imagen 26-9](images/clase_6_page26_img9.png)

![Imagen 26-10](images/clase_6_page26_img10.png)

![Imagen 26-11](images/clase_6_page26_img11.png)

Administración de recursos

### Bastion hosts

### Security Group A inbound rule Security Group B inbound rule

### Source Type Protocol Port range Destination Traffic type Protocol Port range

IP address range SSH TCP 22 Security group A SSH TCP 22

Amazon VPC 10.0.0.0/16

Availability Zone

Private subnet 10.0.128.0/20

Public subnet 10.0.0.0/20

### Security group A Security group B

### Internet EC2 bastion host instance EC2 application instance

gateway Public IP: 101.188.96.134 Private IP: 10.0.128.44

Private IP: 10.0.15.80

![Imagen 27-1](images/clase_6_page27_img1.png)

![Imagen 27-2](images/clase_6_page27_img2.png)

![Imagen 27-3](images/clase_6_page27_img3.png)

![Imagen 27-4](images/clase_6_page27_img4.png)

![Imagen 27-5](images/clase_6_page27_img5.png)

![Imagen 27-6](images/clase_6_page27_img6.png)

![Imagen 27-7](images/clase_6_page27_img7.png)

![Imagen 27-8](images/clase_6_page27_img8.png)

![Imagen 27-9](images/clase_6_page27_img9.png)

### Resumen

- Infraestructura segura de AWS con múltiples capas de defensa.

- Un grupo de seguridad en una VPC especifica el tráfico permitido

hacia o desde los recursos de AWS. Es un grupo stateful.

- Una ACL de red permite o deniega tráfico entrante o saliente

específico a nivel de subred. No tiene estado.

- El tráfico de VPC externo se rutea a través de AWS Network Firewall

para agregar una capa adicional de seguridad del tráfico.

- Los host bastión se utilizan para administrar recursos de subred privada

desde un entorno local.

![Imagen 28-1](images/clase_6_page28_img1.png)

![Imagen 28-2](images/clase_6_page28_img2.png)

![Imagen 28-3](images/clase_6_page28_img3.png)

Conexión a servicios

administrados de AWS

Creación de un entorno de red

![Imagen 29-1](images/clase_6_page29_img1.png)

![Imagen 29-2](images/clase_6_page29_img2.png)

![Imagen 29-3](images/clase_6_page29_img3.png)

Conexión a recursos gestionados

AWS account

Region

Amazon VPC

Availability Zone

Private subnet

EC2 instance Amazon S3 bucket

![Imagen 30-1](images/clase_6_page30_img1.png)

![Imagen 30-2](images/clase_6_page30_img2.png)

![Imagen 30-3](images/clase_6_page30_img3.png)

![Imagen 30-4](images/clase_6_page30_img4.png)

![Imagen 30-5](images/clase_6_page30_img5.png)

![Imagen 30-6](images/clase_6_page30_img6.png)

![Imagen 30-7](images/clase_6_page30_img7.png)

![Imagen 30-8](images/clase_6_page30_img8.png)

![Imagen 30-9](images/clase_6_page30_img9.png)

Endpoints de interface VPC

AWS account

Region

Amazon VPC

Availability Zone

Private subnet IAM policy

Security group Other managed AWS

services

Elastic network Interface VPC

EC2 instance

interface endpoint

Amazon S3 bucket

AWS PrivateLink network

![Imagen 31-1](images/clase_6_page31_img1.png)

![Imagen 31-2](images/clase_6_page31_img2.png)

![Imagen 31-3](images/clase_6_page31_img3.png)

![Imagen 31-4](images/clase_6_page31_img4.png)

![Imagen 31-5](images/clase_6_page31_img5.png)

![Imagen 31-6](images/clase_6_page31_img6.png)

![Imagen 31-7](images/clase_6_page31_img7.png)

![Imagen 31-8](images/clase_6_page31_img8.png)

![Imagen 31-9](images/clase_6_page31_img9.png)

![Imagen 31-10](images/clase_6_page31_img10.png)

![Imagen 31-11](images/clase_6_page31_img11.png)

![Imagen 31-12](images/clase_6_page31_img12.png)

![Imagen 31-13](images/clase_6_page31_img13.png)

![Imagen 31-14](images/clase_6_page31_img14.png)

![Imagen 31-15](images/clase_6_page31_img15.png)

Endpoints de interface VPC

Configuración

AWS account

Region

2 Amazon VPC

Availability Zone

3

Private subnet

1

Security group

4

Elastic network Interface VPC

EC2 instance Amazon S3 bucket

interface endpoint endpoint

![Imagen 32-1](images/clase_6_page32_img1.png)

![Imagen 32-2](images/clase_6_page32_img2.png)

![Imagen 32-3](images/clase_6_page32_img3.png)

![Imagen 32-4](images/clase_6_page32_img4.png)

![Imagen 32-5](images/clase_6_page32_img5.png)

![Imagen 32-6](images/clase_6_page32_img6.png)

![Imagen 32-7](images/clase_6_page32_img7.png)

![Imagen 32-8](images/clase_6_page32_img8.png)

![Imagen 32-9](images/clase_6_page32_img9.png)

![Imagen 32-10](images/clase_6_page32_img10.png)

![Imagen 32-11](images/clase_6_page32_img11.png)

![Imagen 32-12](images/clase_6_page32_img12.png)

![Imagen 32-13](images/clase_6_page32_img13.png)

![Imagen 32-14](images/clase_6_page32_img14.png)

![Imagen 32-15](images/clase_6_page32_img15.png)

Gateway VPC endpoints

Tablas de rutas de redes privadas

Destino Objetivo

Prefix list 1 id Gateway VPC endpoint 1

Prefix list 2 id Gateway VPC endpoint 2

AWS account

Region

Amazon VPC

Private subnet

Gateway VPC endpoint 1 Amazon S3 bucket

Private

EC2 instance

subnet route

table

Gateway VPC endpoint 2 Amazon DynamoDB table

![Imagen 33-1](images/clase_6_page33_img1.png)

![Imagen 33-2](images/clase_6_page33_img2.png)

![Imagen 33-3](images/clase_6_page33_img3.png)

![Imagen 33-4](images/clase_6_page33_img4.png)

![Imagen 33-5](images/clase_6_page33_img5.png)

![Imagen 33-6](images/clase_6_page33_img6.png)

![Imagen 33-7](images/clase_6_page33_img7.png)

![Imagen 33-8](images/clase_6_page33_img8.png)

![Imagen 33-9](images/clase_6_page33_img9.png)

![Imagen 33-10](images/clase_6_page33_img10.png)

![Imagen 33-11](images/clase_6_page33_img11.png)

![Imagen 33-12](images/clase_6_page33_img12.png)

![Imagen 33-13](images/clase_6_page33_img13.png)

### Gateway VPC endpoints

Factor Endpoints de Interface VPC Endpoints de Gateway VPC

### Amazon S3 access

IP Privada de una subred en una VPC IP públicas de Amazon S3

point

On-premises Permite conectarse No

Otra región de

Permitido No

## AWS

Costo Tiene costo Sin costo

### Hasta 10 Gbps por AZ

Ancho de banda Escala automáticamente hasta 100 Sin límite

Gbps.

Tamaño del

Máximo: 8500 bytes. Sin límite

paquete

![Imagen 34-1](images/clase_6_page34_img1.png)

![Imagen 34-2](images/clase_6_page34_img2.png)

![Imagen 34-3](images/clase_6_page34_img3.png)

Gateway Load Balancer

Endpoints

1 Internet

AWS account

Region

Customer VPC Internet gateway Security service VPC

Private Public subnet

subnet

2

3

### EC2 application Gateway Load Gateway Load EC2 security

instance Balancer endpoint Balancer appliance instances

![Imagen 35-1](images/clase_6_page35_img1.png)

![Imagen 35-2](images/clase_6_page35_img2.png)

![Imagen 35-3](images/clase_6_page35_img3.png)

![Imagen 35-4](images/clase_6_page35_img4.png)

![Imagen 35-5](images/clase_6_page35_img5.png)

![Imagen 35-6](images/clase_6_page35_img6.png)

![Imagen 35-7](images/clase_6_page35_img7.png)

![Imagen 35-8](images/clase_6_page35_img8.png)

![Imagen 35-9](images/clase_6_page35_img9.png)

![Imagen 35-10](images/clase_6_page35_img10.png)

![Imagen 35-11](images/clase_6_page35_img11.png)

![Imagen 35-12](images/clase_6_page35_img12.png)

![Imagen 35-13](images/clase_6_page35_img13.png)

![Imagen 35-14](images/clase_6_page35_img14.png)

![Imagen 35-15](images/clase_6_page35_img15.png)

![Imagen 35-16](images/clase_6_page35_img16.png)

![Imagen 35-17](images/clase_6_page35_img17.png)

Conexión de servicios gestionados

### Resumen

- Los recursos de VPC pueden acceder a los servicios administrados

de AWS mediante endpoints de VPC.

- Un endpoint utiliza AWS PrivateLink para acceder a los servicios

administrados de AWS. Esto genera costos y presenta limitaciones de

rendimiento.

- Un Gateway VPC endpoint se integra directamente con Amazon S3

y Amazon DynamoDB. No genera costos ni tiene limitaciones de

rendimiento.

- Los endpoints de Gateway Load Balancer se utilizan con Gateway

Load Balancers para inspeccionar el tráfico con dispositivos de

seguridad.

![Imagen 36-1](images/clase_6_page36_img1.png)

![Imagen 36-2](images/clase_6_page36_img2.png)

![Imagen 36-3](images/clase_6_page36_img3.png)

Monitoreo de red

Otras consideraciones

![Imagen 37-1](images/clase_6_page37_img1.png)

![Imagen 37-2](images/clase_6_page37_img2.png)

![Imagen 37-3](images/clase_6_page37_img3.png)

Resolución de problemas de red

### Escenarios

- Tiempos de respuesta muy lentos en instancias EC2

- Imposibilidad de acceso a través de SSH

- No se aplican parches a las instancias de base de datos de EC2

![Imagen 38-1](images/clase_6_page38_img1.png)

![Imagen 38-2](images/clase_6_page38_img2.png)

![Imagen 38-3](images/clase_6_page38_img3.png)

VPC Flow logs

VPC flow logs

Amazon VPC

Elastic network

Amazon CloudWatch logs AWS Management

interface flow logs

Console

Private subnet

Amazon S3 bucket Amazon Athena

Elastic network

Flow logs

interface

Subnet flow

EC2 instance logs

Amazon Kinesis Amazon OpenSearch

Data Firehose stream Service

![Imagen 39-1](images/clase_6_page39_img1.png)

![Imagen 39-2](images/clase_6_page39_img2.png)

![Imagen 39-3](images/clase_6_page39_img3.png)

![Imagen 39-4](images/clase_6_page39_img4.png)

![Imagen 39-5](images/clase_6_page39_img5.png)

![Imagen 39-6](images/clase_6_page39_img6.png)

![Imagen 39-7](images/clase_6_page39_img7.png)

![Imagen 39-8](images/clase_6_page39_img8.png)

![Imagen 39-9](images/clase_6_page39_img9.png)

![Imagen 39-10](images/clase_6_page39_img10.png)

![Imagen 39-11](images/clase_6_page39_img11.png)

![Imagen 39-12](images/clase_6_page39_img12.png)

![Imagen 39-13](images/clase_6_page39_img13.png)

![Imagen 39-14](images/clase_6_page39_img14.png)

![Imagen 39-15](images/clase_6_page39_img15.png)

![Imagen 39-16](images/clase_6_page39_img16.png)

![Imagen 39-17](images/clase_6_page39_img17.png)

![Imagen 39-18](images/clase_6_page39_img18.png)

![Imagen 39-19](images/clase_6_page39_img19.png)

![Imagen 39-20](images/clase_6_page39_img20.png)

Permisos sobre flow logs

{

"Version": "2012-10-17",

"Statement": [

{

"Effect": "Allow",

"Action": [

"ec2:CreateFlowLogs",

La política de IAM otorga a los

"ec2:DescribeFlowLogs",

usuarios permisos para crear,

"ec2:DeleteFlowLogs" describir y eliminar registros de

flujo.

],

"Resource": "*"

}

]

}

![Imagen 40-1](images/clase_6_page40_img1.png)

![Imagen 40-2](images/clase_6_page40_img2.png)

![Imagen 40-3](images/clase_6_page40_img3.png)

![Imagen 40-4](images/clase_6_page40_img4.png)

![Imagen 40-5](images/clase_6_page40_img5.png)

Ejemplo de flow log (1 de 2)

Field name Field description Example value

version Versión de los registros de flujo de VPC 2

account-id Cuenta de AWS del propietario de la red 123456789010

interface-id Interfaz de red de tráfico eni-1235b8ca123456789

Dirección de origen para el tráfico entrante o interfaz de dirección

srcaddr 172.31.16.139

de red para el tráfico saliente

Dirección de destino para el tráfico saliente o dirección de interfaz

dstaddr 172.31.16.21

de red para el tráfico entrante

srcport Puerto de origen del tráfico 20641

dstport Puerto de destino del tráfico 22

protocol Número de protocolo de IANA de tráfico 6 (TCP)

![Imagen 41-1](images/clase_6_page41_img1.png)

![Imagen 41-2](images/clase_6_page41_img2.png)

![Imagen 41-3](images/clase_6_page41_img3.png)

Ejemplo de flow log (2 de 2)

Field name Field description Example value

packets Cantidad de paquetes transferidos 20

bytes Cantidad de bytes transferidos 4249

start Tiempo Unix en segundos del primer paquete recibido 1418530010

end Tiempo Unix en segundos del último paquete recibido 1418530070

Aceptar o rechazar el indicador de éxito o fracaso del

action ACCEPT

enrutamiento del tráfico

log-status Estado del registro de flujo: OK, NODATA, SKIPDATA OK

![Imagen 42-1](images/clase_6_page42_img1.png)

![Imagen 42-2](images/clase_6_page42_img2.png)

![Imagen 42-3](images/clase_6_page42_img3.png)

Resolución de problemas en VPC

Otras herramientas

### Reachability Analyzer

Permite probar la conectividad entre un recurso de origen y

un recurso de destino en una VPC.

### Network Access Analyzer

Identificar accesos de red no deseados a los recursos de AWS.

### Traffic Mirroring

Hace una copia del tráfico de red y la envía a soluciones de

seguridad y monitoreo.

![Imagen 43-1](images/clase_6_page43_img1.png)

![Imagen 43-2](images/clase_6_page43_img2.png)

![Imagen 43-3](images/clase_6_page43_img3.png)

![Imagen 43-4](images/clase_6_page43_img4.png)

![Imagen 43-5](images/clase_6_page43_img5.png)

Monitoreo de red

### Resumen

- VPC Flow Logs captura información sobre el tráfico de red en una VPC.

- Los registros incluyen todos los flujos dentro de un intervalo

- Reachability Analyzer permite chequear si dos recursos de una VPC tienen

conectividad

- Network Access Analyzer permite identificar accesos no deseados a los

recursos de una cuenta de AWS

- Traffic Mirroring permite copiar el tráfico de red y enviarlo a herramientas

de seguridad y monitoreo

![Imagen 44-1](images/clase_6_page44_img1.png)

![Imagen 44-2](images/clase_6_page44_img2.png)

Well-Architected Framework

Aplicado a la red

![Imagen 45-1](images/clase_6_page45_img1.png)

![Imagen 45-2](images/clase_6_page45_img2.png)

![Imagen 45-3](images/clase_6_page45_img3.png)

Well-Architected Framework

Pilares

![Imagen 46-1](images/clase_6_page46_img1.png)

![Imagen 46-2](images/clase_6_page46_img2.png)

![Imagen 46-3](images/clase_6_page46_img3.png)

![Imagen 46-4](images/clase_6_page46_img4.png)

![Imagen 46-5](images/clase_6_page46_img5.png)

![Imagen 46-6](images/clase_6_page46_img6.png)

Well-Architected Framework

Planificar la topología de red

Asegurarse de asignar

direcciones IP para permitir la

expansion de los servicios

![Imagen 47-1](images/clase_6_page47_img1.png)

![Imagen 47-2](images/clase_6_page47_img2.png)

![Imagen 47-3](images/clase_6_page47_img3.png)

### Well-Architected Framework

Protección de la infraestructura – Protección de redes

Crear capas de red

Controlar el tráfico en todas las

capas.

Implementar medidas de

protección e inspección

![Imagen 48-1](images/clase_6_page48_img1.png)

![Imagen 48-2](images/clase_6_page48_img2.png)

![Imagen 48-3](images/clase_6_page48_img3.png)

Well-Architected Framework

Performance

Entender el impacto de las redes en la performance

Evaluar las funciones de red disponibles

Performance

efficency

Elegir protocolos de red que aumenten la

performance

![Imagen 49-1](images/clase_6_page49_img1.png)

![Imagen 49-2](images/clase_6_page49_img2.png)

Well-Architected Framework

Optimización de costos

Tomar en cuenta los costos para elegir las

regiones

![Imagen 50-1](images/clase_6_page50_img1.png)

![Imagen 50-2](images/clase_6_page50_img2.png)

![Imagen 50-3](images/clase_6_page50_img3.png)

### Errores en el diseño de la red

### Identificar los errores de diseño de este escenario

- La empresa A, basada en Europa, vende calzado.

- La mayoría de los clientes de la compañía está en Estados Unidos.

- La compañía implementó sus servidores web y sus servidores de bases de datos en

la región de AWS de Irlanda, en una única VPC con una subred pública.

- La VPC tiene una netmask de /27 con 32 direcciones IP. La subred tiene una

netmask de /28 con 16 direcciones IP disponibles.

- El grupo de seguridad de los servidores web y de base de datos permite tráfico de

internet hacia los servidores.

- La compañía A proyecta un rápido crecimiento en el futuro cercano.

![Imagen 51-1](images/clase_6_page51_img1.png)

![Imagen 51-2](images/clase_6_page51_img2.png)

### Errores en el diseño de la red

Identificar los errores de diseño de este escenario

### Patrones Antipatrones

VPC grandes con subredes públicas y VPC pequeña con subredes

privadas grandes pequeñas

Grupos de seguridad estrictos Grupos de seguridad permisivos

organizados en capas según el uso del

servidor

### Sin acceso directo a las bases de datos Acceso directo a bases de datos

Región de AWS cercana a los clientes Región de AWS lejos de los clientes

![Imagen 52-1](images/clase_6_page52_img1.png)

![Imagen 52-2](images/clase_6_page52_img2.png)

Café Web

Challenge

![Imagen 53-1](images/clase_6_page53_img1.png)

![Imagen 53-2](images/clase_6_page53_img2.png)

![Imagen 53-3](images/clase_6_page53_img3.png)

Café Challenge

Resumen

En este laboratorio, harás lo siguiente:

- Asegurar el servidor de aplicaciones.

- Trasladar la instancia de la aplicación a una subred privada. Configurar

un bastion host en una subred pública. Configurar un grupo de seguridad

para cada instancia.

- Permitir que el servidor de aplicaciones descargue parches de Internet

configurando una puerta de enlace NAT en la subred pública.

- Agregar reglas de Network ACL para aumentar la seguridad.

![Imagen 54-1](images/clase_6_page54_img1.png)

![Imagen 54-2](images/clase_6_page54_img2.png)

Módulo 7. Servicios de red

### Resumen

- Explicar la función de una nube privada virtual (VPC) en la red en la nube

de Amazon Web Services (AWS).

- Identificar los componentes de una VPC que pueden conectar un

entorno de red de AWS a Internet.

- Aislar y proteger los recursos dentro de un entorno de red de AWS.

- Crear y monitorear una VPC con subredes, un Internet Gateway, tablas

de rutas y security groups.

- Aplicar los principios de AWS Well-Architected Framework a la

planificación y creación de un entorno de red.

![Imagen 55-1](images/clase_6_page55_img1.png)

![Imagen 55-2](images/clase_6_page55_img2.png)

Muchas gracias.

www.austral.edu.ar

![Imagen 56-1](images/clase_6_page56_img1.png)

![Imagen 56-2](images/clase_6_page56_img2.png)

![Imagen 56-3](images/clase_6_page56_img3.png)
