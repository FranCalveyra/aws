# CLI

Command Line Interface

![Imagen 2-1](images/cli_page2_img1.png)

Ejemplo: crear una instancia

aws ec2 run-instances `

--image-id ami-0ecb62995f68bb549 `

--instance-type t2.micro `

--key-name your-key-pair-name `

--security-group-ids sg-0e937765abb07dea2 `

--subnet-id subnet-04714c83b6cab17a0 `

--tag-specifications

'ResourceType=instance,Tags=[{Key=Name,Value=fer}]'

![Imagen 3-1](images/cli_page3_img1.png)

Ejemplo: crear una instancia

(mínimo)

aws ec2 run-instances \

--image-id ami-0c55b159cbfafe1f0 \

--instance-type t2.micro

![Imagen 4-1](images/cli_page4_img1.png)

Ejemplo: obtener parámetros

Mostrar Key Pairs:

aws ec2 describe-key-pairs --query

'KeyPairs[*].[KeyName,KeyPairId]' --output table

O simplemente:

aws ec2 describe-key-pairs

![Imagen 5-1](images/cli_page5_img1.png)

Ejemplo: detener instancias

aws ec2 stop-instances \

--instance-ids i-1234567890abcdef0

![Imagen 6-1](images/cli_page6_img1.png)

Llamada desde lenguajes de alto nivel

import boto3

# Inicializar el cliente de EC2

ec2 = boto3.client('ec2', region_name='us-east-1')

# Crear una instancia EC2

response = ec2.run_instances(

ImageId='ami-xxxxxxxxxxxxxxxxx

InstanceType='t2.micro’,

KeyName='your-key-pair-name',

SecurityGroupIds=['sg-xxxxxxxxxxxxxxxxx'],

![Imagen 7-1](images/cli_page7_img1.png)

Llamada desde lenguajes de alto nivel

### Placement={

'AvailabilityZone': 'us-east-1a' # Zona de disponibilidad

},

MinCount=1, # Número mínimo de instancias

MaxCount=1, # Número máximo de instancias

TagSpecifications=[

{ 'ResourceType': 'instance',

'Tags': [

{'Key': 'Name', 'Value': 'MiInstancia'}

]

}

]

)

![Imagen 8-1](images/cli_page8_img1.png)

Llamada desde lenguajes de alto nivel

# Obtener el ID de la instancia creada

instance_id = response['Instances'][0]['InstanceId']

print(f"Instancia creada con ID: {instance_id}")

![Imagen 9-1](images/cli_page9_img1.png)

### Metadatos de instancia

Es un servicio que permite a las instancias EC2 acceder a información sobre sí

mismas mientras están en ejecución.

### ¿Cómo funciona?

Desde dentro de una instancia EC2, se puede consultar un endpoint HTTP

especial:

http://169.254.169.254/latest/meta-data/

Se pueden obtener datos como:

- ID de la instancia: instance-id

- Tipo de instancia: instance-type

- IP pública/privada: public-ipv4, local-ipv4

- Zona de disponibilidad: placement/availability-zone

- Credenciales IAM: iam/security-credentials/

- User data: Scripts de inicio

- Hostname: Nombre el host

![Imagen 10-1](images/cli_page10_img1.png)

Metadatos de instancia

Ejemplo práctico (bash)

# Obtener el ID de instancia

curl http://169.254.169.254/latest/meta-data/instance-id

# Obtener la IP privada

curl http://169.254.169.254/latest/meta-data/local-ipv4

### Casos de uso

- Scripts de configuración automática

- Obtener credenciales temporales de IAM

- Identificar la región/zona donde corre la instancia

- Aplicaciones que necesitan auto-configurarse según su entorno

![Imagen 11-1](images/cli_page11_img1.png)

Metadatos de instancia

### IMDSv2 (recomendado)

AWS recomienda usar la versión 2 (IMDSv2) que requiere un token

de sesión para mayor seguridad:

TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-

metadata-token-ttl-seconds: 21600")

curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-

data/

![Imagen 12-1](images/cli_page12_img1.png)
