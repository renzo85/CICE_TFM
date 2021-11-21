
ENTREGA PFM
--------------

- De los 2 componentes que formarán parte de la solución "Pretty CV", la presente entrega es una versión FINAL de ambos componentes

- El Componente 1 tiene como objetivo extraer los datos directamente del perfil de LinkedIn, dado que esto facilitará la estructuración de datos del CV.

- El output generado del componente 1 es un archivo cv.txt que contiene un diccionario con todos los datos extraídos del perfil.

- El Componente 2 tiene como objetivo el generar un CV con los datos extraídos del perfil de LinkedIn a partir de una plantilla. El robot genera el CV con el diccionario contenido el cv.json y el archivo.png (foto) extraído del perfil

- Ambos componentes han sido unificados en un mismo código (main.py) y son ejecutados desde el html creado para la solución "Pretty CV" a través de 2 botones:

	-- Un primer botón "Start Process" que ejecuta el ingreso al perfil de LinkedIn, solicita al usuario las credenciales a través de gitbash, y después de algunos minutos genera el CV en formato word
	-- Un segundo botón "Download Pretty CV" que descarga el CV en formato word, en la carpeta de Descargas

- IMPORTANTE:

-- Tener en cuenta que los archivos en el github correspondiente a esta entrega tienen como comentario la palabra "project final".
-- No confundirlos con aquellos que estén con el comentario "project hito 3" que son de la entrega anterior
-- Todos los archivos necesarios para ejecutar el programa se encuentran dentro de la carpeta FLASKY