# ollivanders-flask-api-rest

## **Índice**

- [**Introducción**](#introducción)
- [**Lógica**](#lógica)
- [**Requisitos previos**](#requisitos-previos)
  - [**Instalación**](#instalación)
- [**Uso**](#uso)
  - [**CLI**](#cli)
  - [**PostMan**](#postman)
  - [**Navegador**](#navegador)
- [**Mas información**](#más-información)
  - [**Base de datos**](#base-de-datos)
  - [**Testing**](#testing)
- [**Docker**](#docker)

## Introducción

Te doy la bienvenida a Ollivanders-flask-api-rest, un proyecto en Python encomendada por nuestro tutor [David](https://github.com/dfleta) en el mes de Marzo como entretenimiento durante el proceso de entrevistas y selección de empresas en el curso de Formación Profesional Dual de Desarrollo de Aplicaciones Webs. Si deseas mas información, aquí tienes el [repositorio original](https://github.com/dfleta/ollivanders) de donde se ha sacado los objetivos para este proyecto

## Lógica

Para empezar, destacar que el código de la [lógica](https://github.com/JLDJR2481/ollivanders-flask-api-rest/tree/master/domain) no me pertenece. Ese código se ha sacado del famoso kata de [Emily Bache](https://github.com/emilybache) llamado [Gilded Rose](https://github.com/emilybache/GildedRose-Refactoring-Kata), que simula la gestión de un inventario ubicada en Ollivanders.

Aquí dejo el enlace al [comportamiento original](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.txt) sacado del repositorio de Emily

La lógica es muy sencilla. Cada día, se actualiza un inventario de forma que se reduce los días para su venta y su calidad. Hay una condición que cumplen casi todos los objetos: Si su calidad (en caso de que aumente) es superior a 50, se quedará fijada en 50. Si por el contrario llegan a 0, se fijarán en 0

Estos objetos se dividen en 5 tipos, con sus ciertas peculiaridades:

- **Normal Items**: Estos objetos no tienen un comportamiento muy complejo. Cada día se reduce en 1 su calidad, hasta que su fecha restante de caducidad llegue sea menor que 0, haciendo que se reduzca de 2 en 2.

- **Sulfuras**: Estos objetos, considerados legendarios, tienen una calidad fijada en 80 y no caducan nunca.

- **Backstage**: Estos pases cambian totalmente las reglas. Si la fecha para el concierto es superior a 10, se aumenta su calidad +1. Si es superior a 5, será de +2. Si es superior a 0, será de +3. Es decir, en el intervalo entre 10 y 5 (incluido 10) será de +2, y en el de 5 y 0 (incluido 5) será de +3. Si la fecha llega a 0, la calidad se fija a 0, ya que no tiene valor

- **Aged Brie**: Este tipo de queso tiene una peculiaridad. Su valor va en aumento de 1 en 1 hasta que caduca, momento en el que se aumentará de 2 en 2 hasta 50

- **Conjured**: Este añadido al inventario se comporta como un item normal, aunque se degrada el doble de rápido. Es decir, si aun no ha caducado su calidad baja en 2, y si caduca, bajará en 4

## Requisitos previos

El requisito más importante para poder ejecutar el programa es disponer de una URI de MongoDB Atlas para poder conectarte a tu base de datos y disfrutar del proyecto. Además, debes tener una API key para poder realizar CRUD sin problemas. Un ejemplo de URI es:

"mongodb+srv://USERNAME:PASSWORD@DATABASE.CONNECTION.mongodb.net/?retryWrites=true&w=majority"

Donde **USERNAME** es el usuario creado y con permisos en Atlas, **PASSWORD** es la contraseña vinculada el usuario, **DATABASE** es la base de datos que deseas utilizar y **CONNECTION** es un conjunto de caracteres que lo proporciona MongoDB. Aquí tienes [más información](https://www.mongodb.com/docs/atlas/connect-to-database-deployment/#connect-to-a-cluster)

### Instalación

Tras disponer de una URI de MongoDB Atlas y su Api_Key, instalamos el proyecto paso a paso:

1. Creamos un directorio para guardar nuestro proyecto.

```cmd
mkdir ./<nombre-directorio>
cd <nombre-directorio>
```

2. Creamos un entorno virtual para no instalar en la máquina local dependencias y paquetes que afecten al entorno:

```cmd
python -m venv venv
```

3. Clonar el repositorio

```cmd
git clone https://github.com/JLDJR2481/ollivanders-flask-api-rest
```

4. Crear una variable de entorno llamada "URI". Esto se puede hacer con un archivo .env. Ejemplo: URI="mongodb+srv://USERNAME:PASSWORD@DATABASE.CONNECTION.mongodb.net/?retryWrites=true&w=majority"

5. Instalar los paquetes y las dependencias necesarias para el correcto funcionamiento del proyecto:

```cmd
pip3 install -r requirements.txt
```

## Uso

Una vez instalado los paquetes y dependencias necesarias, y configurada la URI en el archivo .env, ejecutamos el fichero "app.py" con python. Tras ello, tenemos varias opciones para ver el funcionamiento de la aplicación flask:

1. CLI: Podemos usar la terminal con el comando curl para probar todas las rutas configuradas. Si quieres usar CLI, haz click [aquí](#cli)

2. PostMan: Podemos usar PostMan para comprobar si la aplicación Flask funciona. Para más información, haz click [aquí](#postman)

3. Navegador: El menos recomendado, ya que no permite mirar todas las funcionalidades de la aplicación. Más información [aquí](#navegador)

### CLI

Para usar la aplicación en un CLI, usaremos el comando curl. Para evitar filtraciones de IP, usaremos localhost. A continuación, se enseñarán todos los comandos y como usar todas las funcionalidades:

```cmd
curl http://localhost:5000/
```

![curl root](docs/imgs/root.PNG)

```cmd
curl http://localhost:5000/inventario
```

![inventario](docs/imgs/inventario.PNG)

```cmd
curl http://localhost:5000/inventario/update
```

![inventario_update](docs/imgs/inventario_update.PNG)

```cmd
curl http://localhost:5000/items
```

![items](docs/imgs/items.PNG)

```cmd
curl -d '{"_id": 10, "name": "Sombrero seleccionador", "sell_in": 80, "quality": 30, "item_type":"NormalItem"}' -H "Content-Type: application/json" -X POST http://localhost:5000/items/create
```

![create_item](docs/imgs/items_create.PNG)

```cmd
curl http://localhost:5000/items/find/<id>
```

![items_read](docs/imgs/items_read.PNG)

```cmd
 curl -d '{"quality":20}' -H "Content-Type: application/json" -X PUT http://localhost:5000/items/update/10
```

![items_update](docs/imgs/items_update.PNG)

```cmd
curl -X DELETE http://localhost:5000/items/delete/<id>
```

![items_delete](docs/imgs/items_delete.PNG)

### PostMan

Si deseas verlo por tu cuenta, haz click al botón Run in Postman tras ejecutar la app y exporta la colección de requests configurada

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/26400016-d7038b2b-efce-4afb-bec7-d6d80736f3d4?action=collection%2Ffork&collection-url=entityId%3D26400016-d7038b2b-efce-4afb-bec7-d6d80736f3d4%26entityType%3Dcollection%26workspaceId%3Db6e3eeac-770e-4cce-8f61-a31866271e87)

![root_postman](docs/imgs/postman_root.PNG)

![inventario_postman](docs/imgs/postman_inventario.PNG)

![updatear_inventario_postman](docs/imgs/postman_inventario_update.PNG)

![postman_items](docs/imgs/postman_items.PNG)

![create_items_postman](docs/imgs/postman_items_create.PNG)

![postman_read](docs/imgs/postman_items_read.PNG)

![postman_update](docs/imgs/postman_items_update.PNG)
![postupdate](docs/imgs/postman_post_update.PNG)

![postman_delete](docs/imgs/postman_post_delete.PNG)
![post_delete](docs/imgs/postman_post_delete.PNG)

### Navegador

Para usar el navegador, simplemente hay que abrir un navegador y escribir la url: http://localhost:5000

Este es el menos recomendado por el hecho del CRUD. No se puede crear, updatear ni deletear un item de la base de datos, así que se desaconseja probar la app al completo con el navegador.

## Más información

### Base de datos

Para poder usar la base de datos no se requiere nada más que lo anteriormente indicado, aunque si que hay una cosa que puntualizar a la hora de crear un item a la base de datos

Para poder crear un item, tiene que cumplir con 5 claves:

- \_id: Identificador único
- name: Nombre del objeto
- quality: Calidad del objeto
- sell_in: Tiempo de venta antes de caducidad
- item_type: El tipo de objeto para etiquetarlo a la hora de aplicar la lógica que le corresponde

### Testing

Se han utilizado casos tests individuales con pytest, unittest para la comprobación de una correcta integración de distintos metodos, coverage para revisar el porcentaje de cobertura de código y bandit junto a Tox para la comprobación de vulnerabilidades en el código:

- Testing
  ![testing](docs/imgs/pytest.PNG)

- Coverage
  ![coverage](docs/imgs/coverage.PNG)

## Docker

Este proyecto tiene una imagen Docker la cual puedes crear y ejecutar la applicación desde Docker si lo prefieres.

Para crear la imagen, escribe:

```cmd
docker build -t <nombre-imagen> .
```

Tras ello, para ejecutar correctamente un contenedor docker con la aplicación, escribimos en la terminal:

```cmd
docker run --name <nombre-contenedor> -e URI=<uri-mongo> -p 5000:5000 <nombre-imagen>
```

Si resulta que da problemas, asegurate de tener disponible el puerto 5000. Si no, desvía el puerto a otro que tengas disponible:

```cmd
docker run --name <nombre-contenedor> -e URI=<uri-mongo> -p <otro-puerto>:5000 <nombre-imagen>
```
