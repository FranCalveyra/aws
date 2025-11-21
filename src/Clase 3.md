# Clase 3

## Capa de almacenamiento

Amazon S3

![Imagen 2-1](images/clase_3_page2_img1.png)

![Imagen 2-2](images/clase_3_page2_img2.png)

![Imagen 2-3](images/clase_3_page2_img3.png)

Tipos de almacenamiento

### Bloques Archivos Objetos

### Los datos se

Los datos se Los datos se

almacenan en

almacenan en una almacenan como

bloques de tamaño

estructura jerárquica objetos, basados en

fijo

atributos y

metadatos.

![Imagen 3-1](images/clase_3_page3_img1.png)

![Imagen 3-2](images/clase_3_page3_img2.png)

![Imagen 3-3](images/clase_3_page3_img3.png)

![Imagen 3-4](images/clase_3_page3_img4.png)

![Imagen 3-5](images/clase_3_page3_img5.png)

![Imagen 3-6](images/clase_3_page3_img6.png)

### Amazon S3

Almacena enormes cantidades (ilimitadas) de datos no

estructurados.

Almacena archivos como objetos en un bucket que nosotros

definimos.

El tamaño máximo de un archivo en un único objeto es de 5 TB.

Los objetos tienen una URL única a nivel global (namespace

universal).

Los objetos tienen una clave, un ID de versión, un valor,

metadatos y subrecursos.

![Imagen 4-1](images/clase_3_page4_img1.png)

![Imagen 4-2](images/clase_3_page4_img2.png)

![Imagen 4-3](images/clase_3_page4_img3.png)

![Imagen 4-4](images/clase_3_page4_img4.png)

### Amazon S3

Un bucket es un contenedor de objetos.

Bucket Cada bucket tiene un nombre único y un endpoint vinculado con una región específica.

https://s3-<aws-region>.amazonaws.com/<bucket-name>/<object-key >

### Objeto

Un objeto es un archivo junto con los metadatos que lo describen.

Los metadatos son un conjunto de pares nombre-valor que se asignan cuando se carga el objeto.

Un objeto incluye un nombre (object-key) que lo identifica de manera única.

![Imagen 5-1](images/clase_3_page5_img1.png)

![Imagen 5-2](images/clase_3_page5_img2.png)

![Imagen 5-3](images/clase_3_page5_img3.png)

![Imagen 5-4](images/clase_3_page5_img4.png)

![Imagen 5-5](images/clase_3_page5_img5.png)

![Imagen 5-6](images/clase_3_page5_img6.png)

![Imagen 5-7](images/clase_3_page5_img7.png)

![Imagen 5-8](images/clase_3_page5_img8.png)

![Imagen 5-9](images/clase_3_page5_img9.png)

![Imagen 5-10](images/clase_3_page5_img10.png)

![Imagen 5-11](images/clase_3_page5_img11.png)

![Imagen 5-12](images/clase_3_page5_img12.png)

Amazon S3

### Uso de prefijos

Estos objetos están en un bucket que se llama graphics-bucket.

Una consulta GET con el prefijo

photos/2022/catpiano.jpg

photos/2022 devuelve:

photos/2022/catonphone.jpg

photos/2022/ninepuppies.png

photos/2021/lakefront.png graphics-

photos/2021/coveredbridge.png bucket/photos/2022/catpiano.jpg

photos/2021/openairmarket.jpg graphics-

video-source/9984.mp4 bucket/photos/2022/catonphone.jpg

video-source/9918.mp4 graphics-

video-source/18446.mp4 bucket/photos/2022/ninepuppies.png

![Imagen 6-1](images/clase_3_page6_img1.png)

![Imagen 6-2](images/clase_3_page6_img2.png)

Amazon S3

Ventajas

Durabilidad Disponibilidad Alta performance

Acceso a los datos a

Ayuda a evitar la

demanda Ejecuta miles de

pérdida de datos

transacciones por

Capacidad ilimitada de

Provee (upload/retrieve)

almacenamiento

almacenamiento

Escala automáticamente

estándar con 11 nueves S3 estándar con

cuando aumentan las

(99.999999999 %) de

4 nueves (99.99%) de solicitudes

durabilidad

disponibilidad

![Imagen 7-1](images/clase_3_page7_img1.png)

![Imagen 7-2](images/clase_3_page7_img2.png)

![Imagen 7-3](images/clase_3_page7_img3.png)

![Imagen 7-4](images/clase_3_page7_img4.png)

![Imagen 7-5](images/clase_3_page7_img5.png)

Amazon S3

Posibles casos de uso

Picos en la Recuperación

Sitios estáticos Análisis financiero

demanda ante desastres

### Almacenar Almacenar un Almacenar Guardar datos

contenido web sitio estático, datos que otros de resguardo o

que necesita formado por servicios pueden brindar soporte

ancho de archivos HTML, usar para hacer a la

banda para imágenes y análisis. recuperación.

videos.

tolerar picos

extremos de

demanda.

![Imagen 8-1](images/clase_3_page8_img1.png)

![Imagen 8-2](images/clase_3_page8_img2.png)

![Imagen 8-3](images/clase_3_page8_img3.png)

![Imagen 8-4](images/clase_3_page8_img4.png)

![Imagen 8-5](images/clase_3_page8_img5.png)

![Imagen 8-6](images/clase_3_page8_img6.png)

![Imagen 8-7](images/clase_3_page8_img7.png)

Amazon S3

### Almacenamiento de objetos

- La cantidad de objetos que puede contener un bucket es ilimitada.

- Para subir un archive se requieren permisos de escritura sobre un bucket.

- Los objetos están cifrados por default:

- Los objetos se cifran automáticamente usando cifrado del lado del

servidor.

- Durante la descarga, se descifran los objetos.

![Imagen 9-1](images/clase_3_page9_img1.png)

![Imagen 9-2](images/clase_3_page9_img2.png)

![Imagen 9-3](images/clase_3_page9_img3.png)

Amazon S3

Almacenamiento de objetos

Medio Descripción

## AWS

Basado en un wizard para subir y bajar datos de S3, incluyendo la opción de

Management

drag &drop (tamaño máximo 160 GB).

Console

### AWS Command

Line Interface Se aplica por un comando desde una terminal o una llamada desde un script.

## (AWS CLI)

AWS SDKs Se use el AWS SDKs para manejar objetos por programa

### Amazon S3 REST

Una solicitud PUT permite subir objetos en una sola operación.

## API

![Imagen 10-1](images/clase_3_page10_img1.png)

![Imagen 10-2](images/clase_3_page10_img2.png)

![Imagen 10-3](images/clase_3_page10_img3.png)

Amazon S3

Multipart upload

AWS Cloud

2

1 3

S3 bucket

Object Object parts Reassembled object

Ventajas:

- Mayor rendimiento.

- Rápida recuperación ante fallas de red.

- Capacidad de pausar y reiniciar.

- Se puede empezar a subir un archive antes de conocer el tamaño

final del objeto.

![Imagen 11-1](images/clase_3_page11_img1.png)

![Imagen 11-2](images/clase_3_page11_img2.png)

![Imagen 11-3](images/clase_3_page11_img3.png)

![Imagen 11-4](images/clase_3_page11_img4.png)

![Imagen 11-5](images/clase_3_page11_img5.png)

![Imagen 11-6](images/clase_3_page11_img6.png)

![Imagen 11-7](images/clase_3_page11_img7.png)

![Imagen 11-8](images/clase_3_page11_img8.png)

![Imagen 11-9](images/clase_3_page11_img9.png)

![Imagen 11-10](images/clase_3_page11_img10.png)

Amazon S3

Transfer Acceleration

Without S3 Transfer Acceleration

Ventajas:

AWS Cloud

### Internet

- Transferencias rápidas y

seguras en distancias largas.

Any file types

### S3 bucket • Optimiza las velocidades de

With S3 Transfer Acceleration transferencia hacia S3.

AWS Cloud • Usa las ubicaciones de borde

CloudFront de todo el mundo.

edge location

- Aumenta la velocidad para las

Internet

transferencias de archivos

grandes entre países.

Any file types

S3 bucket

![Imagen 12-1](images/clase_3_page12_img1.png)

![Imagen 12-2](images/clase_3_page12_img2.png)

![Imagen 12-3](images/clase_3_page12_img3.png)

![Imagen 12-4](images/clase_3_page12_img4.png)

![Imagen 12-5](images/clase_3_page12_img5.png)

![Imagen 12-6](images/clase_3_page12_img6.png)

![Imagen 12-7](images/clase_3_page12_img7.png)

![Imagen 12-8](images/clase_3_page12_img8.png)

![Imagen 12-9](images/clase_3_page12_img9.png)

![Imagen 12-10](images/clase_3_page12_img10.png)

![Imagen 12-11](images/clase_3_page12_img11.png)

![Imagen 12-12](images/clase_3_page12_img12.png)

Amazon S3

Clases de almacenamiento de objetos

Acceso

Propósito general Intelligent tiering Archivo

infrecuente

S3 Standard S3 Intelligent

S3 Standard IA S3 Glacier

Tiering

Instant Retrieval

S3 Glacier

S3 OneZone-IA

Flexible Retrieval

S3 Glacier Deep

Archive

S3 on Outposts

![Imagen 13-1](images/clase_3_page13_img1.png)

![Imagen 13-2](images/clase_3_page13_img2.png)

![Imagen 13-3](images/clase_3_page13_img3.png)

Amazon S3

Clases de almacenamiento de objetos

S3 S3 Glacier

S3 S3 Standard- S3 Glacier S3 Glacier

Intelligent S3 One Zone-IA Deep

### Standard IA Instant Retrieval Flexible Retrieval

-Tiering Archive

Availability

≥3 ≥3 ≥3 1 ≥3 ≥3 ≥3

Zones

Minimum

capacity

## N/A N/A 128 KB 128 KB 128 KB N/A N/A

charge for

each object

Minimum

storage

N/A N/A 30 días 30 días 90 días 90 días 180 días

duration

charge

Retrieval Per Per Per Per Per

## N/A N/A

charge GB retrieved GB retrieved GB retrieved GB retrieved GB retrieved

![Imagen 14-1](images/clase_3_page14_img1.png)

![Imagen 14-2](images/clase_3_page14_img2.png)

![Imagen 14-3](images/clase_3_page14_img3.png)

Amazon S3

### Configuración del ciclo de vida

### Las configuraciones del ciclo de vida de Amazon S3 definen las

acciones que Amazon S3 aplica a un grupo de objetos:

- Las acciones de transición definen el traslado de objetos a otra

clase de almacenamiento.

- Las acciones de expiración definen cuándo expira un objeto.

### Definir una Los datos se transfieren automáticamente

política de ciclo a otra clase de almacenamiento sin

de vida. cambios en la aplicación del cliente.

![Imagen 15-1](images/clase_3_page15_img1.png)

![Imagen 15-2](images/clase_3_page15_img2.png)

![Imagen 15-3](images/clase_3_page15_img3.png)

Amazon S3

AWS Identity and Access Manager (IAM)

S3 Standard Amazon S3 Glacier

Eliminar 2

1

Conservar Copias de respaldo

30 días 10 años (compliance)

S3 Standard S3 Standard-IA Amazon S3

Glacier

3

Eliminar

Acceso

Acceso frecuente

infrecuente Archivado

durante 60 días

(un año) durante 7 años

![Imagen 16-1](images/clase_3_page16_img1.png)

![Imagen 16-2](images/clase_3_page16_img2.png)

![Imagen 16-3](images/clase_3_page16_img3.png)

![Imagen 16-4](images/clase_3_page16_img4.png)

![Imagen 16-5](images/clase_3_page16_img5.png)

![Imagen 16-6](images/clase_3_page16_img6.png)

![Imagen 16-7](images/clase_3_page16_img7.png)

![Imagen 16-8](images/clase_3_page16_img8.png)

![Imagen 16-9](images/clase_3_page16_img9.png)

![Imagen 16-10](images/clase_3_page16_img10.png)

![Imagen 16-11](images/clase_3_page16_img11.png)

![Imagen 16-12](images/clase_3_page16_img12.png)

Amazon S3

Versionado

Acción Con versionado Sin versionado

Crea un Nuevo objeto con una ID

de version diferente.

Subir un objeto

Sobreescribe el objeto original, que

con la misma

queda inaccessible.

clave

Ambos son accesibles usando el

version ID.

Agrega una marca de borrado,

Borra el objeto, que ya no queda

Eliminar el objeto pero el objeto queda accessible

accessible.

usando el ID de version.

![Imagen 17-1](images/clase_3_page17_img1.png)

![Imagen 17-2](images/clase_3_page17_img2.png)

![Imagen 17-3](images/clase_3_page17_img3.png)

Amazon S3

Versionado

## PUT

### Object key = photo.gif

- Amazon S3 genera un nuevo

ID de versión y agrega el

nuevo objeto al bucket.

- La versión original también

permanece en el bucket.

Object key = photo.gif

## ID = 121245

Object key = photo.gif

## ID = 111111

Version-enabled S3 bucket

![Imagen 18-1](images/clase_3_page18_img1.png)

![Imagen 18-2](images/clase_3_page18_img2.png)

![Imagen 18-3](images/clase_3_page18_img3.png)

![Imagen 18-4](images/clase_3_page18_img4.png)

![Imagen 18-5](images/clase_3_page18_img5.png)

![Imagen 18-6](images/clase_3_page18_img6.png)

![Imagen 18-7](images/clase_3_page18_img7.png)

![Imagen 18-8](images/clase_3_page18_img8.png)

![Imagen 18-9](images/clase_3_page18_img9.png)

Amazon S3

Versionado - Eliminación

## DELETE

Object key =

photo.gif

Cuando se hace una solicitud

Delete

de borrado a un bucket con

marker

versionado, todas las versiones

Object key = photo.gif

se conservan en el bucket, pero

## ID = 3456778

Amazon S3 agrega una marca

Object key = photo.gif de borrado.

## ID = 121245

Object key = photo.gif

## ID = 111111

Version-enabled S3 bucket

![Imagen 19-1](images/clase_3_page19_img1.png)

![Imagen 19-2](images/clase_3_page19_img2.png)

![Imagen 19-3](images/clase_3_page19_img3.png)

![Imagen 19-4](images/clase_3_page19_img4.png)

![Imagen 19-5](images/clase_3_page19_img5.png)

![Imagen 19-6](images/clase_3_page19_img6.png)

![Imagen 19-7](images/clase_3_page19_img7.png)

![Imagen 19-8](images/clase_3_page19_img8.png)

![Imagen 19-9](images/clase_3_page19_img9.png)

![Imagen 19-10](images/clase_3_page19_img10.png)

![Imagen 19-11](images/clase_3_page19_img11.png)

Amazon S3

Versionado – Recuperación de la última versión

## GET

Object key =

photo.gif

404 no object

La solicitud de un objeto

found

devuelve la versión más

reciente.

Si la versión más reciente tiene

Delete

una marca de borrado, la

marker

solicitud falla.

Object key = photo.gif

## ID = 3456778

Object key = photo.gif

## ID = 121245

Object key = photo.gif

## ID = 111111

VVeerrssiioonn--eennaabblleedd SS33 bbuucckkeett

![Imagen 20-1](images/clase_3_page20_img1.png)

![Imagen 20-2](images/clase_3_page20_img2.png)

![Imagen 20-3](images/clase_3_page20_img3.png)

![Imagen 20-4](images/clase_3_page20_img4.png)

![Imagen 20-5](images/clase_3_page20_img5.png)

![Imagen 20-6](images/clase_3_page20_img6.png)

![Imagen 20-7](images/clase_3_page20_img7.png)

![Imagen 20-8](images/clase_3_page20_img8.png)

![Imagen 20-9](images/clase_3_page20_img9.png)

![Imagen 20-10](images/clase_3_page20_img10.png)

![Imagen 20-11](images/clase_3_page20_img11.png)

Amazon S3

Versionado – Recuperación de la última versión

## GET

Object key = photo.gif with

version ID = 121245

Si la solicitud de un objeto

Delete marker eliminado incluye el ID de la

versión, Amazon S3 nos

Object key = photo.gif

devolverá esa versión del

## ID = 3456778

objeto.

Object key = photo.gif

## ID = 121245

Object key = photo.gif

## ID = 111111

VVeerrssiioonn--eennaabblleedd SS33 bbuucckkeett

![Imagen 21-1](images/clase_3_page21_img1.png)

![Imagen 21-2](images/clase_3_page21_img2.png)

![Imagen 21-3](images/clase_3_page21_img3.png)

![Imagen 21-4](images/clase_3_page21_img4.png)

![Imagen 21-5](images/clase_3_page21_img5.png)

![Imagen 21-6](images/clase_3_page21_img6.png)

![Imagen 21-7](images/clase_3_page21_img7.png)

![Imagen 21-8](images/clase_3_page21_img8.png)

![Imagen 21-9](images/clase_3_page21_img9.png)

![Imagen 21-10](images/clase_3_page21_img10.png)

![Imagen 21-11](images/clase_3_page21_img11.png)

Amazon S3

Versionado – Eliminación permanente de un objeto

## DELETE

Object key = photo.gif

With version id = 121245

Para borrar definitivamente

un objeto, se especifica el

ID de la versión.

En este caso, la eliminación

es permanente.

Object key = photo.gif

## ID = 121245

Object key = photo.gif

## ID = 111111

VVeerrssiioonn--eennaabblleedd SS33 bbuucckkeett

![Imagen 22-1](images/clase_3_page22_img1.png)

![Imagen 22-2](images/clase_3_page22_img2.png)

![Imagen 22-3](images/clase_3_page22_img3.png)

![Imagen 22-4](images/clase_3_page22_img4.png)

![Imagen 22-5](images/clase_3_page22_img5.png)

![Imagen 22-6](images/clase_3_page22_img6.png)

![Imagen 22-7](images/clase_3_page22_img7.png)

![Imagen 22-8](images/clase_3_page22_img8.png)

![Imagen 22-9](images/clase_3_page22_img9.png)

Amazon S3

## CORS

<CORSConfiguration>

<CORSRule>

<AllowedOrigin>*</AllowedOrigin>

<AllowedMethod>GET</AllowedMethod>

Amazon S3 Dominio

</CORSRule>

principal

</CORSConfiguration>

## CORS

Permitir solicitudes GET de

cualquier origen

S3 bucket

Dominio

alternativo

![Imagen 23-1](images/clase_3_page23_img1.png)

![Imagen 23-2](images/clase_3_page23_img2.png)

![Imagen 23-3](images/clase_3_page23_img3.png)

![Imagen 23-4](images/clase_3_page23_img4.png)

![Imagen 23-5](images/clase_3_page23_img5.png)

![Imagen 23-6](images/clase_3_page23_img6.png)

![Imagen 23-7](images/clase_3_page23_img7.png)

![Imagen 23-8](images/clase_3_page23_img8.png)

Amazon S3

### Modelo de consistencia de datos

Es consistente para todos los objetos nuevos y

existentes en todas las regiones.

## PUT

### Version 2

### Provee consistencia read-after-write para todas las

operaciones GET, LIST, PUT y DELETE que se apliquen a

Read (even if immediate)

objetos que se encuentran en buckets de S3

S3 bucket

Version 2

Ofrece una ventaja para las grandes cargas de

datos

Simplifica la migración de cargas analíticas on-

premises.

![Imagen 24-1](images/clase_3_page24_img1.png)

![Imagen 24-2](images/clase_3_page24_img2.png)

![Imagen 24-3](images/clase_3_page24_img3.png)

![Imagen 24-4](images/clase_3_page24_img4.png)

![Imagen 24-5](images/clase_3_page24_img5.png)

![Imagen 24-6](images/clase_3_page24_img6.png)

![Imagen 24-7](images/clase_3_page24_img7.png)

Amazon S3

### Seguridad

Los buckets y objetos son privados por default.

El cifrado de buckets está configurada por default. Usa cifrado del lado del servidor con

las claves gestionadas de Amazon S3 (SSE-S3).

Para compartir datos en S3, debemos:

- Administrar y controlar los accesos

- Seguir el principio de mínimo privilegio.

![Imagen 25-1](images/clase_3_page25_img1.png)

![Imagen 25-2](images/clase_3_page25_img2.png)

![Imagen 25-3](images/clase_3_page25_img3.png)

Amazon S3

Cifrado

### Server-side encryption

Amazon S3 cifra los objetos antes de grabarlos en disco y los descifra

cuando los descargamos.

Esta es la opción por default de Amazon S3.

### Client-side encryption

Cifrar los datos del lado del cliente y subirlos ya encriptados.

En este caso, el proceso de cifrado es gestionado por el cliente.

![Imagen 26-1](images/clase_3_page26_img1.png)

![Imagen 26-2](images/clase_3_page26_img2.png)

![Imagen 26-3](images/clase_3_page26_img3.png)

Amazon S3

Herramientas de protección

### Herramienta Descripción

Block Public Access Bloquea el acceso público a los buckets

Políticas de AWS Identity and

Autenticación de usuarios

### Access Management (IAM)

### Políticas de buckets Define accesos sobre la base de reglas específicas

### Access control lists (ACLs) Reglas de acceso a buckets y objetos (son preferibles las políticas)

Se configure el acceso con nombres y permisos específicos para

Amazon S3 access points

cada aplicación

### URLs preasignadas Brinda acceso temporal mediante una URL

AWS Trusted Advisor Permite chequear los permisos de un bucket

![Imagen 27-1](images/clase_3_page27_img1.png)

![Imagen 27-2](images/clase_3_page27_img2.png)

![Imagen 27-3](images/clase_3_page27_img3.png)

Amazon S3

Modelos de acceso

Con políticas de

Default Público

acceso

1 2 3

Owner Owner Owner

Private S3 Controlled Public

User A

bucket Access to S3 access to

bucket

S3 bucket

Anyon Anyon

User B

e else e else

![Imagen 28-1](images/clase_3_page28_img1.png)

![Imagen 28-2](images/clase_3_page28_img2.png)

![Imagen 28-3](images/clase_3_page28_img3.png)

![Imagen 28-4](images/clase_3_page28_img4.png)

![Imagen 28-5](images/clase_3_page28_img5.png)

![Imagen 28-6](images/clase_3_page28_img6.png)

![Imagen 28-7](images/clase_3_page28_img7.png)

![Imagen 28-8](images/clase_3_page28_img8.png)

![Imagen 28-9](images/clase_3_page28_img9.png)

![Imagen 28-10](images/clase_3_page28_img10.png)

![Imagen 28-11](images/clase_3_page28_img11.png)

![Imagen 28-12](images/clase_3_page28_img12.png)

![Imagen 28-13](images/clase_3_page28_img13.png)

![Imagen 28-14](images/clase_3_page28_img14.png)

![Imagen 28-15](images/clase_3_page28_img15.png)

![Imagen 28-16](images/clase_3_page28_img16.png)

![Imagen 28-17](images/clase_3_page28_img17.png)

![Imagen 28-18](images/clase_3_page28_img18.png)

![Imagen 28-19](images/clase_3_page28_img19.png)

![Imagen 28-20](images/clase_3_page28_img20.png)

![Imagen 28-21](images/clase_3_page28_img21.png)

![Imagen 28-22](images/clase_3_page28_img22.png)

![Imagen 28-23](images/clase_3_page28_img23.png)

![Imagen 28-24](images/clase_3_page28_img24.png)

![Imagen 28-25](images/clase_3_page28_img25.png)

Amazon S3

Selección de regiones

### Consideraciones Detalles

- ¿Existen leyes relevantes de privacidad en la región?

### Cumplimiento legal y

- ¿Los datos de los clientes se pueden almacenar fuera del país?

regulatorio

- ¿Podemos cumplir nuestras obligaciones de gestión?

Proximidad entre los usuarios • Pequeñas diferencias en la latencia pueden generar impacto en la

y los datos experiencia del cliente.

- Elegir la región más cercana a los usuarios.

- No todos los servicios de AWS están disponibles en todas las

Disponibilidad de los servicios regiones.

- Regularmente, se expanden los servicios a nuevas regiones.

- El uso de servicios entre regions aumenta la latencia.

- Los costos varían según la región.

- Algunos servicios, como Amazon S3, tienen costo para las

Costos

transferencias salientes.

- Se deben evaluar los costos de replicar todo el entorno en otra

región.

![Imagen 29-1](images/clase_3_page29_img1.png)

![Imagen 29-2](images/clase_3_page29_img2.png)

![Imagen 29-3](images/clase_3_page29_img3.png)

Amazon S3

### Inventario

- Amazon S3 Inventory ayuda a administrar el almacenamiento.

- Se usa para auditor y generar reportes sobre el estado de la

replicación y la encripción de los objetos.

- Contribuye a cumplir los objetivos de negocio, de cumplimiento y

regulatorios.

- Acelera los flujos de negocio y las tareas de análisis de datos.

- Brinda una alternativa programable a las operaciones sincrónicas de

Amazon S3 (List API operations).

![Imagen 30-1](images/clase_3_page30_img1.png)

![Imagen 30-2](images/clase_3_page30_img2.png)

![Imagen 30-3](images/clase_3_page30_img3.png)

Amazon S3

Costos

### Se paga por uso No tienen costo

- Los gigabytes de objetos Los datos salientes hacia internet,

hasta los primeros 100 GB por mes

almacenados (por mes). Los

precios varían por región y por

Los datos transferidos entre

tipo de almacenamiento.

buckets de S3 o hacia cualquier

servicio de AWS dentro de la

## • PUT, COPY, POST, LIST

misma región.

- Las transiciones que mueven

Hacia CloudFront

datos entre las diferentes clases

de almacenamiento Amazon

## S3

![Imagen 31-1](images/clase_3_page31_img1.png)

![Imagen 31-2](images/clase_3_page31_img2.png)

![Imagen 31-3](images/clase_3_page31_img3.png)

Actividades

Material Laboratorio

Guía de estudio del Challenge (Cafe) lab:

módulo 4 Creating a Static Website for

the Café

Módulo 4. Knowledge check

Vencimiento: 5/9

![Imagen 32-1](images/clase_3_page32_img1.png)

![Imagen 32-2](images/clase_3_page32_img2.png)

![Imagen 32-3](images/clase_3_page32_img3.png)

Muchas gracias.

www.austral.edu.ar

![Imagen 33-1](images/clase_3_page33_img1.png)

![Imagen 33-2](images/clase_3_page33_img2.png)

![Imagen 33-3](images/clase_3_page33_img3.png)
