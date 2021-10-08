
ENTREGA HITO 3
--------------

- De los 2 componentes que formarán parte de la solución "Pretty CV", la presente entrega es una versión Beta de ambos componentes

- El Componente 1 tenía como objetivo original la extracción de datos del perfil de LinkedIn a partir de un archivo pdf extraído manualmente de la web del usuario.

- No obstante, se ha hecho una modificación y lo que hace este componente es extraer los datos directamente del perfil de LinkedIn, dado que esto facilitará la estructuración de datos del CV.

- El output generado del componente 1 es un archivo cv.txt que contiene un diccionario con todos los datos extraídos del perfil.

- El programa no corre completamente si es lanzado desde gitbash, sólo si es ejecutado localmente. 

- El Componente 2 tiene como objetivo el generar un CV con los datos extraídos del perfil de LinkedIn a partir de una plantilla. El robot genera el CV con el diccionario contenido el cv.json y el archivo .png (foto) extraído del perfil

- El Componente 1 es lanzado desde el script main2.py. El programa solicitará el correo de linkedin y password. Le tomará alrededor de 3 minutos la extracción de datos y generación del archivo cv.txt

- El Componente 2 es lanzado desd el script cvbuilder_paralelo.py. Su ejecución toma unos pocos segundos y genera el archivo template_0_saved.docx