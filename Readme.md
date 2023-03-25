# Pagina Web para consulta de estacion de ecobici más cercana


## Descripcion del proyecto

La idea principal del proyecto es montar una infraestructura en la nube de AWS para poder a traves de una direccion consultar cual es la estacion de ecobicis más cercana.

A traves de dicha infraestructura se dispondra de una URL de acceso publico en la cual se podrá insertar la dirección.


## Backend

Para la generacion del backend se creara un cluster de contenedores en los cuales correran las actualizaciones de las distintas estaciones de ecobicis, con la finalidad de brindar informacion actualizada de las mismas.

## Etapas

1- Creacion de la base de datos donde se almacenara la informacion correspondiente

2- Popular dicha base de datos para que actualice segun una frecuencia a determinar (1 minuto? ver cantidad de requests disponibles para el token)

3- Generar la vista en la pagina web y mediante lambda consultar la direccion, generar elastic cache para la ultima version de los datos
Ver text box en html

4- Refrescar la informacion con cloudwatch?


