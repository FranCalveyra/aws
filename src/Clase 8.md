# Clase 8

## Seguridad de usuarios,

aplicaciones y datos

![Imagen 2-1](images/clase_8_page2_img1.png)

![Imagen 2-2](images/clase_8_page2_img2.png)

![Imagen 2-3](images/clase_8_page2_img3.png)

### Objetivos

Administrar permisos mediante usuarios, grupos y roles de AWS

## IAM

Implementar federación de usuarios en una arquitectura para

aumentar la seguridad

### Describir cómo se manejan múltiples cuentas de AWS

Reconocer la función de las políticas de control de servicio

(SCP) de AWS Organizations.

Cifrar datos en reposo usando AWS Key Management Service

## (AWS KMS).

Identificar los servicios de seguridad adecuados para ciertos

casos de uso.

![Imagen 3-1](images/clase_8_page3_img1.png)

![Imagen 3-2](images/clase_8_page3_img2.png)

![Imagen 3-3](images/clase_8_page3_img3.png)

Administración de permisos

![Imagen 4-1](images/clase_8_page4_img1.png)

![Imagen 4-2](images/clase_8_page4_img2.png)

![Imagen 4-3](images/clase_8_page4_img3.png)

Gestión de permisos por usuarios

## IAM

user policy Configuración inicial

Cada desarrollador recibe acceso total a Amazon EC2 a través de

Attach Access

políticas vinculadas con usuarios individuales.

John

Amazon EC2

### Se necesitan permisos adicionales

Cada desarrollador necesita acceso a Amazon S3. Para

### Attach Access

implementar el cambio, el administrador debe hacer tres

modificaciones, una para cada política de usuario de IAM.

Mary

Amazon EC2

### Attach Access Crece la cantidad de usuarios

Este enfoque resulta inmanejable. ¿Cuál es la solución más

Pat

apropiada?

Amazon EC2

![Imagen 5-1](images/clase_8_page5_img1.png)

![Imagen 5-2](images/clase_8_page5_img2.png)

![Imagen 5-3](images/clase_8_page5_img3.png)

![Imagen 5-4](images/clase_8_page5_img4.png)

![Imagen 5-5](images/clase_8_page5_img5.png)

![Imagen 5-6](images/clase_8_page5_img6.png)

![Imagen 5-7](images/clase_8_page5_img7.png)

![Imagen 5-8](images/clase_8_page5_img8.png)

![Imagen 5-9](images/clase_8_page5_img9.png)

![Imagen 5-10](images/clase_8_page5_img10.png)

![Imagen 5-11](images/clase_8_page5_img11.png)

![Imagen 5-12](images/clase_8_page5_img12.png)

Asignación de permisos por grupos

IAM Developer

Attach

group

Amazon S3

Access

Add as members

Group policy

(users do not have policies)

Amazon EC2

John Mary Pat

![Imagen 6-1](images/clase_8_page6_img1.png)

![Imagen 6-2](images/clase_8_page6_img2.png)

![Imagen 6-3](images/clase_8_page6_img3.png)

![Imagen 6-4](images/clase_8_page6_img4.png)

![Imagen 6-5](images/clase_8_page6_img5.png)

![Imagen 6-6](images/clase_8_page6_img6.png)

![Imagen 6-7](images/clase_8_page6_img7.png)

![Imagen 6-8](images/clase_8_page6_img8.png)

![Imagen 6-9](images/clase_8_page6_img9.png)

![Imagen 6-10](images/clase_8_page6_img10.png)

![Imagen 6-11](images/clase_8_page6_img11.png)

![Imagen 6-12](images/clase_8_page6_img12.png)

![Imagen 6-13](images/clase_8_page6_img13.png)

![Imagen 6-14](images/clase_8_page6_img14.png)

![Imagen 6-15](images/clase_8_page6_img15.png)

![Imagen 6-16](images/clase_8_page6_img16.png)

![Imagen 6-17](images/clase_8_page6_img17.png)

![Imagen 6-18](images/clase_8_page6_img18.png)

### Ejemplo

### Uso de grupos para reflejar la estructura organizacional

Al contratar un Nuevo desarrollador, se lo agrega en

el grupo de desarrolladores. Inmediatamente,

heredará los mismos accesos que tiene el resto del

equipo.

Si Ana cambia de rol, se hará lo siguiente:

- Quitarle los permisos del grupo de Test

- Agregarla al grupo de desarrollo.

Los usuarios pueden pertenecer a más de un grupo,

pero los grupos no pueden anidarse.

### Los permisos de las políticas asociadas a un usuario

prevalecen sobre los del grupo si son más restrictivos.

![Imagen 7-1](images/clase_8_page7_img1.png)

![Imagen 7-2](images/clase_8_page7_img2.png)

![Imagen 7-3](images/clase_8_page7_img3.png)

![Imagen 7-4](images/clase_8_page7_img4.png)

### Ejemplo

- Allow access S3

### User

- Allow access DynamoDB

policy

- Deny access Kinesis

Policy associated with user Zhang

¿Zhang puede acceder a Amazon Athena?

Zhang

Member of

¿Zhang tiene acceso a Amazon Kinesis?

IAM group

(Developer group)

### Policy associated with developer group

- Allow access S3

Group • Allow access Athena

policy • Allow access DynamoDB

- Allow access Kinesis

![Imagen 8-1](images/clase_8_page8_img1.png)

![Imagen 8-2](images/clase_8_page8_img2.png)

![Imagen 8-3](images/clase_8_page8_img3.png)

![Imagen 8-4](images/clase_8_page8_img4.png)

![Imagen 8-5](images/clase_8_page8_img5.png)

### Ejemplo

- Allow access S3

### User

- Allow access DynamoDB

policy

- Deny access Kinesis

Zhang puede acceder a Amazon Athena

Policy associated with user Zhang

Sí, por ser miembro del grupo, Zhang

tiene acceso a Amazon Athena.

Zhang

Zhang no tiene acceso a Amazon Kinesis

Member of

Aunque el grupo habilita el acceso a

IAM group

Kinesis, la política de usuario de Zhang

(Developer group)

niega explícitamente el acceso a Kinesis.

### Policy associated with developer group

- Allow access S3

Group • Allow access Athena

policy • Allow access DynamoDB

- Allow access Kinesis

![Imagen 9-1](images/clase_8_page9_img1.png)

![Imagen 9-2](images/clase_8_page9_img2.png)

![Imagen 9-3](images/clase_8_page9_img3.png)

![Imagen 9-4](images/clase_8_page9_img4.png)

![Imagen 9-5](images/clase_8_page9_img5.png)

Escalamiento usando RBAC

### Definición de roles Actualización del rol

Crear una política IAM con los permisos Actualizar la política.

del rol.

### Si el nuevo recurso es usado por varios

La política indica los recursos accesibles. roles, es necesario modificar múltiples

políticas.

Asociar la política con una entidad de

IAM (usuario, grupo o rol).

Permissions in Resources

multiple policies

Database Admin Instance Amazon S3

Network Admin Amazon S3 Alarm

Developer Database table Lambda function

![Imagen 10-1](images/clase_8_page10_img1.png)

![Imagen 10-2](images/clase_8_page10_img2.png)

![Imagen 10-3](images/clase_8_page10_img3.png)

![Imagen 10-4](images/clase_8_page10_img4.png)

![Imagen 10-5](images/clase_8_page10_img5.png)

![Imagen 10-6](images/clase_8_page10_img6.png)

![Imagen 10-7](images/clase_8_page10_img7.png)

![Imagen 10-8](images/clase_8_page10_img8.png)

![Imagen 10-9](images/clase_8_page10_img9.png)

![Imagen 10-10](images/clase_8_page10_img10.png)

![Imagen 10-11](images/clase_8_page10_img11.png)

![Imagen 10-12](images/clase_8_page10_img12.png)

![Imagen 10-13](images/clase_8_page10_img13.png)

![Imagen 10-14](images/clase_8_page10_img14.png)

Uso de ABAC

¿Qué es? Ventajas

### Estrategia de autorización que

Es más flexible que las políticas en

define permisos en basados en

las que hay que identificar

atributos.

recursos individuales.

Los atributos son claves o pares de Permiten asignar permisos

clave-valor. granulares sin actualizar las

políticas cada vez que se agrega

En AWS, los atributos se llaman

un recurso.

etiquetas (tags).

### Es altamente escalable y

Las etiquetas se aplican a recursos

auditable.

de IAM y de AWS.

![Imagen 11-1](images/clase_8_page11_img1.png)

![Imagen 11-2](images/clase_8_page11_img2.png)

Etiquetas en AWS

Son metadatos conformados por un

par (key/value).

Ejemplos de etiquetas aplicadas a una

instancia EC2

Se pueden aplicar a recursos de las

cuentas de AWS, y también a

Key Value

usuarios y roles de IAM.

Name Web server

Project Unicorn

Podemos crear nuestras propias

Env Dev

etiquetas.

Muchas de las API de AWS

devuelven datos de etiquetas.

Se utilizan para facturación, control

de accesos o aplicación de filtros a

las vistas.

![Imagen 12-1](images/clase_8_page12_img1.png)

![Imagen 12-2](images/clase_8_page12_img2.png)

Uso de ABAC para asignar permisos

Ejemplo

Requerir atributos para nuevos recursos

Definir atributos de control de

Attributes

accesos a las entidades

Env = dev

Env = test

Maint Maint

Project = maint Dev Instance Test Instance

Developer on maint project

Project = newdev

Configurar permisos en base a

Newdev

Developer on newdev project Newdev

los atributos

Test Instance

Dev Instance

Tester on maint project

Testers

Developers

Una política para todos los

Amazon S3

Amazon S3

permisos

Tester on newdev project bucket bucket

![Imagen 13-1](images/clase_8_page13_img1.png)

![Imagen 13-2](images/clase_8_page13_img2.png)

![Imagen 13-3](images/clase_8_page13_img3.png)

![Imagen 13-4](images/clase_8_page13_img4.png)

![Imagen 13-5](images/clase_8_page13_img5.png)

![Imagen 13-6](images/clase_8_page13_img6.png)

![Imagen 13-7](images/clase_8_page13_img7.png)

![Imagen 13-8](images/clase_8_page13_img8.png)

![Imagen 13-9](images/clase_8_page13_img9.png)

![Imagen 13-10](images/clase_8_page13_img10.png)

![Imagen 13-11](images/clase_8_page13_img11.png)

![Imagen 13-12](images/clase_8_page13_img12.png)

![Imagen 13-13](images/clase_8_page13_img13.png)

![Imagen 13-14](images/clase_8_page13_img14.png)

![Imagen 13-15](images/clase_8_page13_img15.png)

![Imagen 13-16](images/clase_8_page13_img16.png)

![Imagen 13-17](images/clase_8_page13_img17.png)

![Imagen 13-18](images/clase_8_page13_img18.png)

![Imagen 13-19](images/clase_8_page13_img19.png)

![Imagen 13-20](images/clase_8_page13_img20.png)

### Resumen

### Los grupos IAM permiten asignar los mismos derechos de acceso a

múltiples usuarios. Los grupos deben reflejar las funciones de trabajo.

ABAC es más conveniente que RBAC para escalar mejor la gestión de

permisos.

### ABAC es una estrategia de autorización que define los permisos en base a

ciertos atributos. Simplifica la gestión del control de acceso mediante la

combinación de permisos en una única política.

Los atributos son pares key/value.

AWS permite asignar atributos a los recursos e identidades mediante la

creación de etiquetas.

![Imagen 14-1](images/clase_8_page14_img1.png)

![Imagen 14-2](images/clase_8_page14_img2.png)

Federación

Seguridad de usuarios, grupos y datos

![Imagen 15-1](images/clase_8_page15_img1.png)

![Imagen 15-2](images/clase_8_page15_img2.png)

![Imagen 15-3](images/clase_8_page15_img3.png)

Federación de identidades

### Generalidades

### Es un sistema de confianza entre dos partes para autenticar usuarios y

compartir información necesaria para autorizar el acceso a los recursos.

### Proveedor de identidad (IdP) Proveedor del servicio

Responsable de la autenticación Responsable de controlar el

del usuario. acceso a sus recursos.

Ejemplos Ejemplos

AWS services

OpenID connect (OIDC), como

Redes sociales

Amazon, Facebook y Google

Banco online

Security Assertion Markup Language

(SAML), como Active Directory

Federation Services

![Imagen 16-1](images/clase_8_page16_img1.png)

![Imagen 16-2](images/clase_8_page16_img2.png)

![Imagen 16-3](images/clase_8_page16_img3.png)

Servicios de AWS

Con soporte de federación de identidades

AWS Identity and Access Management (IAM)

AWS IAM Identity Center (ex AWS Single Sign-On)

AWS Security Token Service (AWS STS)

Amazon Cognito

![Imagen 17-1](images/clase_8_page17_img1.png)

![Imagen 17-2](images/clase_8_page17_img2.png)

![Imagen 17-3](images/clase_8_page17_img3.png)

![Imagen 17-4](images/clase_8_page17_img4.png)

![Imagen 17-5](images/clase_8_page17_img5.png)

![Imagen 17-6](images/clase_8_page17_img6.png)

![Imagen 17-7](images/clase_8_page17_img7.png)

Federación de identidades

Ejemplo

Organización externa AWS Account

1 2

AWS Identity

and Access

3 Management

User Credentials

## (IAM)

AWS resources

Directorio

4

externo Credentials

Usuario

Amazon Amazon Amazon

DynamoDB EC2 S3

![Imagen 18-1](images/clase_8_page18_img1.png)

![Imagen 18-2](images/clase_8_page18_img2.png)

![Imagen 18-3](images/clase_8_page18_img3.png)

![Imagen 18-4](images/clase_8_page18_img4.png)

![Imagen 18-5](images/clase_8_page18_img5.png)

![Imagen 18-6](images/clase_8_page18_img6.png)

![Imagen 18-7](images/clase_8_page18_img7.png)

![Imagen 18-8](images/clase_8_page18_img8.png)

![Imagen 18-9](images/clase_8_page18_img9.png)

![Imagen 18-10](images/clase_8_page18_img10.png)

![Imagen 18-11](images/clase_8_page18_img11.png)

IAM Identity Center

### Sucesor de AWS Single Sign On

Permite crear o conectar identidades únicas y

manejar los accesos de manera centralizada en

múltiples cuentas de AWS

Función de administración unificada para definir,

personalizar y asignar accesos granulares

IAM Identity

### Center

Proporciona un portal para acceder a todas las

cuentas o aplicaciones de AWS

Se puede usar en conjunto con IAM

![Imagen 19-1](images/clase_8_page19_img1.png)

![Imagen 19-2](images/clase_8_page19_img2.png)

![Imagen 19-3](images/clase_8_page19_img3.png)

![Imagen 19-4](images/clase_8_page19_img4.png)

### IAM Security Token Service (STS)

Es una API que permite solicitar credenciales

transitorias con privilegios limitados.

Las credenciales pueden ser utilizadas por usuarios

IAM, usuarios federados o aplicaciones.

## IAM STS

![Imagen 20-1](images/clase_8_page20_img1.png)

![Imagen 20-2](images/clase_8_page20_img2.png)

![Imagen 20-3](images/clase_8_page20_img3.png)

![Imagen 20-4](images/clase_8_page20_img4.png)

Federación de identidades

Identity brokers

### AWS STS genera El identity broker le

### Un identity broker

El usuario accede con

credenciales brinda las credenciales

funciona como

las credenciales que

temporales de manera temporales a la

intermediario entre los

tiene en el IdP

dinámica aplicación

IdP y el SP

Tienen un tiempo de AWS STS le transfiere

Por ejemplo, un login The identity broker

expiración que las credenciales

corporativo o su requests temporary

puede variar entre temporales al

Amazon.com ID. credentials from

minutos y horas. broker.

## AWS STS.

![Imagen 21-1](images/clase_8_page21_img1.png)

![Imagen 21-2](images/clase_8_page21_img2.png)

![Imagen 21-3](images/clase_8_page21_img3.png)

Federación de identidades

Para el acceso a la consola

Customer AWS Cloud

Application AWS services

User

1

accesses

broker 4 User accesses AWS DynamoDB Amazon Amazon

services or console

## EC2 S3

Single sign-on

## (SSO)

2

Broker retrieves temporary

3

User security credentials from STS,

authenticated passes them to user application IAM

## AWS STS

Corporate Identity

identity store broker

Role Policy

![Imagen 22-1](images/clase_8_page22_img1.png)

![Imagen 22-2](images/clase_8_page22_img2.png)

![Imagen 22-3](images/clase_8_page22_img3.png)

![Imagen 22-4](images/clase_8_page22_img4.png)

![Imagen 22-5](images/clase_8_page22_img5.png)

![Imagen 22-6](images/clase_8_page22_img6.png)

![Imagen 22-7](images/clase_8_page22_img7.png)

![Imagen 22-8](images/clase_8_page22_img8.png)

![Imagen 22-9](images/clase_8_page22_img9.png)

![Imagen 22-10](images/clase_8_page22_img10.png)

![Imagen 22-11](images/clase_8_page22_img11.png)

![Imagen 22-12](images/clase_8_page22_img12.png)

![Imagen 22-13](images/clase_8_page22_img13.png)

![Imagen 22-14](images/clase_8_page22_img14.png)

![Imagen 22-15](images/clase_8_page22_img15.png)

![Imagen 22-16](images/clase_8_page22_img16.png)

![Imagen 22-17](images/clase_8_page22_img17.png)

![Imagen 22-18](images/clase_8_page22_img18.png)

![Imagen 22-19](images/clase_8_page22_img19.png)

![Imagen 22-20](images/clase_8_page22_img20.png)

Federación de identidades

Usando SAML (Windows / LDAP)

Assertion posted to sign

Customer AWS Cloud

## 4 IA

in endpoint for SAML Role

## M

1 User

navigates Policy

Sign-in endpoint AWS STS

to a URL

for SAML

Redirected to

3 5 the console

2

IdP returns

IdP

## SAML

authenticates

assertion

user

Identity store Portal (IdP)

(LDAP or Microsoft

Active Directory)

![Imagen 23-1](images/clase_8_page23_img1.png)

![Imagen 23-2](images/clase_8_page23_img2.png)

![Imagen 23-3](images/clase_8_page23_img3.png)

![Imagen 23-4](images/clase_8_page23_img4.png)

![Imagen 23-5](images/clase_8_page23_img5.png)

![Imagen 23-6](images/clase_8_page23_img6.png)

![Imagen 23-7](images/clase_8_page23_img7.png)

![Imagen 23-8](images/clase_8_page23_img8.png)

![Imagen 23-9](images/clase_8_page23_img9.png)

![Imagen 23-10](images/clase_8_page23_img10.png)

![Imagen 23-11](images/clase_8_page23_img11.png)

![Imagen 23-12](images/clase_8_page23_img12.png)

![Imagen 23-13](images/clase_8_page23_img13.png)

![Imagen 23-14](images/clase_8_page23_img14.png)

![Imagen 23-15](images/clase_8_page23_img15.png)

![Imagen 23-16](images/clase_8_page23_img16.png)

![Imagen 23-17](images/clase_8_page23_img17.png)

![Imagen 23-18](images/clase_8_page23_img18.png)

![Imagen 23-19](images/clase_8_page23_img19.png)

![Imagen 23-20](images/clase_8_page23_img20.png)

### Amazon Cognito

Es un servicio administrado que brinda:

- Autenticación, autorización y gestión de usuarios

para aplicaciones web y móviles

- Identidades federadas para accede por medio de

terceros (Amazon, Facebook, Google) o SAML

- Grupos de usuarios (user pools) que mantienen un

Amazon conjunto de perfiles de usuarios con tokens de

autenticación

### Cognito

- Grupos de identidades (identity pools) que permiten

crear identidades únicas y asignación de permisos

para los usuarios

![Imagen 24-1](images/clase_8_page24_img1.png)

![Imagen 24-2](images/clase_8_page24_img2.png)

![Imagen 24-3](images/clase_8_page24_img3.png)

![Imagen 24-4](images/clase_8_page24_img4.png)

Federación de identidades

Para el acceso desde aplicaciones

Authenticate and

1

get tokens

Amazon Cognito

user pool

Access your own

2

App resources

Your backend

resources

![Imagen 25-1](images/clase_8_page25_img1.png)

![Imagen 25-2](images/clase_8_page25_img2.png)

![Imagen 25-3](images/clase_8_page25_img3.png)

![Imagen 25-4](images/clase_8_page25_img4.png)

![Imagen 25-5](images/clase_8_page25_img5.png)

![Imagen 25-6](images/clase_8_page25_img6.png)

![Imagen 25-7](images/clase_8_page25_img7.png)

![Imagen 25-8](images/clase_8_page25_img8.png)

![Imagen 25-9](images/clase_8_page25_img9.png)

Federación de identidades

Ejemplo de Amazon Cognito

AWS Cloud

Redirect or

1 2

Authenticate and get

post back

tokens

Federating IdP

Amazon Cognito

IdP token

Exchange tokens for

3

user pool

AWS credentials

AWS credentials

Web or

Amazon Cognito

mobile

identity pool

application

Access AWS services

4 AWS services

with credentials

![Imagen 26-1](images/clase_8_page26_img1.png)

![Imagen 26-2](images/clase_8_page26_img2.png)

![Imagen 26-3](images/clase_8_page26_img3.png)

![Imagen 26-4](images/clase_8_page26_img4.png)

![Imagen 26-5](images/clase_8_page26_img5.png)

![Imagen 26-6](images/clase_8_page26_img6.png)

![Imagen 26-7](images/clase_8_page26_img7.png)

![Imagen 26-8](images/clase_8_page26_img8.png)

![Imagen 26-9](images/clase_8_page26_img9.png)

![Imagen 26-10](images/clase_8_page26_img10.png)

![Imagen 26-11](images/clase_8_page26_img11.png)

![Imagen 26-12](images/clase_8_page26_img12.png)

![Imagen 26-13](images/clase_8_page26_img13.png)

![Imagen 26-14](images/clase_8_page26_img14.png)

![Imagen 26-15](images/clase_8_page26_img15.png)

![Imagen 26-16](images/clase_8_page26_img16.png)

Federación de identidades

### User pools

User Amazon Cognito user Identity provider App API/databas

pool e

Connect to app

Request sign-

in

Redirect to third-party IdP (optional)

Additional challenges

Challenge responses

Provide tokens and sign in

Provide access

token and retrieve

data

![Imagen 27-1](images/clase_8_page27_img1.png)

![Imagen 27-2](images/clase_8_page27_img2.png)

![Imagen 27-3](images/clase_8_page27_img3.png)

![Imagen 27-4](images/clase_8_page27_img4.png)

![Imagen 27-5](images/clase_8_page27_img5.png)

![Imagen 27-6](images/clase_8_page27_img6.png)

![Imagen 27-7](images/clase_8_page27_img7.png)

![Imagen 27-8](images/clase_8_page27_img8.png)

![Imagen 27-9](images/clase_8_page27_img9.png)

Amazon Cognito

User pools

### Característica Descripción

Sign-up Los usuarios pueden ingresar su información en la aplicación y crear un perfil de usuario nativo

para el user pool.

Se puede redirigir a los usuarios a un IdP de terceros, el usuario autoriza pasar la información de

autenticación a Amazon Cognito.

Crear usuarios a partir de una fuente de datos o un esquema.

Sign-in Se puede usar el pool de usuarios para brindar acceso o recurrir a un IdP.

Identidades federadas El user pool permite gestionar los tokens recibidos de IdP que usan Open ID o SAML

de terceros

UI propia para sign-up Se pueden personalizar las páginas web de Amazon Cognito (sign-up, sign-in, MFA, password

y sign-in reset).

JWTs Permite usar tokens JWT para acceder a recursos del servidor o a otros servicios de AWS (con

credenciales temporales).

Grupos de user pools Los usuarios se pueden organizar en grupos para simplificar la gestión de permisos.

![Imagen 28-1](images/clase_8_page28_img1.png)

![Imagen 28-2](images/clase_8_page28_img2.png)

![Imagen 28-3](images/clase_8_page28_img3.png)

Federación de identidades

### Resumen

La federación de identidades es un Sistema de confianza entre IdS y SPs.

### AWS IAM Identity Center brinda funciones unificadas para definir, personalizar y

asignar permisos granulares asociadas a las responsabilidades.

### AWS STS es un servicio web que proporciona credenciales temporales de AWS y

permite que un usuario (IAM, federado o de aplicación) asuma un rol de IAM.

Un identity broker permite la federación de usuarios que ya tienen una identidad

fuera de AWS, como un directorio corporativo.

### Amazon Cognito es un servicio gestionado que brinda autenticación, autorización y

gestión de usuarios en aplicaciones web y móviles. Puede tener sus propios usuarios

o integrarse con IdP de terceros.

![Imagen 29-1](images/clase_8_page29_img1.png)

![Imagen 29-2](images/clase_8_page29_img2.png)

![Imagen 29-3](images/clase_8_page29_img3.png)

Gestión de accesos a

múltiples cuentas

![Imagen 30-1](images/clase_8_page30_img1.png)

![Imagen 30-2](images/clase_8_page30_img2.png)

![Imagen 30-3](images/clase_8_page30_img3.png)

Acceso a recursos

Patrones habituales

Múltiples VPC en una cuenta de AWS

AWS account

## VPC VPC VPC VPC

Shared services Development Test Production

Multiples cuentas, con una VPC cada una

AWS account AWS account AWS account AWS account

## VPC VPC VPC VPC

Shared services Development Test Production

![Imagen 31-1](images/clase_8_page31_img1.png)

![Imagen 31-2](images/clase_8_page31_img2.png)

![Imagen 31-3](images/clase_8_page31_img3.png)

![Imagen 31-4](images/clase_8_page31_img4.png)

![Imagen 31-5](images/clase_8_page31_img5.png)

![Imagen 31-6](images/clase_8_page31_img6.png)

![Imagen 31-7](images/clase_8_page31_img7.png)

![Imagen 31-8](images/clase_8_page31_img8.png)

![Imagen 31-9](images/clase_8_page31_img9.png)

![Imagen 31-10](images/clase_8_page31_img10.png)

![Imagen 31-11](images/clase_8_page31_img11.png)

![Imagen 31-12](images/clase_8_page31_img12.png)

![Imagen 31-13](images/clase_8_page31_img13.png)

![Imagen 31-14](images/clase_8_page31_img14.png)

![Imagen 31-15](images/clase_8_page31_img15.png)

![Imagen 31-16](images/clase_8_page31_img16.png)

Uso de múltiples cuentas

Ventajas y desafíos

Ventajas

Desafíos

### Separación de unidades de negocio o departamentos

La gestión de seguridad en múltiples cuentas es

más compleja

Separación de ambientes

### Aislamiento de datos de auditoria y recuperación

Es necesario aplicar procesos manuales en la

creación de cada cuenta

Segregación de cuentas para cargas de trabajo sujetas

a regulación

Determinación de qué organización debe recibir la

facturación

Facilidad para la creación de alertas de costo por

unidad de negocio

Necesidad de un gobierno centralizado que asegure

Ahorro de costos (hay precios preferenciales)

la consistencia y el cumplimiento

![Imagen 32-1](images/clase_8_page32_img1.png)

![Imagen 32-2](images/clase_8_page32_img2.png)

![Imagen 32-3](images/clase_8_page32_img3.png)

### AWS Organizations

### Servicio de gestión de cuentas que permite consolidar

múltiples cuentas de AWS en una única organización,

que se administra de manera centralizada.

### Permite aplicar descuentos

Permite la creación y gestión de cuentas

### Tiene funciones para consolidar la facturación

Permite agrupar las cuentas jerárquicamente

### AWS Organizations

### Permite aplicar controles centralizados sobre las políticas

de los servicios de AWS, mediante service control policies

(SCPs)

![Imagen 33-1](images/clase_8_page33_img1.png)

![Imagen 33-2](images/clase_8_page33_img2.png)

![Imagen 33-3](images/clase_8_page33_img3.png)

![Imagen 33-4](images/clase_8_page33_img4.png)

AWS Organizations

Creación de unidades organizativas

En la cuenta primaria de

AWS Cloud

AWS Organizations:

Primary account

## Crear una jerarquía

AWS Organizations Internal IT

de unidades

## OU

organizativas (OUs). root

Engineering

## OU

Development

## OU

Production

## OU

![Imagen 34-1](images/clase_8_page34_img1.png)

![Imagen 34-2](images/clase_8_page34_img2.png)

![Imagen 34-3](images/clase_8_page34_img3.png)

![Imagen 34-4](images/clase_8_page34_img4.png)

![Imagen 34-5](images/clase_8_page34_img5.png)

![Imagen 34-6](images/clase_8_page34_img6.png)

![Imagen 34-7](images/clase_8_page34_img7.png)

![Imagen 34-8](images/clase_8_page34_img8.png)

![Imagen 34-9](images/clase_8_page34_img9.png)

![Imagen 34-10](images/clase_8_page34_img10.png)

AWS Organizations

Creación de unidades organizativas

AWS Cloud

En la cuenta primaria de

Member accounts

AWS Organizations:

Primary account

AWS account #1

AWS Organizations Internal IT OU

## Crear una jerarquía

de unidades

root

organizativas (OUs).

AWS account #2

Engineering OU

## Asignar cuentas a las

OU, como cuentas

miembro. AWS account #3

Development

## OU

Production OU AWS account #4

AWS account #5

![Imagen 35-1](images/clase_8_page35_img1.png)

![Imagen 35-2](images/clase_8_page35_img2.png)

![Imagen 35-3](images/clase_8_page35_img3.png)

![Imagen 35-4](images/clase_8_page35_img4.png)

![Imagen 35-5](images/clase_8_page35_img5.png)

![Imagen 35-6](images/clase_8_page35_img6.png)

![Imagen 35-7](images/clase_8_page35_img7.png)

![Imagen 35-8](images/clase_8_page35_img8.png)

![Imagen 35-9](images/clase_8_page35_img9.png)

![Imagen 35-10](images/clase_8_page35_img10.png)

![Imagen 35-11](images/clase_8_page35_img11.png)

![Imagen 35-12](images/clase_8_page35_img12.png)

![Imagen 35-13](images/clase_8_page35_img13.png)

![Imagen 35-14](images/clase_8_page35_img14.png)

![Imagen 35-15](images/clase_8_page35_img15.png)

![Imagen 35-16](images/clase_8_page35_img16.png)

![Imagen 35-17](images/clase_8_page35_img17.png)

AWS Organizations

Creación de unidades organizativas

AWS Cloud

En la cuenta primaria de

Member accounts

AWS Organizations:

Primary account

AWS account #1

AWS Organizations Internal IT OU

## Crear una jerarquía

de unidades

root

organizativas (OUs).

AWS account #2

Engineering OU

SCP Policy

## Asignar cuentas a las A

OU, como cuentas

miembro. AWS account #3

SCP Policy Development

## OU

## B

## Definir SCP que

aplican restricciones Production OU AWS account #4

SCP Policy

a los permisos de

## C

cuentas específicas.

AWS account #5

![Imagen 36-1](images/clase_8_page36_img1.png)

![Imagen 36-2](images/clase_8_page36_img2.png)

![Imagen 36-3](images/clase_8_page36_img3.png)

![Imagen 36-4](images/clase_8_page36_img4.png)

![Imagen 36-5](images/clase_8_page36_img5.png)

![Imagen 36-6](images/clase_8_page36_img6.png)

![Imagen 36-7](images/clase_8_page36_img7.png)

![Imagen 36-8](images/clase_8_page36_img8.png)

![Imagen 36-9](images/clase_8_page36_img9.png)

![Imagen 36-10](images/clase_8_page36_img10.png)

![Imagen 36-11](images/clase_8_page36_img11.png)

![Imagen 36-12](images/clase_8_page36_img12.png)

![Imagen 36-13](images/clase_8_page36_img13.png)

![Imagen 36-14](images/clase_8_page36_img14.png)

![Imagen 36-15](images/clase_8_page36_img15.png)

![Imagen 36-16](images/clase_8_page36_img16.png)

![Imagen 36-17](images/clase_8_page36_img17.png)

![Imagen 36-18](images/clase_8_page36_img18.png)

![Imagen 36-19](images/clase_8_page36_img19.png)

![Imagen 36-20](images/clase_8_page36_img20.png)

AWS Organizations

Creación de unidades organizativas

AWS Cloud

En la cuenta primaria de

Member accounts

AWS Organizations:

Primary account

AWS account #1

AWS Organizations Internal IT OU

## Crear una jerarquía de

unidades organizativas

root

(OUs).

AWS account #2

Engineering OU

SCP Policy

## Asignar cuentas a las

## A

OU, como cuentas

miembro. AWS account #3

SCP Policy Development

## OU

## B

## Definir SCP que aplican

restricciones a los Production OU AWS account #4

SCP Policy

permisos de cuentas

## C

específicas.

AWS account #5

## Asociar la SPCs a root,

a las OUs o

directamente a las

cuentas.

![Imagen 37-1](images/clase_8_page37_img1.png)

![Imagen 37-2](images/clase_8_page37_img2.png)

![Imagen 37-3](images/clase_8_page37_img3.png)

![Imagen 37-4](images/clase_8_page37_img4.png)

![Imagen 37-5](images/clase_8_page37_img5.png)

![Imagen 37-6](images/clase_8_page37_img6.png)

![Imagen 37-7](images/clase_8_page37_img7.png)

![Imagen 37-8](images/clase_8_page37_img8.png)

![Imagen 37-9](images/clase_8_page37_img9.png)

![Imagen 37-10](images/clase_8_page37_img10.png)

![Imagen 37-11](images/clase_8_page37_img11.png)

![Imagen 37-12](images/clase_8_page37_img12.png)

![Imagen 37-13](images/clase_8_page37_img13.png)

![Imagen 37-14](images/clase_8_page37_img14.png)

![Imagen 37-15](images/clase_8_page37_img15.png)

![Imagen 37-16](images/clase_8_page37_img16.png)

![Imagen 37-17](images/clase_8_page37_img17.png)

![Imagen 37-18](images/clase_8_page37_img18.png)

![Imagen 37-19](images/clase_8_page37_img19.png)

![Imagen 37-20](images/clase_8_page37_img20.png)

AWS Organizations

### Uso de SCP

Control centralizado de los permisos máximos disponibles para todas las cuentas de la

organización

Permite controlar qué servicios son accesibles a los usuarios de IAM en las cuentas

miembros.

Define permisos que afectan a una cuenta completa.

### Define “guardrails”, o establece límites, sobre las acciones que puede delegar un

administrador de una cuenta a los usuarios de esa cuenta. Las políticas de IAM que se

definen en cada cuenta siguen siendo aplicables.

Las SCP no pueden ser modificadas por los administradores locales.

### Buena práctica

### Es más simple definir políticas en una SCP y aplicarlas a múltiples cuentas, que

replicar los permisos en las políticas de IAM de cada una de las cuentas.

![Imagen 38-1](images/clase_8_page38_img1.png)

![Imagen 38-2](images/clase_8_page38_img2.png)

![Imagen 38-3](images/clase_8_page38_img3.png)

![Imagen 38-4](images/clase_8_page38_img4.png)

![Imagen 38-5](images/clase_8_page38_img5.png)

![Imagen 38-6](images/clase_8_page38_img6.png)

AWS Organizations

Uso de SCP

### Ejemplos

### Bloquear el acceso a servicios o acciones específicas. Por ejemplo, denegar el

acceso a que los usuarios deshabiliten AWS CloudTrail en cualquiera de las

cuentas.

Establecer la obligatoriedad de etiquetar los recursos. Por ejemplo, prohibir que

se lancen instancias de EC2 sin un tag específico.

Evitar que las cuentas se desvinculen de la organización.

![Imagen 39-1](images/clase_8_page39_img1.png)

![Imagen 39-2](images/clase_8_page39_img2.png)

![Imagen 39-3](images/clase_8_page39_img3.png)

![Imagen 39-4](images/clase_8_page39_img4.png)

![Imagen 39-5](images/clase_8_page39_img5.png)

![Imagen 39-6](images/clase_8_page39_img6.png)

![Imagen 39-7](images/clase_8_page39_img7.png)

Gestión de permisos de acceso

Uso de SCP - Ejemplos

{

"Version": "2023-06-17",

"Statement": [

{

"Effect": "Deny",

"Action": [ "organizations:LeaveOrganization"],

"Resource": "*"

}

]

}

![Imagen 40-1](images/clase_8_page40_img1.png)

![Imagen 40-2](images/clase_8_page40_img2.png)

![Imagen 40-3](images/clase_8_page40_img3.png)

Gestión de permisos de acceso

SCP combinadas con permisos en IAM

## SCP IAM

- Deny ec2:* ec2 • Allow ec2:*

s3 • Allow s3:*

Permisos reales

![Imagen 41-1](images/clase_8_page41_img1.png)

![Imagen 41-2](images/clase_8_page41_img2.png)

![Imagen 41-3](images/clase_8_page41_img3.png)

![Imagen 41-4](images/clase_8_page41_img4.png)

![Imagen 41-5](images/clase_8_page41_img5.png)

![Imagen 41-6](images/clase_8_page41_img6.png)

![Imagen 41-7](images/clase_8_page41_img7.png)

Gestión de permisos de acceso

Permission boundaries

Esta política de IAM le da al usuario permiso para

Este límite permite el acceso a S3, EC2 y

crear usuarios en IAM

Cloudwatch

{

{

"Version": "2012-10-17",

"Version": "2012-10-17",

"Statement": {

"Statement": [

"Effect": "Allow",

{

"Action":"iam:CreateUser",

"Effect": "Allow",

"Resource": "*"

"Action": [

}

"s3:*",

}

"cloudwatch:*",

IAM user

"ec2:*"

],

"Resource": "*"

}

] El límite no incluye el acceso a IAM, así que la política de

} identidades no podrá asignar al usuario el permiso iam:CreateUser.

![Imagen 42-1](images/clase_8_page42_img1.png)

![Imagen 42-2](images/clase_8_page42_img2.png)

![Imagen 42-3](images/clase_8_page42_img3.png)

![Imagen 42-4](images/clase_8_page42_img4.png)

![Imagen 42-5](images/clase_8_page42_img5.png)

![Imagen 42-6](images/clase_8_page42_img6.png)

![Imagen 42-7](images/clase_8_page42_img7.png)

![Imagen 42-8](images/clase_8_page42_img8.png)

![Imagen 42-9](images/clase_8_page42_img9.png)

### AWS Organizations

Los permisos deben asignarse en ambas políticas

Identity-based policy

iam:CreateUser • Allow iam:CreateUser

### Permissions Boundary S3 • Deny s3*

- Allow s3* ec2:DescribeInstances • Allow ec2:DescribeInstances

- Allow cloudwatch*

- Allow ec2*

Permisos reales

![Imagen 43-1](images/clase_8_page43_img1.png)

![Imagen 43-2](images/clase_8_page43_img2.png)

![Imagen 43-3](images/clase_8_page43_img3.png)

![Imagen 43-4](images/clase_8_page43_img4.png)

![Imagen 43-5](images/clase_8_page43_img5.png)

![Imagen 43-6](images/clase_8_page43_img6.png)

![Imagen 43-7](images/clase_8_page43_img7.png)

![Imagen 43-8](images/clase_8_page43_img8.png)

Gestión de permisos de acceso

### Combinación de políticas

SCP asociada a la OU “Test” Política IAM basada en identidades

### Permission boundary

- Deny ec2* • Allow ec2:DescribeInstances

- Allow s3*

- Allow kms*

- Deny sqs*

- Allow sqs*

- Allow s3*

- Allow sqs:SendMessage

IAM user in test OU

### Recurso o acceso ¿Puede? ¿Por qué?

Describir las instancias de No La SCP deniega el acceso a EC2. Esto prevalence sobre la política IAM

## EC2

AWS Key Management No No está denegado explícitamente, pero el servicio no está incluido en el permission

Service (AWS KMS) boundary.

Amazon S3 Yes S3 está dentro del permission boundary y no está denegado explícitamente en la SCP.

La política IAM asigna acceso al recurso.

Mandar un mensaje de No El deny explícito en la SCP tiene prioridad sobre los otros dos permisos.

Amazon SQS

![Imagen 44-1](images/clase_8_page44_img1.png)

![Imagen 44-2](images/clase_8_page44_img2.png)

![Imagen 44-3](images/clase_8_page44_img3.png)

![Imagen 44-4](images/clase_8_page44_img4.png)

Gestión de permisos de acceso

Combinación de políticas

### Permission boundaries SCP organizacionales

### Aplica a una entidad de IAM (rol o usuario) Aplica a todos los miembros de una organización

Define los máximos permisos que se le podrían asignar Define los máximos permisos que podrían asignarse en una

a esa entidad organización, una OU o una cuenta dentro de la

organización.

### No asignan permisos No asignan permisos

Se usan para definir los recursos habilitados para un Se suelen usar para denegar el acceso a un conjunto de

usuario o rol recursos

Ejemplo: permitir que el rol “Dev” acceda a EC2, S3 y Ej: Denegar el acceso a RDS a todos los miembros de la OU

### CloudWatch. “Internal IT”

Resultado: el rol de desarrollador solo puede acceder a Resultado: todos los miembros de esa OU tendrán

esos servicios, con independencia del resto de los prohibido el acceso a RDS, aunque otras políticas les den

permisos que tenga. permisos.

![Imagen 45-1](images/clase_8_page45_img1.png)

![Imagen 45-2](images/clase_8_page45_img2.png)

![Imagen 45-3](images/clase_8_page45_img3.png)

AWS Control Tower

Facilita la implementación y la gestión de un

entorno multi-cuentas seguro dentro de AWS.

Permite:

- Automatizar la implementación de un entorno

multi-cuenta que aplique el WAF.

### AWS Control

- Gestionar las reglas de seguridad, operación y

Tower

compliance de las cuentas.

- Brinda guías para gobernar el entorno de AWS a

escala.

![Imagen 46-1](images/clase_8_page46_img1.png)

![Imagen 46-2](images/clase_8_page46_img2.png)

![Imagen 46-3](images/clase_8_page46_img3.png)

![Imagen 46-4](images/clase_8_page46_img4.png)

Múltiples cuentas en AWS

### Resumen

Es frecuente encontrar organizaciones que crean múltiples cuentas de AWS y definen

una VPC en cada una.

Se pueden agrupar cuentas para consolidar la facturación.

Este esquema permite separar distintos recursos y establecer controles de seguridad.

AWS Organizations permite consolidar múltiples cuentas de AWS para gestionarlas

centralizadamente.

Las SCPs permiten establecer límites de permisos en el nivel de la organización.

Los permissions boundaries permiten definir límites para las entidades de IAM (usuarios y

roles)

Los grupos o usuarios pueden tener múltiples políticas asociadas. Se aplica la más

restrictiva.

![Imagen 47-1](images/clase_8_page47_img1.png)

![Imagen 47-2](images/clase_8_page47_img2.png)

![Imagen 47-3](images/clase_8_page47_img3.png)

Cifrado de datos en reposo

Seguridad de usuarios, aplicaciones y datos

![Imagen 48-1](images/clase_8_page48_img1.png)

![Imagen 48-2](images/clase_8_page48_img2.png)

![Imagen 48-3](images/clase_8_page48_img3.png)

Protección de datos en reposo

Objetivos

Asegurar la confidencialidad e

integridad de la información

Brindar una capa extra de

protección si un Sistema está

Seguridad de la

comprometido

información

Disponibilidad

![Imagen 49-1](images/clase_8_page49_img1.png)

![Imagen 49-2](images/clase_8_page49_img2.png)

![Imagen 49-3](images/clase_8_page49_img3.png)

Cifrado de datos

Proceso

Key

Plaintext data Encryption process Ciphertext

![Imagen 50-1](images/clase_8_page50_img1.png)

![Imagen 50-2](images/clase_8_page50_img2.png)

![Imagen 50-3](images/clase_8_page50_img3.png)

![Imagen 50-4](images/clase_8_page50_img4.png)

![Imagen 50-5](images/clase_8_page50_img5.png)

![Imagen 50-6](images/clase_8_page50_img6.png)

![Imagen 50-7](images/clase_8_page50_img7.png)

![Imagen 50-8](images/clase_8_page50_img8.png)

![Imagen 50-9](images/clase_8_page50_img9.png)

![Imagen 50-10](images/clase_8_page50_img10.png)

Cifrado de datos

Simétrico

Encrypt Encrypted

file

Usa la misma clave para

Unencrypted

cifrar y descifrar los datos

file

Más rápido y eficiente

para volúmenes grandes

Key

Muy difundido y

generalmente aceptado

Encrypted

Decrypt

file

Unencrypted

file

![Imagen 51-1](images/clase_8_page51_img1.png)

![Imagen 51-2](images/clase_8_page51_img2.png)

![Imagen 51-3](images/clase_8_page51_img3.png)

![Imagen 51-4](images/clase_8_page51_img4.png)

![Imagen 51-5](images/clase_8_page51_img5.png)

![Imagen 51-6](images/clase_8_page51_img6.png)

![Imagen 51-7](images/clase_8_page51_img7.png)

![Imagen 51-8](images/clase_8_page51_img8.png)

![Imagen 51-9](images/clase_8_page51_img9.png)

Cifrado de datos

Simétrico

Encrypt Encrypted

Casos de uso file

Unencrypted

Cuando se priorizan la velocidad file

y el costo.

Para cifrar grandes volúmenes.

Key

Si los datos no salen de los límites

Decrypt Encrypted

de la organización.

file

Unencrypted

file

![Imagen 52-1](images/clase_8_page52_img1.png)

![Imagen 52-2](images/clase_8_page52_img2.png)

![Imagen 52-3](images/clase_8_page52_img3.png)

![Imagen 52-4](images/clase_8_page52_img4.png)

![Imagen 52-5](images/clase_8_page52_img5.png)

![Imagen 52-6](images/clase_8_page52_img6.png)

![Imagen 52-7](images/clase_8_page52_img7.png)

![Imagen 52-8](images/clase_8_page52_img8.png)

![Imagen 52-9](images/clase_8_page52_img9.png)

Cifrado de datos

Asimétrico

Usa un par de claves (pública y

Encrypt Encrypted

privada).

file

Unencrypted

Considerado más seguro.

file

Más lento que el cifrado

simétrico.

Public Private

key key

Casos de uso

Cuando la información sale de la

organización

Encrypted

Decrypt

file

No-repudio

Unencrypted

Motivos regulatorios file

![Imagen 53-1](images/clase_8_page53_img1.png)

![Imagen 53-2](images/clase_8_page53_img2.png)

![Imagen 53-3](images/clase_8_page53_img3.png)

![Imagen 53-4](images/clase_8_page53_img4.png)

![Imagen 53-5](images/clase_8_page53_img5.png)

![Imagen 53-6](images/clase_8_page53_img6.png)

![Imagen 53-7](images/clase_8_page53_img7.png)

![Imagen 53-8](images/clase_8_page53_img8.png)

![Imagen 53-9](images/clase_8_page53_img9.png)

![Imagen 53-10](images/clase_8_page53_img10.png)

![Imagen 53-11](images/clase_8_page53_img11.png)

![Imagen 53-12](images/clase_8_page53_img12.png)

![Imagen 53-13](images/clase_8_page53_img13.png)

![Imagen 53-14](images/clase_8_page53_img14.png)

![Imagen 53-15](images/clase_8_page53_img15.png)

![Imagen 53-16](images/clase_8_page53_img16.png)

![Imagen 53-17](images/clase_8_page53_img17.png)

![Imagen 53-18](images/clase_8_page53_img18.png)

Cifrado de datos

1

4

Plaintext Data key Encrypted

item item

2

Data key key-encryption key Encrypted data

1 key

## Cifrar el elemento con una clave (data key).

3

## Utilizar otra clave para cifrar la data key (key-

encryption key).

## Continuar “envolviedo” una clave de cifrado con otra Encrypted key-encryption Encrypted

hasta llegar al número de capas estipulado. data key key 2 key-encryption key 1

## Almacenar la clave de cifrado junto con el ítem cifrado.

![Imagen 54-1](images/clase_8_page54_img1.png)

![Imagen 54-2](images/clase_8_page54_img2.png)

![Imagen 54-3](images/clase_8_page54_img3.png)

![Imagen 54-4](images/clase_8_page54_img4.png)

![Imagen 54-5](images/clase_8_page54_img5.png)

![Imagen 54-6](images/clase_8_page54_img6.png)

![Imagen 54-7](images/clase_8_page54_img7.png)

![Imagen 54-8](images/clase_8_page54_img8.png)

![Imagen 54-9](images/clase_8_page54_img9.png)

![Imagen 54-10](images/clase_8_page54_img10.png)

![Imagen 54-11](images/clase_8_page54_img11.png)

![Imagen 54-12](images/clase_8_page54_img12.png)

![Imagen 54-13](images/clase_8_page54_img13.png)

![Imagen 54-14](images/clase_8_page54_img14.png)

![Imagen 54-15](images/clase_8_page54_img15.png)

![Imagen 54-16](images/clase_8_page54_img16.png)

![Imagen 54-17](images/clase_8_page54_img17.png)

![Imagen 54-18](images/clase_8_page54_img18.png)

![Imagen 54-19](images/clase_8_page54_img19.png)

![Imagen 54-20](images/clase_8_page54_img20.png)

![Imagen 54-21](images/clase_8_page54_img21.png)

![Imagen 54-22](images/clase_8_page54_img22.png)

![Imagen 54-23](images/clase_8_page54_img23.png)

![Imagen 54-24](images/clase_8_page54_img24.png)

![Imagen 54-25](images/clase_8_page54_img25.png)

![Imagen 54-26](images/clase_8_page54_img26.png)

![Imagen 54-27](images/clase_8_page54_img27.png)

![Imagen 54-28](images/clase_8_page54_img28.png)

### Cifrado de datos en reposo

### Cifrado del lado del cliente (CSE) Cifrado del lado del servidor (SSE)

La aplicación cifra los datos AWS cifra los datos una vez que

antes de mandarlos a AWS. los recibe.

### Los servicios cifran los datos antes

### El cliente crea y administra sus de grabarlos en disco y los

propias claves de cifrado. descifran de manera transparente

en cada acceso.

### Las claves y los algoritmos solo Las claves pueden ser

son conocidos por el cliente. administradas por AWS.

![Imagen 55-1](images/clase_8_page55_img1.png)

![Imagen 55-2](images/clase_8_page55_img2.png)

![Imagen 55-3](images/clase_8_page55_img3.png)

Cifrado de datos en reposo

Del lado del cliente

Corporate data center AWS Cloud

Key

Unencrypte Client encryption Encrypted

d data software data

Amazon S3

bucket

![Imagen 56-1](images/clase_8_page56_img1.png)

![Imagen 56-2](images/clase_8_page56_img2.png)

![Imagen 56-3](images/clase_8_page56_img3.png)

![Imagen 56-4](images/clase_8_page56_img4.png)

![Imagen 56-5](images/clase_8_page56_img5.png)

![Imagen 56-6](images/clase_8_page56_img6.png)

![Imagen 56-7](images/clase_8_page56_img7.png)

![Imagen 56-8](images/clase_8_page56_img8.png)

![Imagen 56-9](images/clase_8_page56_img9.png)

![Imagen 56-10](images/clase_8_page56_img10.png)

![Imagen 56-11](images/clase_8_page56_img11.png)

![Imagen 56-12](images/clase_8_page56_img12.png)

![Imagen 56-13](images/clase_8_page56_img13.png)

Cifrado de datos en reposo

Del lado del servidor

Corporate data AWS Cloud

center

Unencrypte Amazon S3 Encrypted

d data data

Amazon

S3 bucket

Key

## AWS KMS

![Imagen 57-1](images/clase_8_page57_img1.png)

![Imagen 57-2](images/clase_8_page57_img2.png)

![Imagen 57-3](images/clase_8_page57_img3.png)

![Imagen 57-4](images/clase_8_page57_img4.png)

![Imagen 57-5](images/clase_8_page57_img5.png)

![Imagen 57-6](images/clase_8_page57_img6.png)

![Imagen 57-7](images/clase_8_page57_img7.png)

![Imagen 57-8](images/clase_8_page57_img8.png)

![Imagen 57-9](images/clase_8_page57_img9.png)

![Imagen 57-10](images/clase_8_page57_img10.png)

![Imagen 57-11](images/clase_8_page57_img11.png)

![Imagen 57-12](images/clase_8_page57_img12.png)

![Imagen 57-13](images/clase_8_page57_img13.png)

![Imagen 57-14](images/clase_8_page57_img14.png)

### AWS Key Management System (KMS)

Permite crear y administrar claves criptográficas.

Usa módulos de seguridad por hardware (HSM) para

proteger las claves

Se integra con otros servicios de AWS

## AWS KMS

Permite establecer políticas de uso para determinar

qué usuarios pueden emplear las claves.

![Imagen 58-1](images/clase_8_page58_img1.png)

![Imagen 58-2](images/clase_8_page58_img2.png)

![Imagen 58-3](images/clase_8_page58_img3.png)

![Imagen 58-4](images/clase_8_page58_img4.png)

AWS Key Management System (KMS)

Claves Operaciones

Gestionadas por el cliente Encrypt

Gestionadas por KMS Decrypt

Data key (symmetric) GenerateDataKey

Data key pair (asymmetric) GenerateDataKeyPair

![Imagen 59-1](images/clase_8_page59_img1.png)

![Imagen 59-2](images/clase_8_page59_img2.png)

![Imagen 59-3](images/clase_8_page59_img3.png)

AWS Key Management System (KMS)

Integraciones

Amazon Simple Storage Service (Amazon S3)

Amazon Elastic Block Store (Amazon EBS)

### Importante

Los servicios integrados con AWS KMS solamente usan claves

simétricas.

![Imagen 60-1](images/clase_8_page60_img1.png)

![Imagen 60-2](images/clase_8_page60_img2.png)

![Imagen 60-3](images/clase_8_page60_img3.png)

![Imagen 60-4](images/clase_8_page60_img4.png)

![Imagen 60-5](images/clase_8_page60_img5.png)

AWS Key Management System (KMS)

Ejemplo de cifrado con S3

1 2

## AWS KMS

User

S3 bucket

3

with

Encrypts

objects

5

Customer Plaintext

managed data key

key

4

![Imagen 61-1](images/clase_8_page61_img1.png)

![Imagen 61-2](images/clase_8_page61_img2.png)

![Imagen 61-3](images/clase_8_page61_img3.png)

![Imagen 61-4](images/clase_8_page61_img4.png)

![Imagen 61-5](images/clase_8_page61_img5.png)

![Imagen 61-6](images/clase_8_page61_img6.png)

![Imagen 61-7](images/clase_8_page61_img7.png)

![Imagen 61-8](images/clase_8_page61_img8.png)

![Imagen 61-9](images/clase_8_page61_img9.png)

![Imagen 61-10](images/clase_8_page61_img10.png)

![Imagen 61-11](images/clase_8_page61_img11.png)

![Imagen 61-12](images/clase_8_page61_img12.png)

![Imagen 61-13](images/clase_8_page61_img13.png)

AWS Key Management System (KMS)

Ejemplo de descifrado con S3

1 2

## AWS KMS

User

S3 bucket

5

4

with objects

Decrypts

Customer Plaintext

managed data key

key

3

![Imagen 62-1](images/clase_8_page62_img1.png)

![Imagen 62-2](images/clase_8_page62_img2.png)

![Imagen 62-3](images/clase_8_page62_img3.png)

![Imagen 62-4](images/clase_8_page62_img4.png)

![Imagen 62-5](images/clase_8_page62_img5.png)

![Imagen 62-6](images/clase_8_page62_img6.png)

![Imagen 62-7](images/clase_8_page62_img7.png)

![Imagen 62-8](images/clase_8_page62_img8.png)

AWS Key Management System (KMS)

Ejemplo de integración con Amazon EBS

## AWS KMS

La clave se guarda

EBS volume

1 junto con los datos

cifrados.

El host de EC2

Encrypted

recupera la

data key

data key

La clave descifrada en

cifrada.

2 4 memoria se usa para

cifrar/descifrar los datos.

Encrypts

Customer Data

Se hace una solicitud a

Server 3 managed key

## AWS KMS, AWS KMS

key

descifra y devuelve la

clave de datos.

![Imagen 63-1](images/clase_8_page63_img1.png)

![Imagen 63-2](images/clase_8_page63_img2.png)

![Imagen 63-3](images/clase_8_page63_img3.png)

![Imagen 63-4](images/clase_8_page63_img4.png)

![Imagen 63-5](images/clase_8_page63_img5.png)

![Imagen 63-6](images/clase_8_page63_img6.png)

![Imagen 63-7](images/clase_8_page63_img7.png)

![Imagen 63-8](images/clase_8_page63_img8.png)

![Imagen 63-9](images/clase_8_page63_img9.png)

![Imagen 63-10](images/clase_8_page63_img10.png)

![Imagen 63-11](images/clase_8_page63_img11.png)

![Imagen 63-12](images/clase_8_page63_img12.png)

![Imagen 63-13](images/clase_8_page63_img13.png)

![Imagen 63-14](images/clase_8_page63_img14.png)

Múltiples cuentas en AWS

### Resumen

El cifrado de datos en reposo reduce los riesgos de compromiso de datos, incluso cuando un

endpoint está comprometido.

El cifrado simétrico usa la misma clave para cifrar y descifrar los datos.

El cifrado asimétrico usa un par de claves: la pública para cifrar, la privada para descifrar.

El ensobrado es una práctica de cifrar texto plano con una clave de datos y luego cifrar la

clave de datos con otra clave.

### Con cifrado del lado del cliente, la aplicación cifra los datos localmente antes de enviarlos a

AWS. La propia aplicación tiene que descifrarlos una vez que los recibe.

El cifrado del lado del servidor consiste en que la aplicación o el servicio que recibe los datos los

cifra antes de grabarlos y los descifra cuando los recupera.

Las claves AWS KMS son el principal recurso de AWS KMS. Se usan para cifrar y descifrar datos.

![Imagen 64-1](images/clase_8_page64_img1.png)

![Imagen 64-2](images/clase_8_page64_img2.png)

![Imagen 64-3](images/clase_8_page64_img3.png)

Servicios de seguridad de AWS

Seguridad de usuarios, aplicaciones y datos

![Imagen 65-1](images/clase_8_page65_img1.png)

![Imagen 65-2](images/clase_8_page65_img2.png)

![Imagen 65-3](images/clase_8_page65_img3.png)

Servicios de AWS para seguridad

Categoría Descripción Ejemplos

AWS Identity and Access Management (IAM)

Gestión de

### AWS IAM Identity Center

identidades y Administrar identidades, recursos y permisos.

Amazon Cognito

accesos

AWS Organizations

AWS CloudTrail

Mejorar la postura de seguridad y aplicar las

Detección y Amazon Detective

operaciones de seguridad en un entorno completo de

respuesta Amazon Inspector

## AWS.

AWS Security Hub

### Protección de AWS Network Firewall

Aplicar políticas de seguridad granulares y puntos de

redes y AWS Shield

control de red en toda la organización.

aplicaciones AWS WAF

### AWS Key Management System (AWS KMS)

Protección de Proteger los datos, las cuentas y las cargas de trabajo

AWS Secrets Manager

datos para evitar accesos no autorizados.

Amazon Macie

### Obtener una visión general del cumplimiento y

monitorear continuamente chequeos automáticos AWS Artifact

### Compliance

basados en buenas prácticas de AWS y estándares de la AWS Audit Manager

industria..

![Imagen 66-1](images/clase_8_page66_img1.png)

![Imagen 66-2](images/clase_8_page66_img2.png)

![Imagen 66-3](images/clase_8_page66_img3.png)

### Servicios de AWS para seguridad

Defender el perímetro Proteger los datos Detectar y responder a amenazas

AWS WAF and AWS Amazon Macie Amazon Inspector

Shield

Amazon Detective

AWS Security Hub

![Imagen 67-1](images/clase_8_page67_img1.png)

![Imagen 67-2](images/clase_8_page67_img2.png)

![Imagen 67-3](images/clase_8_page67_img3.png)

![Imagen 67-4](images/clase_8_page67_img4.png)

![Imagen 67-5](images/clase_8_page67_img5.png)

![Imagen 67-6](images/clase_8_page67_img6.png)

![Imagen 67-7](images/clase_8_page67_img7.png)

![Imagen 67-8](images/clase_8_page67_img8.png)

![Imagen 67-9](images/clase_8_page67_img9.png)

![Imagen 67-10](images/clase_8_page67_img10.png)

![Imagen 67-11](images/clase_8_page67_img11.png)

## AWS WAF

### Descripción Características Ejemplos

### Es un Web Application Se pueden usar reglas Bloquear los

### Firewall que permite administradas o requerimientos que no

monitorear las solicitudes gestionadas. tienen el encabezado

de HTTP y HTTPS que se User-Agent de HTTP.

Se pueden permitir o

reenvían a los recursos

bloquear requerimientos en Detectar y administra

protegidos de la

función de diversos criterios intentos maliciosos de

aplicación del cliente.

(dirección IP, país de origen, creación de cuentas en la

encabezados). página de sign-up de la

aplicación.

AWS Shield permite reducir

el impacto de ataques de

(DDoS).

![Imagen 68-1](images/clase_8_page68_img1.png)

![Imagen 68-2](images/clase_8_page68_img2.png)

![Imagen 68-3](images/clase_8_page68_img3.png)

![Imagen 68-4](images/clase_8_page68_img4.png)

AWS Macie

### Descripción Características Ejemplos

### Es servicio de seguridad Automatizar el Macie permite identificar

que descubre los datos descubrimiento de datos datos sensibles cuando se

sensibles almacenados en los migra a Amazon S3.

Permite crear y ejecutar jobs

Amazon S3.

de descubrimiento de datos Esto permite notificar a un

Aplica machine learning, administrador y decidir si

Se pueden usar etiquetas

provee visibilidad de los se permite que siga

estandarizadas o

riesgos sobre los daos y copiando datos a S3.

personalizadas.

permite protegerse de

esos riesgos. Permite revisar, analizar y

gestionar los hallazgos.

![Imagen 69-1](images/clase_8_page69_img1.png)

![Imagen 69-2](images/clase_8_page69_img2.png)

![Imagen 69-3](images/clase_8_page69_img3.png)

![Imagen 69-4](images/clase_8_page69_img4.png)

AWS Inspector

Descripción Características Ejemplos

Se puede usar AWS

Servicio de gestión de Escanear las AMI de EC2 y

Organizations para centralizar

vulnerabilidades que generar los reportes de

la administración.

escanea las cargas de hallazgos en AWS

trabajo para identificar Inspector Risk score permite Inspector para asegurar

vulnerabilidades y evaluar vulnerabilidades que se actualice antes de

exposiciones no deseadas la implementación.

El dashboard de Amazon

a la red.

Inspector permite identificar

Detecta y escanea hallazgos de alto impacto.

instancias de EC2,

Los hallazgos se pueden

contenedores de ECR y

publicar en Amazon

funciones lambda.

EventBridge para integrarse

con otros servicios

![Imagen 70-1](images/clase_8_page70_img1.png)

![Imagen 70-2](images/clase_8_page70_img2.png)

![Imagen 70-3](images/clase_8_page70_img3.png)

![Imagen 70-4](images/clase_8_page70_img4.png)

AWS Detective

### Descripción Características Ejemplos

### Permite visualizar los datos en

Ayuda a analizar, investigar Investigación de incidente

modo de grafo que resumen

e identificar la causa raíz de vinculado con una

la información de contexto y

los hallazgos o de las entidad IAM.

datos de comportamiento.

actividades sospechosas.

Validar, comparar y

Recolecta

correlacionar los datos para

automáticamente datos de

hacer análisis

log de distintas fuentes.

Obtener y analizar

Usa machine learning,

automáticamente los datos

análisis estadístico y teoría

relevantes de todas las

de grafos para generar

cuentas habilitadas.

visualizaciones que mejoran

las capacidades de

investigación

![Imagen 71-1](images/clase_8_page71_img1.png)

![Imagen 71-2](images/clase_8_page71_img2.png)

![Imagen 71-3](images/clase_8_page71_img3.png)

![Imagen 71-4](images/clase_8_page71_img4.png)

AWS Security Hub

Descripción Características Ejemplos

Priorizar los esfuerzos de

Recolecta datos de Soporta múltiples estándares

respuesta y remediación

de seguridad

seguridad de todas las

de los equipos de

cuentas, servicios de AWS, y

### Recibe hallazgos de otros seguridad mediante la

de productos de terceros servicios, como Amazon búsqueda, correlación y

soportados. Macie y Amazon Inspector. agregación de hallazgos

de distintas cuentas y

Permite analizar las Se pueden aplicar reglas de

recursos.

automatización para

tendencias de seguridad e

actualizar automáticamente

identificar problemas de

los hallazgos críticos.

seguridad de alta prioridad.

![Imagen 72-1](images/clase_8_page72_img1.png)

![Imagen 72-2](images/clase_8_page72_img2.png)

![Imagen 72-3](images/clase_8_page72_img3.png)

![Imagen 72-4](images/clase_8_page72_img4.png)

### AWS Trusted Advisor

Genera recomendaciones basadas en 5 categorías de las buenas

prácticas.

Evalúa la cuenta para sugerir mejoras y optimizaciones para los

recursos.

Se accede desde la consola de AWS y está disponible para todos

los niveles de soporte.

### Trusted

La consola de Trusted Advisor permite ver los controles y los

### Advisor

hallazgos de seguridad si se habilita Security Hub.

![Imagen 73-1](images/clase_8_page73_img1.png)

![Imagen 73-2](images/clase_8_page73_img2.png)

![Imagen 73-3](images/clase_8_page73_img3.png)

![Imagen 73-4](images/clase_8_page73_img4.png)

Servicios de seguridad de AWS

### Resumen

Los servicios de seguridad de AWS permiten implementar una estrategia de defensa en

profundidad para las cargas de trabajo de AWS.

Los servicios de seguridad de AWS incluyen:

- AWS WAF. Monitoreo de requerimientos web

- Amazon Macie. Identificación de datos sensibles en Amazon S3

- Amazon Inspector. Identificación de vulnerabilidades en instancias EC2, contenedores y

funciones lambda

- Amazon Detective. Análisis, investigación e identificación de la causa raíz de actividades

sospechosas o hallazgos de seguridad

- AWS Security Hub. Consolidar automáticamente los hallazgos y monitorear la postura de

seguridad respecto de las buenas prácticas.

AWS Trusted Advisor inspecciona el entorno de AWS y hace recomendaciones para cerrar los

gaps de seguridad.

![Imagen 74-1](images/clase_8_page74_img1.png)

![Imagen 74-2](images/clase_8_page74_img2.png)

![Imagen 74-3](images/clase_8_page74_img3.png)

Módulo 9

### Resumen

Uso de AWS Identity and Access Management (IAM) para administrar

permisos.

Federación de identidades para aumentar la seguridad.

Describir cómo administrar múltiples cuentas de AWS.

Reconocer cómo contribuyen las service control policies (SCPs) a la

seguridad.

Cifrar datos en reposo con AWS KMS.

Identificar los servicios de seguridad de AWS apropiados para cada

caso.

![Imagen 75-1](images/clase_8_page75_img1.png)

![Imagen 75-2](images/clase_8_page75_img2.png)

![Imagen 75-3](images/clase_8_page75_img3.png)

### Ejemplo de pregunta

Create a service control policy (SCP) to deny all actions on all AWS services except for the

## A

Amazon EC2 and Amazon RDS services, and attach it to the Tester role in both accounts.

Create an AWS Identity and Access Management (IAM) policy with the required EC2 and RDS

## B

permissions, and attach it to the organizational unit.

Create a service control policy (SCP) to deny all actions on all AWS services except for the

## C

Amazon EC2 and Amazon RDS services, and attach it to the organizational unit.

Create an AWS Identity and Access Management (IAM) policy in both accounts with the required

## D

EC2 and RDS permissions, and attach it to the Tester role.

Create a service control policy (SCP) in both accounts with the required EC2 and RDS

## E

permissions, and attach it to the Tester role.

![Imagen 76-1](images/clase_8_page76_img1.png)

![Imagen 76-2](images/clase_8_page76_img2.png)

![Imagen 76-3](images/clase_8_page76_img3.png)

![Imagen 76-4](images/clase_8_page76_img4.png)

### Ejemplo de pregunta

Create a service control policy (SCP) to deny all actions on all AWS services except for the

## A

Amazon EC2 and Amazon RDS services, and attach it to the Tester role in both accounts.

Create an AWS Identity and Access Management (IAM) policy with the required EC2 and RDS

## B

permissions, and attach it to the organizational unit.

Create a service control policy (SCP) to deny all actions on all AWS services except for the

## C

Amazon EC2 and Amazon RDS services, and attach it to the organizational unit.

Create an AWS Identity and Access Management (IAM) policy in both accounts with the required

## D

EC2 and RDS permissions, and attach it to the Tester role.

Create a service control policy (SCP) in both accounts with the required EC2 and RDS

## E

permissions, and attach it to the Tester role.

![Imagen 77-1](images/clase_8_page77_img1.png)

![Imagen 77-2](images/clase_8_page77_img2.png)

![Imagen 77-3](images/clase_8_page77_img3.png)

![Imagen 77-4](images/clase_8_page77_img4.png)

Muchas gracias.

www.austral.edu.ar

![Imagen 78-1](images/clase_8_page78_img1.png)

![Imagen 78-2](images/clase_8_page78_img2.png)

![Imagen 78-3](images/clase_8_page78_img3.png)
