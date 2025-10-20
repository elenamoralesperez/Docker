# DOCKER
- Es una maquina virtual: "Ordenador dentro de un ordenador"
- Puedes usar varios sistemas operativos sin dañar tu equipo
- Sistema de contenedores 
- Ejemplos de programas: VirtualBox, VMware, Hyper-V

- Plataforma creada con el fin de **desarrollar, implementar y ejecutar aplicaciones dentro de contenedores**



### VENTAJAS

- Nos olvidamos de "En mi ordenador funciona..." 
- Mucho más ligero y escalable que una máquina virtual. 
- Trabajar en equipos de desarrollo. 
- La idea es emular durante el desarrollo lo máximo posible nuestro entorno de producción.



### PROCESO DE CREACIÓN

**Dockerfile**: Un Dockerfile es un archivo de texto plano que contiene una serie de instrucciones necesarias para crear una imagen. 
- Instrucciones para montar el coche 

**Docker image**: Las imágenes de Docker son esencialmente una instantánea de un contenedor. Las imágenes se crean con el comando **build**, que crean un contenedor. 
- Coche montado 

**Container**: es una imagen de Docker cuando empieza a funcionar, es decir, cuando cobra vida. 
- Coche en marcha



### COMANDOS

- Crear y ejecutar un contenedor nuevo a partir de una imagen de Docker: **docker run**
- Ver todos los contenedores de tu sistema, tanto los que están ejecutándose como los que están detenidos: **docker ps -a**
- Ponerle nombre: **--name web-server**
- Le pone el nombre web-server
- Eliminar contenedores: **docker rm**
- Buscar contenedores específicos: **docker ps -a | grep**
- Buscar información sobre el comando stop dentro de la ayuda de Docker: **docker help | grep stop**
- Crea y ejecuta un contenedor de Nginx (un servidor web) con un nombre personalizado y acceso desde tu navegador: **docker run --name web-server -p 80:80 nginx** (Mapea el puerto 80 del host (tu PC) al puerto 80 del contenedor)
- Inicia un contenedor que esta detenido: **docker start**
- Detiene un contenedor que está en ejecución: **docker stop**
- Reinicia un contenedor, es decir, lo detiene si está corriendo y lo vuelve a iniciar automáticamente: **docker restart**
- Programar tareas para que se ejecuten automáticamente en momentos específicos, sin intervención humana: **crontab**
- Entrar en el contenedor: **docker exec**
- Listar imagenes: **docker images**
- Elimina imagen de Docker: ***docker image rm**
- Construir imagenes: **docker build -t** el -t etiqueta la imagen con un nombre
- Descarga la última versión oficial de Python: **docker pull python**
- Ver todos los comandos docker pull que has ejecutado previamente: **history | grep "docker pull"** Muy útil si quieres repetir, revisar o depurar descargas de imágenes Docker
- Elimina los contenedores parados: **docker container prune**
- Elimina contenedores parados, imagenes viejas, caché sin usar..., data que no se usa: **docker system prune**
- Ver cuanto esta consumiendo: **docker system df**
- Ver informacion del sistema: **docker system info**
- Ver variables de entorno: **docker exec *nombrecontenedor* printenv**
- Elimina los contenedores y la red: **docker compose down**
- Muestra lista de contenedores que están actualmente en ejecucion: **docker compose ps**


## DOCKER HUB

Nos permite descargar y subir imágenes de Docker de forma sencilla.

Podemos compararlo con GitHub, donde gestionamos nuestro código fuente. Sin embargo, en el caso de Docker Hub, en lugar de código, trabajamos con imágenes de contenedores, que podemos obtener o publicar según nuestras necesidades



### Dockerfile

Documento de texto que contiene todas las instrucciones necesarias para construir una imagen de Docker

*FROM python:3.11-slim*   --> IMAGEN BASE, elegimos una imagen oficial de Python. Slim es una mini version de Linux
*WORKDIR /app*            --> Define dónde se harán todas las operaciones dentro del contenedor

*COPY . .*                --> Copiamos el resto del código de la aplic. desde host punto izq. y contenedor punto dch

*CMD ["python", "main.py"]* --> Definimos el comando que arranca la aplicación




### Construimos la imagen (montamos coche)

Con el Dockerfile en tu directorio, puedes construir y ejecutar la imagen.

**-t** Etiqueta la imagen con el nombre mi-app:latest.
**.** Busca el Dockerfile en el directorio actual.
**docker build -t mi-app:latest**


### Ejecutamos el contenedor(arrancamos coche)

Una vez construida la imagen ya podemos arrancar nuestro contenedor 
**-d** ejecuta en modo detached (segundo plano): **docker run --help | grep detach**



*Servidor de development*: entorno donde los programadores prueban su aplicación mientras la están creando; no es un servidor real
*Kernel:* núcleo del sistema operativo; hace de puente entre el hardware y los programas; quien coordina todo
*Ubuntu*: distribucion de Linux llamada Debian


## CLASE 2


REPASO:
CREAR IMAGEN DOCKER:
docker build -t *lo llamo como quiera*:latest .
docker images
docker run -d *pongo como lo he llamado* --> el numero que me sale es el **numero identificador**
docker ps --> lista los contenedores en ejecucion
docker logs y el ID del contenedor, por ej. c365f9f408ee


- ENTRYPOINT → dice qué programa siempre se ejecuta al arrancar el contenedor. ju*Cuando quieren hacer la conexion al servidor*
- CMD → dice qué argumentos o comando por defecto usar, pero se puede sobrescribir fácilmente. *Se utiliza mas para hacer migraciones*

**HAY QUE HACER UN DOCKERBUILD SIEMPRE QUE SE CAMBIE EL DOCKERFILE**



# EJECUTAR CONTENEDOR 

Este comando inicia un contenedor basado en tu Imagen.
**run**: Ejecuta la Imagen.
**-d**: Ejecuta el contenedor en modo detached (en segundo plano).
**-p 8080:80**: Mapea puertos. Expone el puerto **80** del **contenedor** al puerto *8080* de tu máquina local (el *host*).

- EL PRIMERO ES EL HOST CON EL DOBLE 80 Y EL ULTIMO EL CONTENEDOR DE DOCKER EL 80
**--name mi-contenedor**: Asigna un nombre fácil de recordar al contenedor.


# INICIAR CONTENEDOR
Podemos iniciar nuevamente un contenedor detenido:

-a, --attach: adjunta **shell** para salida y errores (STDOUT/STDERR).
-i, --interactive : adjunta shell interactiva (STDIN).
STD = standard

*docker start mi-contenedor*


# ELIMINAR CONTENEDOR
Con este comando eliminamos el contenedor por su nombre o ID:

-f, --force: fuerza la eliminación de un contenedor ya en marcha
-v, --volumes: elimina volúmenes anónimos asociados

*docker rm mi-contenedor*


# ¿QUE ES UN VOLUMEN?
- Un volumen es una carpeta o directorio fuera del contenedor, gestionado por Docker, donde puedes guardar datos que no quieres perder cuando el contenedor se elimina o reinicia.

Ejecutar un Contenedor con volumen

*Este comando inicia un contenedor basado en tu Imagen*
*run: Ejecuta la Imagen*
*-d: Ejecuta el contenedor en modo detached (en segundo plano).*
*-p 80:80: Mapea puertos. Expone el puerto 80 del contenedor al puerto 80 del host ( visible en http://localhost)*

**–v, --volume: Permite montar volúmenes. Conecta una carpeta del host ( . ) con una del contenedor (/usr/share/nginx/html)**  --> permite compartir archivos o carpetas entre tu máquina y el contenedor:
*$ docker run -d -p 80:80 -v .:/usr/share/nginx/html nginx*

### Usa la imagen oficial de Python 3.14 en versión slim
FROM python:3.14-slim
### Establece el directorio de trabajo dentro del contenedor
WORKDIR /app
### Copia solo el archivo de dependencias (requirements.txt) al contenedor. Se hace antes de copiar todo el código para que Docker pueda cachear la instalación de dependencias
COPY requirements.txt ./
### Copia todo el resto del código de tu proyecto al contenedor
RUN pip install --no-cache-dir -r requirements.txt
### Copia el resto del código de la aplicación
COPY . .
### Expone el puerto que usará la aplicación
EXPOSE 8000
### Comando para ejecutar la aplicación
CMD [“python", “main.py"]


### Librerias

requests # Para hacer solicitudes HTTP de manera muy sencilla y “humana”. Es como el equivalente a un navegador, pero controlado desde tu código.

pandas # Para trabajar con tablas, CSV, Excel y manipulación de datos tipo DataFrame.

numpy # Para cálculos numéricos, álgebra lineal y arrays eficientes.

openpyxl # Para leer y escribir archivos Excel.

matplotlib # Gráficos 2D clásicos (líneas, barras, scatter).

seaborn # Gráficos estadísticos bonitos y fáciles de hacer.

plotly # Gráficos interactivos y dashboards.

bokeh # Visualizaciones interactivas para web.


# ¿QUE ES DOCKER COMPOSE?

Docker Compose es una herramienta que, **a partir de un fichero YAML** (como el json pero sin comillas) permite crear, configurar e iniciar múltiples servicios dentro de contenedores. 

Ventajas:
- Definir y ejecutar varios contenedores a la vez, así como redes y volúmenes definidas en él.
- Iniciar, detener y administrar los servicios fácilmente.

Gracias a Docker Compose, el despliegue y la orquestación de contenedores se vuelven **más eficientes y organizados**.


### Compose file
Se puede guardar en un archivo *compose.yaml* el contenido necesario para emular lo que se hizo anteriormente desde la terminal con docker.

services:
   nginx:
     image: nginx:latest                     --> Ultima version de nginx; es igual que el **FROM**
     ports:                                  --> Mapea puertos del contenedor al host
       - 80:80
    volumes:                                 --> Conecta una carpeta host con una del contenedor
       - .:/usr/share/nginx/html

Para levantarlo se emplea el comando: **docker compose up**
- Compose le da run a mas de 1 contenedor
- Up, te crea una network sin que lo hagas tu 
