# CLI

Muchas de las acciones (por no decir todas) que podemos ejecutar en el dashboard de AWS se pueden realizar por medio de la línea de comandos de nuestro sistema (instalando las librerías correctas)

## Ejemplo: crear una instancia
```bash
aws ec2 run-instances `

--image-id ami-0ecb62995f68bb549 `

--instance-type t2.micro `

--key-name your-key-pair-name `

--security-group-ids sg-0e937765abb07dea2 `

--subnet-id subnet-04714c83b6cab17a0 `

--tag-specifications

'ResourceType=instance,Tags=[{Key=Name,Value=fer}]'
```

## Ejemplo: crear una instancia (mínimo)

```bash
aws ec2 run-instances \

--image-id ami-0c55b159cbfafe1f0 \

--instance-type t2.micro
```

## Ejemplo: obtener parámetros

**Mostrar Key Pairs:**
```bash
aws ec2 describe-key-pairs --query

'KeyPairs[*].[KeyName,KeyPairId]' --output table
```

O simplemente:
```bash
aws ec2 describe-key-pairs
```

## Ejemplo: detener instancias

```bash
aws ec2 stop-instances \

--instance-ids i-1234567890abcdef0
```

## Llamada desde lenguajes de alto nivel
Podemos hacerlo no solo desde línea de comandos, sino también por el SDK de algún lenguaje de programación.

Véase el siguiente ejemplo en Python
```py
import boto3

# Inicializar el cliente de EC2

ec2 = boto3.client('ec2', region_name='us-east-1')

# Crear una instancia EC2

response = ec2.run_instances(
    ImageId="ami-xxxxxxxxxxxxxxxxx",
    InstanceType="t2.micro",
    KeyName="your-key-pair-name",
    SecurityGroupIds=["sg-xxxxxxxxxxxxxxxxx"],
    Placement={"AvailabilityZone": "us-east-1a"},  # Zona de disponibilidad
    MinCount=1,  # Número mínimo de instancias
    MaxCount=1,  # Número máximo de instancias
    TagSpecifications=[
        {"ResourceType": "instance", "Tags": [{"Key": "Name", "Value": "MiInstancia"}]}
    ],
)
```

### Obtener el ID de la instancia creada
```py
instance_id = response['Instances'][0]['InstanceId']

print(f"Instancia creada con ID: {instance_id}")
```

## Metadatos de instancia

Es un servicio que permite a las instancias EC2 acceder a información sobre sí mismas mientras están en ejecución.

### ¿Cómo funciona?

Desde dentro de una instancia EC2, se puede consultar un endpoint HTTP especial:

`http://169.254.169.254/latest/meta-data/`

Se pueden obtener datos como:

- **ID de la instancia**: instance-id
- **Tipo de instancia**: instance-type
- **IP pública/privada**: public-ipv4, local-ipv4
- **Zona de disponibilidad**: placement/availability-zone
- **Credenciales IAM**: iam/security-credentials/
- **User data**: Scripts de inicio
- **Hostname**: Nombre el host

### Ejemplo práctico (bash)

**Obtener el ID de instancia**

```bash
curl http://169.254.169.254/latest/meta-data/instance-id
```

**Obtener la IP privada**

```bash
curl http://169.254.169.254/latest/meta-data/local-ipv4
```

#### Casos de uso

- Scripts de configuración automática
- Obtener credenciales temporales de IAM
- Identificar la región/zona donde corre la instancia
- Aplicaciones que necesitan auto-configurarse según su entorno

### IMDSv2 (recomendado)

AWS recomienda usar la versión 2 (IMDSv2) que requiere un token de sesión para mayor seguridad:

```bash
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/
```
