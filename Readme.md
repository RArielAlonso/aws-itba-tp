# ***AWS - Consulta de estacion de ecobici más cercana***

El siguiente repositorio muestra la infraestructura y despliegue de la misma en AWS, correspondiente al curso de [*Cloud Architecture del ITBA*](https://innovacion.itba.edu.ar/educacion-ejecutiva/tic/cloud-architecture/)

Si bien se podrian optimizar costos, realizando todo en una funcion lambda, la idea es repasar los principales servicios desde el lado practico.

## ***Descripcion del proyecto***

La idea principal del proyecto es montar una infraestructura en la nube de AWS para poder a traves de la latitud y longitud ingresada por el usuario, consultar cual es la estacion de ecobicis más cercana con la cantidad de bicicletas disponibles

## ***Backend***

Para la generacion del backend se creara un cluster de contenedores en los cuales correran las actualizaciones de las distintas estaciones de ecobicis, con la finalidad de brindar informacion actualizada de las mismas.

La informacion se obtiene a traves de las API de [*Buenos Aires Data*](https://data.buenosaires.gob.ar/dataset/). Para conectar a la misma se requieren tanto el *client_id* como el *client_secret* que se obtienen al registrarse.

### Diagrama de Infraestructura

Para la infraesctructura defina se incluye el siguiente diagrama:


![](https://github.com/RArielAlonso/aws-itba-tp/blob/main/resources/Diagrama%20de%20infraestructura.png?raw=True)

El contenedor correra un script de Python donde se hara la consulta a la API descripta anteriormente, se realizara la transformacion correspondiente y se guardara dicha informacion en la base de datos (Postgresql)

#### *Ingreso a base de datos:*

Para ingresar a la base de datos, se realizo un puente ssh entre el bastion host y la misma para de esta forma poder consultar los datos. En la realidad deberia usarse una VPN para brindarle mayor seguridad a la red.

Cada vez que se quiera ingresar a la base de datos se ejecutan los siguientes comandos desde la terminal para de esta forma generar el tunel:

*Tunel SSH Teorico*
<pre><code>ssh -i your-pem-file-name.pem -f -N -L 5432:aurora-db-dns:5432 ec2-user@jump-box-public-ip -v
</code></pre> 

*Tunel SSH Ejemplo*
<pre><code>ssh -i itba-tp.pem -f -N -L 5432:database-ecobikes.c0d9fwrv6o9h.us-east-1.rds.amazonaws.com:5432 ec2-user@54.86.38.49 -v</code></pre> 

Esto generara en background el tunel para poder ingresar a la base de datos y el mismo se debera ejecutar cada vez que se quiera conectar al a base de datos

#### *ECR y ECS*

- Generacion de imagen y subida a ECR

Para la generacion de la imagen se utilizara Docker y la misma se subira a ECR ([Guia para pushear a ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)).

Para ingresar y poder copiar las images a ECR se debe configurar la CLI de AWS para *aws_access_key_id*, *aws_secret_access_key* y *aws_session_token*. A continuacion dejamos los comandos a ejecutar en la terminal para configurar el mismo:

<pre><code># for default profile

aws configure

# set the session token for default profile

aws configure set aws_session_token 
</code></pre>

Las credenciales se obtienen al ingresar al laboratorio en la seccion de AWS details.

Posteriormente al login se siguen los pasos en el instructivo detallado más arriba.

- Generacion de ECS con Fargate

Pasos para la generacion de la ejecucion:

1- Generacion de la task definition, a partir de la imagen subida a ECR se genera la *task definition*, en la misma se definen los parametros de comunicacion asi como las variables de entorno para ejecutar el contenedor.

*Como potencial mejora se podrian incluir las variables de entorno en Secrets Manager*

2 - Generacion del cluster, donde se ejecutara la tarea, para nuestro caso son las private subnets 1 y 2 y la infraestructura sera del tipo Fargate. Al ser una tarea simple y puntual se considera mejor que el manejo lo realice Amazon.

3- Una vez generado el cluster se puede ejecutar una sola tarea para ver la verificacion del proceso, importante definir bien las variables de entorno y los security groups para poder importar la imagen de ECR (el mismo debe permitir el trafico saliente hacia internet)


Se generaron dos recargas del mismo de forma manual, se podria utilizar EventBridge para automatizar la recarga pero esta fuera del permiso del laboratorio.

## ***Frontend***

### Diagrama de Infraestructura

![](https://github.com/RArielAlonso/aws-itba-tp/blob/main/resources/diagrama-frontend.png?raw=True)

El usuario consultara la pagina web estatica hosteada via S3 e ingresara los valores de latitud y longitud.

La pagina tendra un *API GATEWAY* que funcionara de trigger para la función lambda definida.

#### Static web Page in S3

Se genero un bucket con S3 para poder hostear la pagina web


#### Lambda function

A partir de una funcion lambda generada se utilizara para ubicar el punto mas cercano de ecobici que cuente con disponibilidad de bicicleta


## ***Etapas***


4- Refrescar la informacion con cloudwatch?


