# Clase 10

## Automatización de

infraestructura

![Imagen 2-1](images/clase_10_page2_img1.png)

![Imagen 2-2](images/clase_10_page2_img2.png)

![Imagen 2-3](images/clase_10_page2_img3.png)

### Objetivos

Reconocer cuándo y por qué se utiliza la automatización de

arquitectura.

Identificar cómo se usa la infraestructura como código (IaC) para crear

y administrar recursos de nube.

Identificar cómo modelar, crear y gestionar una colección de recursos

usando AWS CloudFormation.

Comprender cómo usar templates de AWS Quick Start CloudFormation

para definir una arquitectura.

Reconocer los usos de Amazon Q Developer.

Aplicar los principios del AWS Well-Architected Framework al diseño de

estrategias de automatización.

![Imagen 3-1](images/clase_10_page3_img1.png)

![Imagen 3-2](images/clase_10_page3_img2.png)

![Imagen 3-3](images/clase_10_page3_img3.png)

Automatización de la arquitectura

![Imagen 4-1](images/clase_10_page4_img1.png)

![Imagen 4-2](images/clase_10_page4_img2.png)

![Imagen 4-3](images/clase_10_page4_img3.png)

Sin automatización

### AWS Cloud

La construcción de la Configure data storage.

arquitectura es un

proceso largo y manual

Route your network.

Create your instances.

You AWS Management

Console

Build your databases.

Amazon DynamoDB Amazon RDS

![Imagen 5-1](images/clase_10_page5_img1.png)

![Imagen 5-2](images/clase_10_page5_img2.png)

![Imagen 5-3](images/clase_10_page5_img3.png)

![Imagen 5-4](images/clase_10_page5_img4.png)

![Imagen 5-5](images/clase_10_page5_img5.png)

![Imagen 5-6](images/clase_10_page5_img6.png)

![Imagen 5-7](images/clase_10_page5_img7.png)

![Imagen 5-8](images/clase_10_page5_img8.png)

![Imagen 5-9](images/clase_10_page5_img9.png)

![Imagen 5-10](images/clase_10_page5_img10.png)

![Imagen 5-11](images/clase_10_page5_img11.png)

![Imagen 5-12](images/clase_10_page5_img12.png)

![Imagen 5-13](images/clase_10_page5_img13.png)

![Imagen 5-14](images/clase_10_page5_img14.png)

![Imagen 5-15](images/clase_10_page5_img15.png)

![Imagen 5-16](images/clase_10_page5_img16.png)

### Riesgos del proceso manual

No es repetible a escala No tiene control de No tiene registro de No asegura la

versiones auditoría consistencia de las

configuraciones

![Imagen 6-1](images/clase_10_page6_img1.png)

![Imagen 6-2](images/clase_10_page6_img2.png)

![Imagen 6-3](images/clase_10_page6_img3.png)

![Imagen 6-4](images/clase_10_page6_img4.png)

![Imagen 6-5](images/clase_10_page6_img5.png)

![Imagen 6-6](images/clase_10_page6_img6.png)

![Imagen 6-7](images/clase_10_page6_img7.png)

### Beneficios de la automatización

### Reduce el acceso y la Permite crear entornos Aumenta la Automatiza las

intervención manual reproducibles productividad pruebas y el

escalamiento

![Imagen 7-1](images/clase_10_page7_img1.png)

![Imagen 7-2](images/clase_10_page7_img2.png)

![Imagen 7-3](images/clase_10_page7_img3.png)

![Imagen 7-4](images/clase_10_page7_img4.png)

![Imagen 7-5](images/clase_10_page7_img5.png)

![Imagen 7-6](images/clase_10_page7_img6.png)

![Imagen 7-7](images/clase_10_page7_img7.png)

### Resumen

Los procesos manuales están sujetos a error y son

inadecuados para soportar un negocio ágil.

Los procesos manuales crean riesgos para las aplicaciones

y los entornos.

La automatización ayuda a eliminar los procesos manuales

y construir con rapidez.

![Imagen 8-1](images/clase_10_page8_img1.png)

![Imagen 8-2](images/clase_10_page8_img2.png)

![Imagen 8-3](images/clase_10_page8_img3.png)

Infraestructura como código

![Imagen 9-1](images/clase_10_page9_img1.png)

![Imagen 9-2](images/clase_10_page9_img2.png)

![Imagen 9-3](images/clase_10_page9_img3.png)

### IaC

IaC es el proceso de escribir un template que crea y

mantiene recursos de nube.

Template

Recursos Recursos Recursos

Con IaC, es posible replicar, volver a

Legible para las Consumible por una

implementar y reutilizar infraestructura.

personas máquina

![Imagen 10-1](images/clase_10_page10_img1.png)

![Imagen 10-2](images/clase_10_page10_img2.png)

![Imagen 10-3](images/clase_10_page10_img3.png)

![Imagen 10-4](images/clase_10_page10_img4.png)

![Imagen 10-5](images/clase_10_page10_img5.png)

![Imagen 10-6](images/clase_10_page10_img6.png)

![Imagen 10-7](images/clase_10_page10_img7.png)

![Imagen 10-8](images/clase_10_page10_img8.png)

![Imagen 10-9](images/clase_10_page10_img9.png)

Beneficios de IaC

Application Load Balancer

Velocidad de implementación y

consistencia.

Auto Scaling group

Stack 1

### Propagación de cambios a

todo el stack, modificando Application Load Balancer

solo el template

Limpieza: al eliminar el stack, se

Auto Scaling group

borran todos los recursos Stack 2

Template

creados.

Application Load Balancer

Reusable, repetible y más fácil

de mantener.

Auto Scaling group

Stack 3

![Imagen 11-1](images/clase_10_page11_img1.png)

![Imagen 11-2](images/clase_10_page11_img2.png)

![Imagen 11-3](images/clase_10_page11_img3.png)

![Imagen 11-4](images/clase_10_page11_img4.png)

![Imagen 11-5](images/clase_10_page11_img5.png)

![Imagen 11-6](images/clase_10_page11_img6.png)

![Imagen 11-7](images/clase_10_page11_img7.png)

![Imagen 11-8](images/clase_10_page11_img8.png)

![Imagen 11-9](images/clase_10_page11_img9.png)

![Imagen 11-10](images/clase_10_page11_img10.png)

![Imagen 11-11](images/clase_10_page11_img11.png)

![Imagen 11-12](images/clase_10_page11_img12.png)

![Imagen 11-13](images/clase_10_page11_img13.png)

![Imagen 11-14](images/clase_10_page11_img14.png)

![Imagen 11-15](images/clase_10_page11_img15.png)

![Imagen 11-16](images/clase_10_page11_img16.png)

![Imagen 11-17](images/clase_10_page11_img17.png)

![Imagen 11-18](images/clase_10_page11_img18.png)

![Imagen 11-19](images/clase_10_page11_img19.png)

![Imagen 11-20](images/clase_10_page11_img20.png)

![Imagen 11-21](images/clase_10_page11_img21.png)

![Imagen 11-22](images/clase_10_page11_img22.png)

### CloudFormation

Es una forma simplificada de modelar, crear y administrar

recursos de AWS.

- Una colección de recursos se llama un stack de CloudFormation

- Se pagan los recursos que se usan, no el empleo de

CloudFormation

### CloudFormation

Permite crear, actualizar y eliminar stacks.

Permite la creación y actualización ordenadas y

predecibles de recursos.

Brinda un control de versiones de las implementaciones

de recursos de AWS.

![Imagen 12-1](images/clase_10_page12_img1.png)

![Imagen 12-2](images/clase_10_page12_img2.png)

![Imagen 12-3](images/clase_10_page12_img3.png)

![Imagen 12-4](images/clase_10_page12_img4.png)

### Servicios de AWS que usan CloudFormation

AWS Elastic AWS Quick Starts AWS Serverless AWS Amplify AWS Cloud

Beanstalk Application Development Kit

Model (AWS Framework de (AWS CDK)

Framework de

Arquitecturas de ExteSnAsMión) de desarrollo para

Servicio gestionado

código abierto

referencia CloudFormation aplicaciones web y

que crea para crear

automáticas, con una sintaxis mobile que

automáticamente recursos de

simplificada requiere menos

basadas en

un entorno de AWS CloudFormation

para construir código y menos

templates de

con el código de la infraestructura conocimiento de usando lenguajes

CloudFormation de programación

aplicacíon del serverless común las integraciones

familiares

cliente. con el backend

AWS CloudFormation

![Imagen 13-1](images/clase_10_page13_img1.png)

![Imagen 13-2](images/clase_10_page13_img2.png)

![Imagen 13-3](images/clase_10_page13_img3.png)

![Imagen 13-4](images/clase_10_page13_img4.png)

![Imagen 13-5](images/clase_10_page13_img5.png)

![Imagen 13-6](images/clase_10_page13_img6.png)

![Imagen 13-7](images/clase_10_page13_img7.png)

![Imagen 13-8](images/clase_10_page13_img8.png)

![Imagen 13-9](images/clase_10_page13_img9.png)

### Resumen

IaC es el proceso de crear y administrar recursos de nube mediante archivos

de template.

Permite implementar entornos complejos rápidamente, y volver a construirlos

o actualizarlos repetidamente.

### La solución de IaC más apropiada se selecciona en función de: el caso de

uso, el balance adecuado entre conveniencia y control, y las habilidades

del equipo de trabajo.

CloudFormation es un servicio de IaC que permite crear, actualizar y eliminar

servicios y arquitecturas.

![Imagen 14-1](images/clase_10_page14_img1.png)

![Imagen 14-2](images/clase_10_page14_img2.png)

![Imagen 14-3](images/clase_10_page14_img3.png)

Personalización con CloudFormation

![Imagen 15-1](images/clase_10_page15_img1.png)

![Imagen 15-2](images/clase_10_page15_img2.png)

![Imagen 15-3](images/clase_10_page15_img3.png)

CloudFormation

¿Cómo funciona?

Amazon Route 53

Auto scaling

Template Stack Stack

AWS CloudFormation

1

2 4

Elastic Load Balancing (ELB)

Subimos el template a

### Definimos nuestros

El stack mantiene el control

CloudFormation, o

recursos en un template

de los recursos creados.

apuntamos a un template

(o usamos uno existente) 3

Luego, podemos actualizar

almacenado en un bucket

Amazon EC2

el stack, detectar desvíos o

de S3

Ejecutamos la acción create stack.

borrar el stack.

Los recursos se crean en distintos

servicios de nuestra cuenta de AWS-

![Imagen 16-1](images/clase_10_page16_img1.png)

![Imagen 16-2](images/clase_10_page16_img2.png)

![Imagen 16-3](images/clase_10_page16_img3.png)

![Imagen 16-4](images/clase_10_page16_img4.png)

![Imagen 16-5](images/clase_10_page16_img5.png)

![Imagen 16-6](images/clase_10_page16_img6.png)

![Imagen 16-7](images/clase_10_page16_img7.png)

![Imagen 16-8](images/clase_10_page16_img8.png)

![Imagen 16-9](images/clase_10_page16_img9.png)

![Imagen 16-10](images/clase_10_page16_img10.png)

![Imagen 16-11](images/clase_10_page16_img11.png)

CloudFormation

Templates

Template

YAML example JSON example

### AWSTemplateFormatVersion: 2010-09-09 {

Resources: "AWSTemplateFormatVersion": "2010-09-09",

awsexamplebucket1: "Resources" : {

Type: AWS::S3::Bucket “awsexamplebucket1" : {

"Type" : "AWS::S3::Bucket"

}

}

}

### Ventajas de YAML JSON advantages

### Está optimizado para que sea legible Uso más difundido en otros sistemas (por ejemplo, API)

### Menos texto Suele ser menos complejo de generar y analizar

Permite incluir comentarios

![Imagen 17-1](images/clase_10_page17_img1.png)

![Imagen 17-2](images/clase_10_page17_img2.png)

![Imagen 17-3](images/clase_10_page17_img3.png)

![Imagen 17-4](images/clase_10_page17_img4.png)

CloudFormation

### Templates

AWSTemplateFormatVersion: "version date"

Description:

Un template puede incluir distintas secciones, String

Metadata:

que se definen en función de las cargas de

template metadata

trabajo que queremos crear.

Parameters:

set of parameters

La única sección obligatoria es Resources. El

Rules:

resto son opcionales.

set of rules

Mappings:

El ejemplo muestra un fragmento de un

set of mappings

template en YAML con el orden sugerido de

Conditions:

las secciones. set of conditions

Transform:

set of transforms

Resources:

set of resources

Outputs:

set of outputs

![Imagen 18-1](images/clase_10_page18_img1.png)

![Imagen 18-2](images/clase_10_page18_img2.png)

![Imagen 18-3](images/clase_10_page18_img3.png)

CloudFormation

Ejemplo de un template

{ Resources define lo que necesitamos

"Resources": {

crear en una cuenta de AWS

"Ec2Instance": {

"Type": "AWS::EC2::Instance",

"Properties": {

"ImageId": "ami-9d23aeea",

"InstanceType": "m3.medium",

"KeyName": {"Ref": "KeyPair}

}},

### Outputs especifica los valores que

"Outputs": { recibiremos cuando finalice la creación

del stack.

"InstanceId": {

"Description": "InstanceId",

"Value": {"Ref": "Ec2Instance"}

}

}

}

![Imagen 19-1](images/clase_10_page19_img1.png)

![Imagen 19-2](images/clase_10_page19_img2.png)

![Imagen 19-3](images/clase_10_page19_img3.png)

AWS CloudFormation Designer

1

Toolbar

Fit-to-window button 4

3

Canvas pane

2

Resources

Full screen and Split

types pane 5

screen buttons

Integrated JSON and

7

6

YAML editor pane

Messages pane

![Imagen 20-1](images/clase_10_page20_img1.png)

![Imagen 20-2](images/clase_10_page20_img2.png)

![Imagen 20-3](images/clase_10_page20_img3.png)

![Imagen 20-4](images/clase_10_page20_img4.png)

Condiciones en CloudFormation

Production Development

## VPC VPC

Se usa un único template,

pero se definen

condiciones:

Availability Zone A Availability Zone B Availability Zone A

Web tier • Dos AZ para el entorno Web tier

de producción.

- Una AZ para el entorno

de desarrollo.

Application tier Application tier

Template

Stack Stack

Primary database Standby database Primary database

![Imagen 21-1](images/clase_10_page21_img1.png)

![Imagen 21-2](images/clase_10_page21_img2.png)

![Imagen 21-3](images/clase_10_page21_img3.png)

![Imagen 21-4](images/clase_10_page21_img4.png)

![Imagen 21-5](images/clase_10_page21_img5.png)

![Imagen 21-6](images/clase_10_page21_img6.png)

![Imagen 21-7](images/clase_10_page21_img7.png)

![Imagen 21-8](images/clase_10_page21_img8.png)

![Imagen 21-9](images/clase_10_page21_img9.png)

![Imagen 21-10](images/clase_10_page21_img10.png)

![Imagen 21-11](images/clase_10_page21_img11.png)

![Imagen 21-12](images/clase_10_page21_img12.png)

![Imagen 21-13](images/clase_10_page21_img13.png)

![Imagen 21-14](images/clase_10_page21_img14.png)

![Imagen 21-15](images/clase_10_page21_img15.png)

![Imagen 21-16](images/clase_10_page21_img16.png)

![Imagen 21-17](images/clase_10_page21_img17.png)

![Imagen 21-18](images/clase_10_page21_img18.png)

![Imagen 21-19](images/clase_10_page21_img19.png)

![Imagen 21-20](images/clase_10_page21_img20.png)

![Imagen 21-21](images/clase_10_page21_img21.png)

![Imagen 21-22](images/clase_10_page21_img22.png)

![Imagen 21-23](images/clase_10_page21_img23.png)

![Imagen 21-24](images/clase_10_page21_img24.png)

![Imagen 21-25](images/clase_10_page21_img25.png)

![Imagen 21-26](images/clase_10_page21_img26.png)

![Imagen 21-27](images/clase_10_page21_img27.png)

![Imagen 21-28](images/clase_10_page21_img28.png)

![Imagen 21-29](images/clase_10_page21_img29.png)

![Imagen 21-30](images/clase_10_page21_img30.png)

### Conjuntos de cambios en CloudFormation

Se pueden usar change sets para hacer una vista previa antes de la

implementación de cambios.

Crear un Revisarlo Ejecutarlo

1 2 3

change set.

Original stack Change set Inspección de los cambios CloudFormation actualiza

el stack

El atributo DeletionPolicy se puede usar para preservar o resguardar un recurso

cuando se borra o actualiza su stack

![Imagen 22-1](images/clase_10_page22_img1.png)

![Imagen 22-2](images/clase_10_page22_img2.png)

![Imagen 22-3](images/clase_10_page22_img3.png)

![Imagen 22-4](images/clase_10_page22_img4.png)

![Imagen 22-5](images/clase_10_page22_img5.png)

![Imagen 22-6](images/clase_10_page22_img6.png)

![Imagen 22-7](images/clase_10_page22_img7.png)

Detección de desvíos en CloudFormation

Stack

Availability Zone Escenario

### CloudFormation

Template Lab VPC 1. Un entorno de aplicación se crea

con un stack de CloudFormation.

Public subnet 2. Luego, alguien modifica

manualmente el security group y

Security group abre un puerto entrante.

## Se ejecuta la detección de desvíos

Web server EC2 instance

en el stack.

## Todos los recursos, excepto el

Apache HTTP server

security group muestran el estado

IN_SYNC, pero el security group

muestra un estado MODIFIED con

detalles.

![Imagen 23-1](images/clase_10_page23_img1.png)

![Imagen 23-2](images/clase_10_page23_img2.png)

![Imagen 23-3](images/clase_10_page23_img3.png)

![Imagen 23-4](images/clase_10_page23_img4.png)

![Imagen 23-5](images/clase_10_page23_img5.png)

![Imagen 23-6](images/clase_10_page23_img6.png)

![Imagen 23-7](images/clase_10_page23_img7.png)

![Imagen 23-8](images/clase_10_page23_img8.png)

Alcance y organización de templates

### Categoría Tipo de template

Frontend services Interfaces web, acceso mobile y dashboard de análitica.

### Backend services Búsqueda, pagos, revisions y recomendaciones

### Shared services Bases de datos CRM, monitoreo, alarmas, subredes y security groups

Network VPCs, internet gateways, virtual private networks (VPNs), and NAT

devices

Security AWS Identity and Access Management (IAM) policies, users, groups, and

roles

![Imagen 24-1](images/clase_10_page24_img1.png)

![Imagen 24-2](images/clase_10_page24_img2.png)

CloudFormation

### Resumen

Es un servicio de IaC que se puede usar para modelar,

crear y gestionar un conjunto de recursos de AWS

En CloudFormation, la IaC se define en templates

creados en JSON o YAML.

Cuando se crean recursos de AWS a partir de un

template, forman un stack

Las acciones permitidas sobre un stack existente

incluyen: actualización, detección de desvíos y

eliminación del stack.

![Imagen 25-1](images/clase_10_page25_img1.png)

![Imagen 25-2](images/clase_10_page25_img2.png)

AWS Quick Start

Automatización de arquitectura

![Imagen 26-1](images/clase_10_page26_img1.png)

![Imagen 26-2](images/clase_10_page26_img2.png)

![Imagen 26-3](images/clase_10_page26_img3.png)

AWS Quick Starts

Implementaciones gold-standard

Se basan en las buenas prácticas de AWS

sobre seguridad y alta disponibilidad.

Se pueden utilizar para crear arquitecturas

AWS Quick

completas en menos de una hora

Starts

Se pueden usar para experimentar, como

base para nuestra propia arquitectura.

![Imagen 27-1](images/clase_10_page27_img1.png)

![Imagen 27-2](images/clase_10_page27_img2.png)

![Imagen 27-3](images/clase_10_page27_img3.png)

AWS Quick Starts

AWS Quick Start

Cuenta AWS

## VPC

CloudFormation

File system

Recursos

template

creados por el

DynamoDB Quick Start

Stack

Instances

S3 bucket

Guía de

implementación

![Imagen 28-1](images/clase_10_page28_img1.png)

![Imagen 28-2](images/clase_10_page28_img2.png)

![Imagen 28-3](images/clase_10_page28_img3.png)

![Imagen 28-4](images/clase_10_page28_img4.png)

![Imagen 28-5](images/clase_10_page28_img5.png)

![Imagen 28-6](images/clase_10_page28_img6.png)

![Imagen 28-7](images/clase_10_page28_img7.png)

![Imagen 28-8](images/clase_10_page28_img8.png)

![Imagen 28-9](images/clase_10_page28_img9.png)

![Imagen 28-10](images/clase_10_page28_img10.png)

![Imagen 28-11](images/clase_10_page28_img11.png)

![Imagen 28-12](images/clase_10_page28_img12.png)

AWS Quick Starts

Ejemplo

Amazon Rekognition

6

CloudFormation stack

1 2 3 4

Client CloudFront API Gateway Lambda Amazon S3

5

Secrets Manager

![Imagen 29-1](images/clase_10_page29_img1.png)

![Imagen 29-2](images/clase_10_page29_img2.png)

![Imagen 29-3](images/clase_10_page29_img3.png)

![Imagen 29-4](images/clase_10_page29_img4.png)

![Imagen 29-5](images/clase_10_page29_img5.png)

![Imagen 29-6](images/clase_10_page29_img6.png)

![Imagen 29-7](images/clase_10_page29_img7.png)

![Imagen 29-8](images/clase_10_page29_img8.png)

![Imagen 29-9](images/clase_10_page29_img9.png)

AWS QuickStarts

### Resumen

### AWS Quick Starts contiene templates de CloudFormation

construidos por arquitectos de solución y partners que reflejan las

buenas prácticas de AWS.

### AWS Quick Starts está conformado por un template y una guía de

implementación, que provee detalles sobre las opciones de

despliegue y las configuraciones más adecuadas.

También sirve para ver patrones y prácticas que sirvan para

acelerar el desarrollo de templates propios.

![Imagen 30-1](images/clase_10_page30_img1.png)

![Imagen 30-2](images/clase_10_page30_img2.png)

Amazon Q Developer

Personalización

![Imagen 31-1](images/clase_10_page31_img1.png)

![Imagen 31-2](images/clase_10_page31_img2.png)

![Imagen 31-3](images/clase_10_page31_img3.png)

Infraestructura como código

Desafíos

Error humano Habilidades Tamaño y Vulnerabilidades

dispares complejidad de los de seguridad

templates

![Imagen 32-1](images/clase_10_page32_img1.png)

![Imagen 32-2](images/clase_10_page32_img2.png)

![Imagen 32-3](images/clase_10_page32_img3.png)

![Imagen 32-4](images/clase_10_page32_img4.png)

![Imagen 32-5](images/clase_10_page32_img5.png)

![Imagen 32-6](images/clase_10_page32_img6.png)

Amazon Q Developer

### Asistente de código asistido por IA generativa

### Diseñado para desarrolladores y profesionales de IT

Genera código y ayuda a entender, construir, extender

y operar aplicaciones en AWS

### Amazon Q

Escanea el código para detector vulnerabilidades de

Developer

seguridad

Seguro y privado desde el diseño

![Imagen 33-1](images/clase_10_page33_img1.png)

![Imagen 33-2](images/clase_10_page33_img2.png)

![Imagen 33-3](images/clase_10_page33_img3.png)

Amazon Q Developer

Apoyo al desarrollo de aplicaciones

Maintain and

Plan Create Test and secure Operate

modernize

Formular preguntas Recibir recomendaciones Generar tests unitarios Detectar y corregir Modernizar el código

para obtener una guía en varios idiomas. errores con Amazon Q

Escanear el código para

referenciable y Developer Agent.

Implementar funciones a detector Verificar la conectividad

contextualizada.

través de comentarios o vulnerabilidades y de red con VPC

Explicar el código con prompts. recibir sugerencias de Reachability Analyzer.

codificación remediación

Conversar con el IDE.

conversacional

![Imagen 34-1](images/clase_10_page34_img1.png)

![Imagen 34-2](images/clase_10_page34_img2.png)

![Imagen 34-3](images/clase_10_page34_img3.png)

![Imagen 34-4](images/clase_10_page34_img4.png)

![Imagen 34-5](images/clase_10_page34_img5.png)

![Imagen 34-6](images/clase_10_page34_img6.png)

![Imagen 34-7](images/clase_10_page34_img7.png)

Ejemplo

Uso de Amazon Q Developer con

### CloudFormation

El código se agrega al

Amazon Q Developer hace

template

sugerencias que el

desarrollador puede aceptar

El desarrollador empieza a

escribir el nombre del

recurso

![Imagen 35-1](images/clase_10_page35_img1.png)

![Imagen 35-2](images/clase_10_page35_img2.png)

![Imagen 35-3](images/clase_10_page35_img3.png)

![Imagen 35-4](images/clase_10_page35_img4.png)

![Imagen 35-5](images/clase_10_page35_img5.png)

![Imagen 35-6](images/clase_10_page35_img6.png)

![Imagen 35-7](images/clase_10_page35_img7.png)

![Imagen 35-8](images/clase_10_page35_img8.png)

![Imagen 35-9](images/clase_10_page35_img9.png)

![Imagen 35-10](images/clase_10_page35_img10.png)

![Imagen 35-11](images/clase_10_page35_img11.png)

![Imagen 35-12](images/clase_10_page35_img12.png)

Automatización

Pilares del Well-Architected Framework

![Imagen 36-1](images/clase_10_page36_img1.png)

![Imagen 36-2](images/clase_10_page36_img2.png)

![Imagen 36-3](images/clase_10_page36_img3.png)

Well-Architected Framework

Buenas prácticas para la automatización

![Imagen 37-1](images/clase_10_page37_img1.png)

![Imagen 37-2](images/clase_10_page37_img2.png)

![Imagen 37-3](images/clase_10_page37_img3.png)

![Imagen 37-4](images/clase_10_page37_img4.png)

![Imagen 37-5](images/clase_10_page37_img5.png)

![Imagen 37-6](images/clase_10_page37_img6.png)

![Imagen 37-7](images/clase_10_page37_img7.png)

Well-Architected Framework

Prepararse y diseñar para la operación

Buenas prácticas

Realizar las operaciones como código

Hacer cambios frecuentes, pequeños y

reversibles.

Automatizar completamente la

integración y la implementación.

![Imagen 38-1](images/clase_10_page38_img1.png)

![Imagen 38-2](images/clase_10_page38_img2.png)

![Imagen 38-3](images/clase_10_page38_img3.png)

![Imagen 38-4](images/clase_10_page38_img4.png)

Well-Architected Framework

Seguridad

Automatizar buenas prácticas de

seguridad

![Imagen 39-1](images/clase_10_page39_img1.png)

![Imagen 39-2](images/clase_10_page39_img2.png)

![Imagen 39-3](images/clase_10_page39_img3.png)

![Imagen 39-4](images/clase_10_page39_img4.png)

Well-Architected Framework

Optimización en el tiempo

Buena práctica

Aplicar automatización a las

operaciones

![Imagen 40-1](images/clase_10_page40_img1.png)

![Imagen 40-2](images/clase_10_page40_img2.png)

![Imagen 40-3](images/clase_10_page40_img3.png)

![Imagen 40-4](images/clase_10_page40_img4.png)

Well-Architected Framework

### Resumen

Las buenas prácticas relacionadas con la automatización de la

arquitectura incluyen:

- Ejecutar operaciones como código

- Hacer cambios frecuentes, pequeños y reversibles

- Automatizar completamente la integración y la implementación

- Automatizar las buenas prácticas de seguridad

- Implementar los cambios mediante automatizaciones

- Usar automatización para crear y escalar recursos

![Imagen 41-1](images/clase_10_page41_img1.png)

![Imagen 41-2](images/clase_10_page41_img2.png)

![Imagen 41-3](images/clase_10_page41_img3.png)

Módulo 11

### Pregunta de práctica

Consider a situation where you want to create a single AWS CloudFormation template that is capable of creating

both a production environment that spans two Availability Zones and a development environment that exists in a

single Availability Zone. Which optional section of the CloudFormation template will you want to make use of to

configure the logic that will support this?

Identifiquemos las palabras o frases clave:

The following are the key words and phrases:

- A single AWS CloudFormation template

- An environment with two Availability Zones and an environment with a single Availability Zone

- Optional section

![Imagen 42-1](images/clase_10_page42_img1.png)

![Imagen 42-2](images/clase_10_page42_img2.png)

![Imagen 42-3](images/clase_10_page42_img3.png)

Módulo 11

### Pregunta de práctica

Consider a situation where you want to create a single AWS CloudFormation template that is capable of creating

both a production environment that spans two Availability Zones and a development environment that exists in a

single Availability Zone. Which optional section of the CloudFormation template will you want to make use of to

configure the logic that will support this?

Choice Response

A Conditions

B Outputs

C Resources

D Description

![Imagen 43-1](images/clase_10_page43_img1.png)

![Imagen 43-2](images/clase_10_page43_img2.png)

![Imagen 43-3](images/clase_10_page43_img3.png)

Módulo 11

### Pregunta de práctica

Consider a situation where you want to create a single AWS CloudFormation template that is capable of creating

both a production environment that spans two Availability Zones and a development environment that exists in a

single Availability Zone. Which optional section of the CloudFormation template will you want to make use of to

configure the logic that will support this?

Choice Response

A Conditions

![Imagen 44-1](images/clase_10_page44_img1.png)

![Imagen 44-2](images/clase_10_page44_img2.png)

![Imagen 44-3](images/clase_10_page44_img3.png)

Módulo 11

### Resumen

Reconocer cuándo automatizar la arquitectura y por qué.

Identificar cómo podemos usar IaC como estrategia para

administrar recursos de nube.

Entender cómo modelar, crear y administrar una colección de

recursos de AWS con AWS CloudFormation.

Identificar cómo usar AWS Quick Start para definir una

arquitectura.

Reconocer los usos de Amazon Q Developer.

Aplicar los principios del AWS Well-Architected Framework a la

automatización.

![Imagen 45-1](images/clase_10_page45_img1.png)

![Imagen 45-2](images/clase_10_page45_img2.png)

![Imagen 45-3](images/clase_10_page45_img3.png)

Muchas gracias.

www.austral.edu.ar

![Imagen 46-1](images/clase_10_page46_img1.png)

![Imagen 46-2](images/clase_10_page46_img2.png)

![Imagen 46-3](images/clase_10_page46_img3.png)
