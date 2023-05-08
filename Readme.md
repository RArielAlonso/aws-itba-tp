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

El contenedor correrar un script de Python donde se hara la consulta a la API descripta anteriormente, se realizara la transformacion correspondiente y se guardara dicha informacion en la base de datos (Postgresql)


## ***Etapas***

1- Creacion de la base de datos donde se almacenara la informacion correspondiente

2- Popular dicha base de datos para que actualice segun una frecuencia a determinar (1 minuto? ver cantidad de requests disponibles para el token)

3- Generar la vista en la pagina web y mediante lambda consultar la direccion, generar elastic cache para la ultima version de los datos
Ver text box en html

4- Refrescar la informacion con cloudwatch?


