import boto3

# Inicializar el cliente de EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

# Crear una instancia EC2
response = ec2.run_instances(
    ImageId='ami-0ecb62995f68bb549',           # ID de la AMI (Amazon Machine Image)
    InstanceType='t3.micro',                    # Tipo de instancia
    KeyName='vockey',               # Nombre del par de claves
    MinCount=1,                                 # Número mínimo de instancias
    MaxCount=1,                                 # Número máximo de instancias
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'servidor'}
            ]
        }
    ]
)

# Obtener el ID de la instancia creada
instance_id = response['Instances'][0]['InstanceId']
print(f"Instancia creada con ID: {instance_id}")
