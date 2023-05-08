# ***Pagina Web para consulta de estacion de ecobici más cercana***

El siguiente repositorio muestra la infraestructura y despliegue de la misma en AWS, correspondiente al curso de [*Cloud Architecture del ITBA*](https://innovacion.itba.edu.ar/educacion-ejecutiva/tic/cloud-architecture/)

Si bien se podrian optimizar costos, realizando todo en una funcion lambda, 

## ***Descripcion del proyecto***

La idea principal del proyecto es montar una infraestructura en la nube de AWS para poder a traves de la latitud y longitud ingresada por el usuario, consultar cual es la estacion de ecobicis más cercana con la cantidad de bicicletas disponibles

## ***Backend***

Para la generacion del backend se creara un cluster de contenedores en los cuales correran las actualizaciones de las distintas estaciones de ecobicis, con la finalidad de brindar informacion actualizada de las mismas.

La informacion se obtiene a traves de las API de [*Buenos Aires Data*](https://data.buenosaires.gob.ar/dataset/). Para conectar a la misma se requieren tanto el *client_id* como el *client_secret* que se obtienen al registrarse.

### Infraestructura

Para la infraesctructura defina se incluye el siguiente diagrama:


![](https://github.com/RArielAlonso/aws-itba-tp/blob/main/resources/Diagrama%20de%20infraestructura.png?raw=True)

El contenedor correra un script de Python donde se hara la consulta a la API descripta anteriormente, se realizara la transformacion correspondiente y se guardara dicha informacion en la base de datos (Postgresql)

Para ingresar a la base de datos, se realizo un puente ssh entre el bastion host y la misma para de esta forma poder consultar los datos. En la realidad deberia usarse una VPN para brindarle mayor seguridad a la red.

- Ingreso a base de datos:

Cada vez que se quiera ingresar a la base de datos se ejecutan los siguientes comandos desde la terminal para de esta forma generar el tunel:

*Tunel SSH Teorico*
<pre><code>ssh -i your-pem-file-name.pem -f -N -L 5432:aurora-db-dns:5432 ec2-user@jump-box-public-ip -v
</code></pre> 

*Tunel SSH Ejemplo*
<pre><code>ssh -i itba-tp.pem -f -N -L 5432:database-ecobikes.c0d9fwrv6o9h.us-east-1.rds.amazonaws.com:5432 ec2-user@54.86.38.49 -v</code></pre> 

Esto generar en background el tunel para poder ingresar a la base de datos

## ***Etapas***

1- Creacion de la base de datos donde se almacenara la informacion correspondiente

2- Popular dicha base de datos para que actualice segun una frecuencia a determinar (1 minuto? ver cantidad de requests disponibles para el token)

3- Generar la vista en la pagina web y mediante lambda consultar la direccion, generar elastic cache para la ultima version de los datos
Ver text box en html

4- Refrescar la informacion con cloudwatch?


