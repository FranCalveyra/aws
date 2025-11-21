# Clase 7

## Conexión entre redes

![Imagen 2-1](images/clase_7_page2_img1.png)

![Imagen 2-2](images/clase_7_page2_img2.png)

![Imagen 2-3](images/clase_7_page2_img3.png)

### Objetivos

- Describir cómo se conecta una red on-premises con los servicios

de AWS

- Explicar cómo se conectan múltiples VPC entre sí

- Conectar VPC mediante peering

- Describir cómo se pueden escalar VPC en la nube de AWS

- Aplicar los principios del Well-Architected Framework

![Imagen 3-1](images/clase_7_page3_img1.png)

![Imagen 3-2](images/clase_7_page3_img2.png)

![Imagen 3-3](images/clase_7_page3_img3.png)

### Principios de arquitectura

- Diseñar las conexiones aplicando medidas para la continuidad

y asegurando un ancho de banda adecuado, para las

aplicaciones on-premises, en la nube o hibridas.

- Seleccionar componentes de red que optimicen la

performance y reduzcan los costos de transferencia de datos

entre redes, para maximizar el valor.

- Proteger los datos en tránsito entre redes

![Imagen 4-1](images/clase_7_page4_img1.png)

![Imagen 4-2](images/clase_7_page4_img2.png)

![Imagen 4-3](images/clase_7_page4_img3.png)

Diseño de red con múltiples VPC

Arquitectura Full mesh Arquitectura Hub-and-spoke

## VPC A VPC B VPC A VPC B

Hub

## VPC C VPC D VPC C VPC D

![Imagen 5-1](images/clase_7_page5_img1.png)

![Imagen 5-2](images/clase_7_page5_img2.png)

![Imagen 5-3](images/clase_7_page5_img3.png)

![Imagen 5-4](images/clase_7_page5_img4.png)

![Imagen 5-5](images/clase_7_page5_img5.png)

![Imagen 5-6](images/clase_7_page5_img6.png)

![Imagen 5-7](images/clase_7_page5_img7.png)

![Imagen 5-8](images/clase_7_page5_img8.png)

![Imagen 5-9](images/clase_7_page5_img9.png)

![Imagen 5-10](images/clase_7_page5_img10.png)

![Imagen 5-11](images/clase_7_page5_img11.png)

### AWS Transit Gateway

- Es un router centralizado, regional para conectar VPCs y

redes on-premises sobre la base de una arquitectura hub-

and-spoke

- Es un servicio administrado por AWS que escala

automáticamente en base al volumen del tráfico de red.

- Se puede conectar con otros Transit Gateways en otras

regiones o cuentas de AWS.

- El costo depende de la cantidad de conexiones y de la

cantidad de tráfico

- Tiene una función que publica logs: Transit Gateway Flow

Logs

![Imagen 6-1](images/clase_7_page6_img1.png)

![Imagen 6-2](images/clase_7_page6_img2.png)

![Imagen 6-3](images/clase_7_page6_img3.png)

![Imagen 6-4](images/clase_7_page6_img4.png)

Ruteo con Transit Gateway entre VPCs

VPC 1 route table VPC 1: 10.1.0.0/16

Destination Target

Availability Zone 1 3

10.1.0.0/16 local

Subnet 1: 10.1.0.0/20 1 Transit gateway route table

Transit

Destination Target

10.0.0.0/8 gateway

Transit gateway

ID Elastic network interface 1 Transit

2 attachment VPC 1

gateway

10.1.0.0/16

attachment

## VPC 1 ID

## VPC 2: 10.2.0.0/16

VPC 2 route table

Transit

Availability Zone 2

Destination Target gateway

Transit 10.2.0.0/16

attachment

Subnet 1: 10.2.0.0/20

1

10.2.0.0/16 local Gateway

## VPC 2 ID

Transit

10.0.0.0/8 gateway

Elastic network interface 2 Transit gateway

## ID

attachment VPC 2

2

![Imagen 7-1](images/clase_7_page7_img1.png)

![Imagen 7-2](images/clase_7_page7_img2.png)

![Imagen 7-3](images/clase_7_page7_img3.png)

![Imagen 7-4](images/clase_7_page7_img4.png)

![Imagen 7-5](images/clase_7_page7_img5.png)

![Imagen 7-6](images/clase_7_page7_img6.png)

![Imagen 7-7](images/clase_7_page7_img7.png)

![Imagen 7-8](images/clase_7_page7_img8.png)

![Imagen 7-9](images/clase_7_page7_img9.png)

![Imagen 7-10](images/clase_7_page7_img10.png)

![Imagen 7-11](images/clase_7_page7_img11.png)

![Imagen 7-12](images/clase_7_page7_img12.png)

![Imagen 7-13](images/clase_7_page7_img13.png)

![Imagen 7-14](images/clase_7_page7_img14.png)

![Imagen 7-15](images/clase_7_page7_img15.png)

![Imagen 7-16](images/clase_7_page7_img16.png)

Tráfico saliente entre VPC

Transit gateway route table

## VPC 1: 10.1.0.0/16

VPC 1 route table

Destination Target

Destination Target Subnet 1: 10.1.0.0/20

Transit

10.1.0.0/16 local gateway

10.1.0.0/16

Transit gateway attachment

Transit Network interface 1

0.0.0.0/0 attachment VPC 1 VPC 1 ID

gateway ID

Transit

Egress VPC: 10.2.0.0/16

gateway

10.2.0.0/16

attachment

Subnet 2 route table

Subnet 2: 10.2.0.0/20

## VPC 2 ID

Transit

Destination Target

### Gateway

10.1.0.0/16 local Network interface 2 Transit gateway Egress VPC route table

attachment VPC 2

NAT Destination Target

0.0.0.0/0

gateway ID

10.2.0.0/16 local

Subnet 3: 10.2.16.0/20

Transit

10.1.0.0/16

gateway ID

NAT gateway Internet Internet

0.0.0.0/0

gateway gateway ID

![Imagen 8-1](images/clase_7_page8_img1.png)

![Imagen 8-2](images/clase_7_page8_img2.png)

![Imagen 8-3](images/clase_7_page8_img3.png)

![Imagen 8-4](images/clase_7_page8_img4.png)

![Imagen 8-5](images/clase_7_page8_img5.png)

![Imagen 8-6](images/clase_7_page8_img6.png)

![Imagen 8-7](images/clase_7_page8_img7.png)

![Imagen 8-8](images/clase_7_page8_img8.png)

![Imagen 8-9](images/clase_7_page8_img9.png)

![Imagen 8-10](images/clase_7_page8_img10.png)

![Imagen 8-11](images/clase_7_page8_img11.png)

![Imagen 8-12](images/clase_7_page8_img12.png)

![Imagen 8-13](images/clase_7_page8_img13.png)

![Imagen 8-14](images/clase_7_page8_img14.png)

Conexión de dos Transit Gateways

Peering

AWS account 1 AWS account 2

Region A Region B

1

## VPC 1: 3

4

10.1.0.0/16

## VPC 3:

11.1.0.0/16

## VPC 2:

Transit gateway

10.2.0.0/16 2 Transit Transit

peering

gateway A gateway B

attachment

Transit gateway A route table Transit gateway B route table

Destination Target Destination Target

4

1

10.1.0.0/16 Transit gateway attachment VPC 1 ID 11.1.0.0/16 Transit gateway attachment VPC 3 ID

3

10.2.0.0/16 Transit gateway attachment VPC 2 ID 2 10.1.0.0/16 Transit gateway peering attachment ID

11.1.0.0/16 Transit gateway peering attachment ID 3 10.2.0.0/16 Transit gateway peering attachment ID 3

![Imagen 9-1](images/clase_7_page9_img1.png)

![Imagen 9-2](images/clase_7_page9_img2.png)

![Imagen 9-3](images/clase_7_page9_img3.png)

![Imagen 9-4](images/clase_7_page9_img4.png)

![Imagen 9-5](images/clase_7_page9_img5.png)

![Imagen 9-6](images/clase_7_page9_img6.png)

![Imagen 9-7](images/clase_7_page9_img7.png)

![Imagen 9-8](images/clase_7_page9_img8.png)

![Imagen 9-9](images/clase_7_page9_img9.png)

![Imagen 9-10](images/clase_7_page9_img10.png)

![Imagen 9-11](images/clase_7_page9_img11.png)

![Imagen 9-12](images/clase_7_page9_img12.png)

![Imagen 9-13](images/clase_7_page9_img13.png)

![Imagen 9-14](images/clase_7_page9_img14.png)

![Imagen 9-15](images/clase_7_page9_img15.png)

![Imagen 9-16](images/clase_7_page9_img16.png)

![Imagen 9-17](images/clase_7_page9_img17.png)

![Imagen 9-18](images/clase_7_page9_img18.png)

![Imagen 9-19](images/clase_7_page9_img19.png)

![Imagen 9-20](images/clase_7_page9_img20.png)

![Imagen 9-21](images/clase_7_page9_img21.png)

![Imagen 9-22](images/clase_7_page9_img22.png)

![Imagen 9-23](images/clase_7_page9_img23.png)

![Imagen 9-24](images/clase_7_page9_img24.png)

![Imagen 9-25](images/clase_7_page9_img25.png)

Caso de uso

Escenario:

Una compañía tiene múltiples

### AWS account AWS account AWS account

departamentos de IT, cada uno departments department departments

A and B C D and E

posee su propia VPC.

Algunas VPC están dentro de la

## VPC A VPC D

misma cuenta de AWS, y otras

## VPC C

están en cuentas distintas.

## VPC B VPC E

Queremos conectar todas las

VPC para que tengan acceso a

los recursos de las demás. La

compañía está evaluando la

posibilidad de agregar nuevas

cuentas en el futuro.

Transit Gateway

![Imagen 10-1](images/clase_7_page10_img1.png)

![Imagen 10-2](images/clase_7_page10_img2.png)

![Imagen 10-3](images/clase_7_page10_img3.png)

![Imagen 10-4](images/clase_7_page10_img4.png)

![Imagen 10-5](images/clase_7_page10_img5.png)

![Imagen 10-6](images/clase_7_page10_img6.png)

![Imagen 10-7](images/clase_7_page10_img7.png)

![Imagen 10-8](images/clase_7_page10_img8.png)

![Imagen 10-9](images/clase_7_page10_img9.png)

![Imagen 10-10](images/clase_7_page10_img10.png)

![Imagen 10-11](images/clase_7_page10_img11.png)

Actividad

Configurar tablas de rutas de la VPC

![Imagen 11-1](images/clase_7_page11_img1.png)

![Imagen 11-2](images/clase_7_page11_img2.png)

![Imagen 11-3](images/clase_7_page11_img3.png)

Actividad

### Consigna

¿Qué rutas debemos agregar a las tablas de rutas de las VPC si queremos que

las cinco estén totalmente conectadas?

Transit gateway VPC route VPC route table VPC route table

## VPC ID VPC CIDR

VPC attachment ID table ID destination target

vpc-a 10.1.0.0/16 tgw-attach-vpc-a rtb-vpc-a ? ?

vpc-b 10.2.0.0/16 tgw-attach-vpc-b rtb-vpc-a ? ?

vpc-c 10.3.0.0/16 tgw-attach-vpc-c rtb-vpc-a ? ?

vpc-d 10.4.0.0/16 tgw-attach-vpc-d rtb-vpc-a ? ?

vpc-e 10.5.0.0/16 tgw-attach-vpc-e rtb-vpc-a ? ?

![Imagen 12-1](images/clase_7_page12_img1.png)

![Imagen 12-2](images/clase_7_page12_img2.png)

![Imagen 12-3](images/clase_7_page12_img3.png)

Actividad

### Consigna

## Configurar la tabla de rutas tgw-1 del Transit Gateway.

Transit gateway route table destination Transit gateway route table target

? ?

? ?

? ?

? ?

? ?

![Imagen 13-1](images/clase_7_page13_img1.png)

![Imagen 13-2](images/clase_7_page13_img2.png)

![Imagen 13-3](images/clase_7_page13_img3.png)

Actividad

Solución parte 1

Transit gateway VPC VPC route table VPC route

VPC ID VPC CIDR VPC route table ID

attachment ID destination table target

vpc-a 10.1.0.0/16 tgw-attach-vpc-a rtb-vpc-a 10.0.0.0/8 tgw-1

vpc-b 10.2.0.0/16 tgw-attach-vpc-b rtb-vpc-a 10.0.0.0/8 tgw-1

vpc-c 10.3.0.0/16 tgw-attach-vpc-c rtb-vpc-a 10.0.0.0/8 tgw-1

vpc-d 10.4.0.0/16 tgw-attach-vpc-d rtb-vpc-a 10.0.0.0/8 tgw-1

vpc-e 10.5.0.0/16 tgw-attach-vpc-e rtb-vpc-a 10.0.0.0/8 tgw-1

![Imagen 14-1](images/clase_7_page14_img1.png)

![Imagen 14-2](images/clase_7_page14_img2.png)

![Imagen 14-3](images/clase_7_page14_img3.png)

Actividad

### Solución parte 2

Transit gateway route table destination Transit gateway route table target

10.1.0.0/16 tgw-attach-vpc-a

10.2.0.0/16 tgw-attach-vpc-b

10.3.0.0/16 tgw-attach-vpc-c

10.4.0.0/16 tgw-attach-vpc-d

10.5.0.0/16 tgw-attach-vpc-e

![Imagen 15-1](images/clase_7_page15_img1.png)

![Imagen 15-2](images/clase_7_page15_img2.png)

![Imagen 15-3](images/clase_7_page15_img3.png)

### Resumen

Un Transit Gateway es un router centralizado regional que

conecta VPCs.

Los Transit Gateways de distintas regiones o cuentas se pueden

conectar entre sí

Un Transit Gateway soporta miles de conexiones.

Transit Gateway tiene costo por hora, que depende de:

- El número de conexiones

- La cantidad de tráfico

![Imagen 16-1](images/clase_7_page16_img1.png)

![Imagen 16-2](images/clase_7_page16_img2.png)

![Imagen 16-3](images/clase_7_page16_img3.png)

VPC peering

![Imagen 17-1](images/clase_7_page17_img1.png)

![Imagen 17-2](images/clase_7_page17_img2.png)

![Imagen 17-3](images/clase_7_page17_img3.png)

Arquitecturas mesh con VPC Peering

AWS account 1 AWS account 2

Region A Region B

## VPC A VPC B

### VPC A-B peering connection

VPC A-C peering VPC A-D peering connection VPC B-D peering

connection connection

VPC C-B peering connection

## VPC C VPC D

VPC C-D peering connection

![Imagen 18-1](images/clase_7_page18_img1.png)

![Imagen 18-2](images/clase_7_page18_img2.png)

![Imagen 18-3](images/clase_7_page18_img3.png)

![Imagen 18-4](images/clase_7_page18_img4.png)

![Imagen 18-5](images/clase_7_page18_img5.png)

![Imagen 18-6](images/clase_7_page18_img6.png)

![Imagen 18-7](images/clase_7_page18_img7.png)

![Imagen 18-8](images/clase_7_page18_img8.png)

![Imagen 18-9](images/clase_7_page18_img9.png)

![Imagen 18-10](images/clase_7_page18_img10.png)

![Imagen 18-11](images/clase_7_page18_img11.png)

![Imagen 18-12](images/clase_7_page18_img12.png)

![Imagen 18-13](images/clase_7_page18_img13.png)

![Imagen 18-14](images/clase_7_page18_img14.png)

![Imagen 18-15](images/clase_7_page18_img15.png)

![Imagen 18-16](images/clase_7_page18_img16.png)

![Imagen 18-17](images/clase_7_page18_img17.png)

¿Cómo establecer una conexión?

## VPC A: 10.1.0.0/16 VPC B: 10.2.0.0/16

VPC A-B peering connection

VPC A route table VPC B route table

Destination Target Destination Target

10.1.0.0/16 local 10.2.0.0/16 local

10.2.0.0/16 VPC A-B peering connection ID 10.1.0.0/16 VPC A-B peering connection ID

![Imagen 19-1](images/clase_7_page19_img1.png)

![Imagen 19-2](images/clase_7_page19_img2.png)

![Imagen 19-3](images/clase_7_page19_img3.png)

![Imagen 19-4](images/clase_7_page19_img4.png)

![Imagen 19-5](images/clase_7_page19_img5.png)

![Imagen 19-6](images/clase_7_page19_img6.png)

VPC peering connections

No son transitivas

## VPC A: VPC B: VPC C:

10.1.0.0/16 10.2.0.0/16 10.3.0.0/16

## VPC A-B VPC B-C

peering connection peering connection

### La VPC B puede

La VPC A puede La VPC C está

enviar y recibir

enviar y recibir conectada con la

tráfico de red de la

tráfico de la VPC B VPC B.

VPC A y de la VPC C.

![Imagen 20-1](images/clase_7_page20_img1.png)

![Imagen 20-2](images/clase_7_page20_img2.png)

![Imagen 20-3](images/clase_7_page20_img3.png)

![Imagen 20-4](images/clase_7_page20_img4.png)

![Imagen 20-5](images/clase_7_page20_img5.png)

![Imagen 20-6](images/clase_7_page20_img6.png)

![Imagen 20-7](images/clase_7_page20_img7.png)

![Imagen 20-8](images/clase_7_page20_img8.png)

![Imagen 20-9](images/clase_7_page20_img9.png)

![Imagen 20-10](images/clase_7_page20_img10.png)

![Imagen 20-11](images/clase_7_page20_img11.png)

![Imagen 20-12](images/clase_7_page20_img12.png)

![Imagen 20-13](images/clase_7_page20_img13.png)

![Imagen 20-14](images/clase_7_page20_img14.png)

VPC peering connections

Uso de rutas específicas

## VPC A: 10.1.0.0/16 VPC B: 10.2.0.0/16

VPC A subnet: VPC B subnet:

10.1.1.0/20 10.2.1.0/20

VPC A-B peering connection

EC2 instance

private IP:

10.2.1.18/32

VPC A subnet route table VPC B subnet route table

Destination Target Destination Target

10.1.0.0/16 local 10.2.0.0/16 local

10.2.1.18/32 VPC A-B peering connection ID 10.1.1.0/20 VPC A-B peering connection ID

![Imagen 21-1](images/clase_7_page21_img1.png)

![Imagen 21-2](images/clase_7_page21_img2.png)

![Imagen 21-3](images/clase_7_page21_img3.png)

![Imagen 21-4](images/clase_7_page21_img4.png)

![Imagen 21-5](images/clase_7_page21_img5.png)

![Imagen 21-6](images/clase_7_page21_img6.png)

![Imagen 21-7](images/clase_7_page21_img7.png)

![Imagen 21-8](images/clase_7_page21_img8.png)

![Imagen 21-9](images/clase_7_page21_img9.png)

### Caso de uso

Conexión a una VPC para acceder a recursos centralizados

VPC de archivos VPC compartida con

Active Directory

compartidos clientes

Active Directory

File user 1 VPC Customer 1 VPC

user 1 VPC

Active Directory user 1

File user 1 Customer 1

VPC peering connection

VPC peering connection VPC peering connection

Active Directory VPC

File sharing VPC Customer service

## VPC

![Imagen 22-1](images/clase_7_page22_img1.png)

![Imagen 22-2](images/clase_7_page22_img2.png)

![Imagen 22-3](images/clase_7_page22_img3.png)

![Imagen 22-4](images/clase_7_page22_img4.png)

![Imagen 22-5](images/clase_7_page22_img5.png)

![Imagen 22-6](images/clase_7_page22_img6.png)

![Imagen 22-7](images/clase_7_page22_img7.png)

![Imagen 22-8](images/clase_7_page22_img8.png)

![Imagen 22-9](images/clase_7_page22_img9.png)

![Imagen 22-10](images/clase_7_page22_img10.png)

![Imagen 22-11](images/clase_7_page22_img11.png)

![Imagen 22-12](images/clase_7_page22_img12.png)

Conexión de VPC con AWS Private Link

### Arquitectura

Consumer VPC: 10.1.0.0/16 Service provider VPC: 10.1.0.0/16

Consumer VPC subnet: Service provider VPC subnet

VPC endpoint Network Load EC2

EC2 instance

elastic network Balancer instances

interface

Cuando se usa AWS

PrivateLink con un Load

balancer de red, no se

necesitan conexiones de

peering entre las VPC

![Imagen 23-1](images/clase_7_page23_img1.png)

![Imagen 23-2](images/clase_7_page23_img2.png)

![Imagen 23-3](images/clase_7_page23_img3.png)

![Imagen 23-4](images/clase_7_page23_img4.png)

![Imagen 23-5](images/clase_7_page23_img5.png)

![Imagen 23-6](images/clase_7_page23_img6.png)

![Imagen 23-7](images/clase_7_page23_img7.png)

![Imagen 23-8](images/clase_7_page23_img8.png)

![Imagen 23-9](images/clase_7_page23_img9.png)

![Imagen 23-10](images/clase_7_page23_img10.png)

![Imagen 23-11](images/clase_7_page23_img11.png)

![Imagen 23-12](images/clase_7_page23_img12.png)

![Imagen 23-13](images/clase_7_page23_img13.png)

### Resumen

- VPC peering establece una conexión de red uno-a-uno entre dos VPC

para brindar rutas de tráfico de red privadas.

- No tiene costo, pero sí existen cargos por transferir datos entre AZ o

entre regiones.

- Permite el tráfico de red entre cuentas y regiones diferentes de AWS.

- No admite relaciones transitivas entre VPC.

- Si los bloques de Classless Inter-Domain Routing (CIDR) de las VPC se

superponen, hay que usar PrivateLink con un Network Load Balancer

para establecer la conexión

![Imagen 24-1](images/clase_7_page24_img1.png)

![Imagen 24-2](images/clase_7_page24_img2.png)

![Imagen 24-3](images/clase_7_page24_img3.png)

Conexión de redes remotas

Site-to-site VPN

![Imagen 25-1](images/clase_7_page25_img1.png)

![Imagen 25-2](images/clase_7_page25_img2.png)

![Imagen 25-3](images/clase_7_page25_img3.png)

Conexión de instalaciones on-premise

A una VPC

Entorno corporativo AWS Cloud

AWS account

Region

Red on-premise VPC

![Imagen 26-1](images/clase_7_page26_img1.png)

![Imagen 26-2](images/clase_7_page26_img2.png)

![Imagen 26-3](images/clase_7_page26_img3.png)

![Imagen 26-4](images/clase_7_page26_img4.png)

![Imagen 26-5](images/clase_7_page26_img5.png)

![Imagen 26-6](images/clase_7_page26_img6.png)

![Imagen 26-7](images/clase_7_page26_img7.png)

![Imagen 26-8](images/clase_7_page26_img8.png)

Conexión de servicios gestionados

Resumen

Crea una conexión segura entre un Gateway

en las instalaciones del cliente con un

Gateway privado virtual de AWS o un Transit

Gateway.

Crea dos túneles IPsec para cada conexión

a través de múltiples AZ.

Site-to-Site

## VPN

Hay costo por cada hora de conexión de

## VPN

![Imagen 27-1](images/clase_7_page27_img1.png)

![Imagen 27-2](images/clase_7_page27_img2.png)

![Imagen 27-3](images/clase_7_page27_img3.png)

![Imagen 27-4](images/clase_7_page27_img4.png)

Conexión VPN site-to-site

AWS Cloud

Entorno corporativo

AWS Region

## VPC

Red on-premise

Availability Zone 1

5

3 4

6 Security group 1

1 Internet VPN

2

connection Route table 1

tunnel 1

Customer Customer Virtual private

gateway device gateway gateway

Internet VPN

Security group 2

connection Route table 2

tunnel 2

Availability Zone 2

![Imagen 28-1](images/clase_7_page28_img1.png)

![Imagen 28-2](images/clase_7_page28_img2.png)

![Imagen 28-3](images/clase_7_page28_img3.png)

![Imagen 28-4](images/clase_7_page28_img4.png)

![Imagen 28-5](images/clase_7_page28_img5.png)

![Imagen 28-6](images/clase_7_page28_img6.png)

![Imagen 28-7](images/clase_7_page28_img7.png)

![Imagen 28-8](images/clase_7_page28_img8.png)

![Imagen 28-9](images/clase_7_page28_img9.png)

![Imagen 28-10](images/clase_7_page28_img10.png)

![Imagen 28-11](images/clase_7_page28_img11.png)

![Imagen 28-12](images/clase_7_page28_img12.png)

![Imagen 28-13](images/clase_7_page28_img13.png)

![Imagen 28-14](images/clase_7_page28_img14.png)

![Imagen 28-15](images/clase_7_page28_img15.png)

![Imagen 28-16](images/clase_7_page28_img16.png)

![Imagen 28-17](images/clase_7_page28_img17.png)

![Imagen 28-18](images/clase_7_page28_img18.png)

![Imagen 28-19](images/clase_7_page28_img19.png)

![Imagen 28-20](images/clase_7_page28_img20.png)

AWS VPN CloudHub

Internet VPN

AWS Region

On-premises connection 1

Red 1

Customer

gateway 1

Internet VPN

On-premises connection 2

Red 2

Customer

Virtual private

gateway 2

gateway

Internet VPN

On-premises connection 3

Red 3

Customer

gateway 3

![Imagen 29-1](images/clase_7_page29_img1.png)

![Imagen 29-2](images/clase_7_page29_img2.png)

![Imagen 29-3](images/clase_7_page29_img3.png)

![Imagen 29-4](images/clase_7_page29_img4.png)

![Imagen 29-5](images/clase_7_page29_img5.png)

![Imagen 29-6](images/clase_7_page29_img6.png)

![Imagen 29-7](images/clase_7_page29_img7.png)

![Imagen 29-8](images/clase_7_page29_img8.png)

![Imagen 29-9](images/clase_7_page29_img9.png)

![Imagen 29-10](images/clase_7_page29_img10.png)

![Imagen 29-11](images/clase_7_page29_img11.png)

![Imagen 29-12](images/clase_7_page29_img12.png)

![Imagen 29-13](images/clase_7_page29_img13.png)

![Imagen 29-14](images/clase_7_page29_img14.png)

AWS Global Accelerator

AWS Cloud

Edge location AWS Region

## VPC

On-premises

network

### Internet VPN

Customer connection Transit gateway Transit gateway

gateway AWS Global Transit

## VPN VPC

Accelerator Gateway

attachment attachment

https://speedtest.globalaccelerator.aws/#/

![Imagen 30-1](images/clase_7_page30_img1.png)

![Imagen 30-2](images/clase_7_page30_img2.png)

![Imagen 30-3](images/clase_7_page30_img3.png)

![Imagen 30-4](images/clase_7_page30_img4.png)

![Imagen 30-5](images/clase_7_page30_img5.png)

![Imagen 30-6](images/clase_7_page30_img6.png)

![Imagen 30-7](images/clase_7_page30_img7.png)

![Imagen 30-8](images/clase_7_page30_img8.png)

![Imagen 30-9](images/clase_7_page30_img9.png)

![Imagen 30-10](images/clase_7_page30_img10.png)

![Imagen 30-11](images/clase_7_page30_img11.png)

![Imagen 30-12](images/clase_7_page30_img12.png)

![Imagen 30-13](images/clase_7_page30_img13.png)

Aislar VPC con acceso por VPN

Transit Gateway

On-premises route table

Destination Target AWS Region

10.X.0.0/16 local VPC 1:

10.1.0.0/16

0.0.0.0/0 Transit gateway ID Transit gateway

attachment VPC 1

On-premises

Internet VPN

network

Customer

Transit

connection

gateway Transit VPC 2:

gateway VPN

10.99.99.0/24 Gateway 10.2.0.0/16

attachment

Transit gateway

attachment VPC 2

Transit gateway VPN route table Transit gateway VPC route table

### Destination Target Destination Target

10.1.0.0/16 Transit gateway attachment VPC 1 ID 10.99.99.0/24 Transit gateway VPN attachment ID

10.2.0.0/16 Transit gateway attachment VPC 2 ID

![Imagen 31-1](images/clase_7_page31_img1.png)

![Imagen 31-2](images/clase_7_page31_img2.png)

![Imagen 31-3](images/clase_7_page31_img3.png)

![Imagen 31-4](images/clase_7_page31_img4.png)

![Imagen 31-5](images/clase_7_page31_img5.png)

![Imagen 31-6](images/clase_7_page31_img6.png)

![Imagen 31-7](images/clase_7_page31_img7.png)

![Imagen 31-8](images/clase_7_page31_img8.png)

![Imagen 31-9](images/clase_7_page31_img9.png)

![Imagen 31-10](images/clase_7_page31_img10.png)

![Imagen 31-11](images/clase_7_page31_img11.png)

![Imagen 31-12](images/clase_7_page31_img12.png)

![Imagen 31-13](images/clase_7_page31_img13.png)

Resumen

### Conexión con instalaciones propias

- Site-to-site VPN crea una conexión segura entre un gateway on-

premises del cliente y un Virtual Private Gateway (o un Transit

Gateway) de AWS.

- Múltiples redes on-premises se pueden conectar a un único Virtual

Private Gateway.

- Global Accelerator permite acelerar las conexiones site-to-site.

- Se pueden configurar múltiples tablas de rutas en Transit Gateway

para aislar las VPC que brindan acceso completo a través de VPN.

![Imagen 32-1](images/clase_7_page32_img1.png)

![Imagen 32-2](images/clase_7_page32_img2.png)

![Imagen 32-3](images/clase_7_page32_img3.png)

Conexión de redes remotas

AWS Direct Connect

![Imagen 33-1](images/clase_7_page33_img1.png)

![Imagen 33-2](images/clase_7_page33_img2.png)

![Imagen 33-3](images/clase_7_page33_img3.png)

### AWS Direct Connect

### Es una conexión de VLAN (virtual local area network)

dedicada, privada que extiende la red on-premises para

incluir recursos de AWS.

Direct Brinda una experiencia de red consistente, con

Connect

rendimiento predecible y mayor ancho de banda.

![Imagen 34-1](images/clase_7_page34_img1.png)

![Imagen 34-2](images/clase_7_page34_img2.png)

![Imagen 34-3](images/clase_7_page34_img3.png)

![Imagen 34-4](images/clase_7_page34_img4.png)

AWS Direct Connect

Casos de uso

Entornos Volúmenes de Rendimiento de Seguridad y

híbridos datos grandes red predecible cumplimiento

![Imagen 35-1](images/clase_7_page35_img1.png)

![Imagen 35-2](images/clase_7_page35_img2.png)

![Imagen 35-3](images/clase_7_page35_img3.png)

![Imagen 35-4](images/clase_7_page35_img4.png)

![Imagen 35-5](images/clase_7_page35_img5.png)

![Imagen 35-6](images/clase_7_page35_img6.png)

![Imagen 35-7](images/clase_7_page35_img7.png)

AWS Direct Connect

Extensión de una red on-premises

Red On- AWS Cloud

premises

AWS Region

Direct Connect

location

## VPC

Virtual private

Router on- Router DX Direct

gateway

premises del del cliente Connect

cliente o de un endpoint

partner

Amazon S3

![Imagen 36-1](images/clase_7_page36_img1.png)

![Imagen 36-2](images/clase_7_page36_img2.png)

![Imagen 36-3](images/clase_7_page36_img3.png)

![Imagen 36-4](images/clase_7_page36_img4.png)

![Imagen 36-5](images/clase_7_page36_img5.png)

![Imagen 36-6](images/clase_7_page36_img6.png)

![Imagen 36-7](images/clase_7_page36_img7.png)

![Imagen 36-8](images/clase_7_page36_img8.png)

![Imagen 36-9](images/clase_7_page36_img9.png)

![Imagen 36-10](images/clase_7_page36_img10.png)

![Imagen 36-11](images/clase_7_page36_img11.png)

![Imagen 36-12](images/clase_7_page36_img12.png)

![Imagen 36-13](images/clase_7_page36_img13.png)

AWS Direct Connect

Con Transit Gateway

On- AWS Cloud

premises

network Direct Connect AWS Region

location

## VPC

Customer Customer Direct

Transit Transit

Direct Transit

router or DX Connect

gateway DX gateway VPC

Connect gateway

partner endpoint

attachment attachment

gateway

router

![Imagen 37-1](images/clase_7_page37_img1.png)

![Imagen 37-2](images/clase_7_page37_img2.png)

![Imagen 37-3](images/clase_7_page37_img3.png)

![Imagen 37-4](images/clase_7_page37_img4.png)

![Imagen 37-5](images/clase_7_page37_img5.png)

![Imagen 37-6](images/clase_7_page37_img6.png)

![Imagen 37-7](images/clase_7_page37_img7.png)

![Imagen 37-8](images/clase_7_page37_img8.png)

![Imagen 37-9](images/clase_7_page37_img9.png)

![Imagen 37-10](images/clase_7_page37_img10.png)

![Imagen 37-11](images/clase_7_page37_img11.png)

![Imagen 37-12](images/clase_7_page37_img12.png)

![Imagen 37-13](images/clase_7_page37_img13.png)

![Imagen 37-14](images/clase_7_page37_img14.png)

![Imagen 37-15](images/clase_7_page37_img15.png)

AWS Direct Connect

Alta disponibilidad

Enlace primario

Red on- AWS Cloud

premises AWS Region

Direct Connect location

## VPC

Router on- DX router Direct

premises Connect

Virtual private

endpoint

gateway

Conexíón VPN

Gateway del

cliente

Conexión

secundaria de

respaldo

![Imagen 38-1](images/clase_7_page38_img1.png)

![Imagen 38-2](images/clase_7_page38_img2.png)

![Imagen 38-3](images/clase_7_page38_img3.png)

![Imagen 38-4](images/clase_7_page38_img4.png)

![Imagen 38-5](images/clase_7_page38_img5.png)

![Imagen 38-6](images/clase_7_page38_img6.png)

![Imagen 38-7](images/clase_7_page38_img7.png)

![Imagen 38-8](images/clase_7_page38_img8.png)

![Imagen 38-9](images/clase_7_page38_img9.png)

![Imagen 38-10](images/clase_7_page38_img10.png)

![Imagen 38-11](images/clase_7_page38_img11.png)

![Imagen 38-12](images/clase_7_page38_img12.png)

![Imagen 38-13](images/clase_7_page38_img13.png)

![Imagen 38-14](images/clase_7_page38_img14.png)

![Imagen 38-15](images/clase_7_page38_img15.png)

![Imagen 38-16](images/clase_7_page38_img16.png)

![Imagen 38-17](images/clase_7_page38_img17.png)

![Imagen 38-18](images/clase_7_page38_img18.png)

![Imagen 38-19](images/clase_7_page38_img19.png)

![Imagen 38-20](images/clase_7_page38_img20.png)

![Imagen 38-21](images/clase_7_page38_img21.png)

![Imagen 38-22](images/clase_7_page38_img22.png)

![Imagen 38-23](images/clase_7_page38_img23.png)

![Imagen 38-24](images/clase_7_page38_img24.png)

![Imagen 38-25](images/clase_7_page38_img25.png)

![Imagen 38-26](images/clase_7_page38_img26.png)

![Imagen 38-27](images/clase_7_page38_img27.png)

![Imagen 38-28](images/clase_7_page38_img28.png)

![Imagen 38-29](images/clase_7_page38_img29.png)

AWS Direct Connect

Alta resiliencia con múltiples ubicaciones

AWS Cloud

Red 1 on-

DX location 1 AWS Region

premises

Router DX DX

Router 1 1 endpoint 1

## VPC

Red 2 on- Virtual

premises DX location 2 private

gateway

Router DX

## DX

Router 2

2

endpoint 2

![Imagen 39-1](images/clase_7_page39_img1.png)

![Imagen 39-2](images/clase_7_page39_img2.png)

![Imagen 39-3](images/clase_7_page39_img3.png)

![Imagen 39-4](images/clase_7_page39_img4.png)

![Imagen 39-5](images/clase_7_page39_img5.png)

![Imagen 39-6](images/clase_7_page39_img6.png)

![Imagen 39-7](images/clase_7_page39_img7.png)

![Imagen 39-8](images/clase_7_page39_img8.png)

![Imagen 39-9](images/clase_7_page39_img9.png)

![Imagen 39-10](images/clase_7_page39_img10.png)

![Imagen 39-11](images/clase_7_page39_img11.png)

![Imagen 39-12](images/clase_7_page39_img12.png)

![Imagen 39-13](images/clase_7_page39_img13.png)

![Imagen 39-14](images/clase_7_page39_img14.png)

![Imagen 39-15](images/clase_7_page39_img15.png)

![Imagen 39-16](images/clase_7_page39_img16.png)

![Imagen 39-17](images/clase_7_page39_img17.png)

Direct Connect

### Resumen

Direct Connect es una conexión VLAN dedicada, privada que extiende una red on-

premises para incluir recursos de AWS:

- Usa una interfaz privada para conectar una ubicación de Direct Connect con un

Gateway privado virtual.

- Usa una interfaz pública para conectar una ubicación de Direct Connect a

servicios de AWS que lo soportan.

- Usa una interfaz de tránsito para conectar una ubicación de Direct Connect a un

transit Gateway a través de Direct Connect Gateway.

Se puede usar una VPN como conexión secundaria para crear alta disponibilidad.

El uso de varias ubicaciones de Direct Connect permite mejorar la resiliencia de

varias redes on-premises.

![Imagen 40-1](images/clase_7_page40_img1.png)

![Imagen 40-2](images/clase_7_page40_img2.png)

Well-Architected Framework

Aplicado a la conexión entre redes

![Imagen 41-1](images/clase_7_page41_img1.png)

![Imagen 41-2](images/clase_7_page41_img2.png)

![Imagen 41-3](images/clase_7_page41_img3.png)

Well-Architected Framework

Pilares

![Imagen 42-1](images/clase_7_page42_img1.png)

![Imagen 42-2](images/clase_7_page42_img2.png)

![Imagen 42-3](images/clase_7_page42_img3.png)

![Imagen 42-4](images/clase_7_page42_img4.png)

![Imagen 42-5](images/clase_7_page42_img5.png)

![Imagen 42-6](images/clase_7_page42_img6.png)

Well-Architected Framework

### Planificar la topología de red

Crear enlaces redundantes entre las redes privadas de

la nube y las instalaciones on-premises

Elegir topologías hub-and-spoke en lugar de

implementar topologías mesh muchos a muchos

![Imagen 43-1](images/clase_7_page43_img1.png)

![Imagen 43-2](images/clase_7_page43_img2.png)

![Imagen 43-3](images/clase_7_page43_img3.png)

Well-Architected Framework

Protección de redes

Controlar el tráfico en todas las capas

Protección de datos en tránsito

Autenticar las comunicaciones de red

Cifrado

![Imagen 44-1](images/clase_7_page44_img1.png)

![Imagen 44-2](images/clase_7_page44_img2.png)

![Imagen 44-3](images/clase_7_page44_img3.png)

![Imagen 44-4](images/clase_7_page44_img4.png)

Well-Architected Framework

Performance

Elegir conexiones dedicadas o VPN apropiadas

para el tamaño de las cargas de trabajo

Performance

efficency

Elegir la ubicación de las cargas de trabajo en

función de los requerimientos de red

![Imagen 45-1](images/clase_7_page45_img1.png)

![Imagen 45-2](images/clase_7_page45_img2.png)

Well-Architected Framework

Optimización de costos

Elegir los componentes que optimicen el

costo de transferencia de datos

Implementar servicios que reduzcan el

costo de transferencia de datos

![Imagen 46-1](images/clase_7_page46_img1.png)

![Imagen 46-2](images/clase_7_page46_img2.png)

![Imagen 46-3](images/clase_7_page46_img3.png)

Módulo 8. Conexión de redes

### Resumen

- Describir cómo se puede conectar una red on-premises con la nube de

## AWS

- Describir cómo conectar múltiples VPC en la nube de AWS

- Conectar VPC usando VPC peering

- Describir el escalamiento de VPC en la nube de AWS

- Aplicar el AWS Well-Architected Framework a este proceso

![Imagen 47-1](images/clase_7_page47_img1.png)

![Imagen 47-2](images/clase_7_page47_img2.png)

### Sample exam question

An application running on Amazon EC2 instances in a virtual private cloud (VPC) processes sensitive information stored

on Amazon S3. The information is accessed by using an Amazon S3 public Regional endpoint over the internet. The

security team is concerned that the internet connectivity to Amazon S3 is a security risk. Which solution will resolve the

security concern with the most efficient network route?

Identify the key words and phrases before continuing.

The following are the key words and phrases:

- EC2 instances in a VPC

- Sensitive information

- Internet connectivity to Amazon S3 is a security risk

- Most efficient network route

48

### Sample exam question: Response choices

An application running on Amazon EC2 instances in a virtual private cloud (VPC) processes sensitive information stored

on Amazon S3. The information is accessed by using an Amazon S3 public regional endpoint over the internet. The

security team is concerned that the internet connectivity to Amazon S3 is a security risk. Which solution will resolve the

security concern with the most efficient network route?

Choice Response

A Access the data through an internet gateway.

B Access the data through a virtual private network (VPN) connection.

C Access the data through a NAT gateway.

D Access the data through a VPC endpoint for Amazon S3.

49

Sample exam question: Answer

The answer is D.

Choice Response

## A

## B

## C

D Access the data through a VPC endpoint for Amazon S3.

50

Muchas gracias.

www.austral.edu.ar

![Imagen 51-1](images/clase_7_page51_img1.png)

![Imagen 51-2](images/clase_7_page51_img2.png)

![Imagen 51-3](images/clase_7_page51_img3.png)
