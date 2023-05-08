# ***Pagina Web para consulta de estacion de ecobici más cercana***

El siguiente repositorio muestra la infraestructura y despliegue de la misma en AWS.

## ***Descripcion del proyecto***

La idea principal del proyecto es montar una infraestructura en la nube de AWS para poder a traves de la latitud y longitud ingresada por el usuario, consultar cual es la estacion de ecobicis más cercana con la cantidad de bicicletas disponibles

## ***Backend***

Para la generacion del backend se creara un cluster de contenedores en los cuales correran las actualizaciones de las distintas estaciones de ecobicis, con la finalidad de brindar informacion actualizada de las mismas.

La informacion se obtiene a traves de las API de Buenos Aires Data (https://data.buenosaires.gob.ar/dataset/). Para conectar a la misma se requieren tanto el *client_id* como el *client_secret* que se obtienen al registrarse.

### Infraestructura

## ***Etapas***

1- Creacion de la base de datos donde se almacenara la informacion correspondiente

2- Popular dicha base de datos para que actualice segun una frecuencia a determinar (1 minuto? ver cantidad de requests disponibles para el token)

3- Generar la vista en la pagina web y mediante lambda consultar la direccion, generar elastic cache para la ultima version de los datos
Ver text box en html

4- Refrescar la informacion con cloudwatch?


