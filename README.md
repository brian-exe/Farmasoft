Farmasoft
==========

## Nueva version disponible!
### Ver cambios en [release notes](https://github.com/brian-exe/Farmasoft/blob/master/release_notes.md)

INTRODUCCIÓN:
-------------

El presente sistema está destinado a la administracion y consulta de las ventas realizadas por la empresa.

FLUJO DEL PROGRAMA:
-------------------

Como pagina de bienvenida, se ofrece una pequeña pagina de bienvenida, en donde ademas se puede ver la barra de navegacion que estará en todas las paginas del sitio.
En dicha barra de navegación se encontraran los diferentes botones correspondientes a funcionalidades específicas.
Dado que la barra de navegación estará siempre visible, la misma mostrara los botones dependiendo si el usuario tienen o no permisos para verlos.


ESTRUCTURA DE REPRESENTACION:
-----------

La estructura de los datos de entrada para el programa se obtienen de un archivo .csv, donde los datos estarán separados por comas.
Al momento de mostrarlos por pantalla, en cambio, los datos serán mostrados en forma de tabla, haciendo mas agradeble y entendible a la vista.

UTILIZACION EL PROGRAMA:
------------------------

Para poder ver las funciones tales como las consultas o la lista de ventas, el usuario de la aplicación deberá estar logueado.

Para loguearse podrá ver dos botones en la esquina superior derecha: uno para registrarse y otro para realizar el login. Si se el usuario ya está registrado deberá hacer click sobre "login", caso contrario deberá registrarse desde el botón "Registrarse".
Una vez registrado, el usuario estará habilitado para loguearse con su usuario y contraseña.

Luego de loguearse, se habilitarán en la barra de navecación las siguientes opciones:

+ Listar: Muestra una tabla con las ultimas ventas realizadas
+ Agregar Venta: redirige a la pagina para ingresar una nueva venta.
+ Consultas: Menú desplegable desde el que estarán disponibles las distintas consultas que se pueden realizar. Dichas consultas son:
    - Productos por cliente : Retorna una tabla con los prodcutos que haya comprado el cliente ingresado para buscar.
    - Clientes por producto: Retorna una tabla con los nombres de los clientes que compraron el producto ingresado para buscar.
    - Mejores Clientes: Retorna la cantidad de resultados que se ingresan de la lista de mejores clientes. Basandose en la cantidad de dinero gastado por venta.
    - Productos mas Vendidos: Retorna una tabla con los productos mas vendidos

CLASES UTILIZADAS:
------------------
+ User: Clase que representa a cada usuario. Necesaria para poder utilizar "Flask-login"
+ UserRepository: Clase que se encargará de autenticar usuarios, dar de alta nuevos, comprobar que existan, etc. 
+ Validador: Clase dedicada a comprobar el archivo que se va a leer. Se comprobaran los distintos aspectos pedidos.
+ ValidationException: Clase Exception para poder encapsular cualquier error de validación del archivo.
+ AdminDB: Clase encargada de la lectura/escritura como asi tambien de realizar las distintas consultas sobre el archivo de datos de ventas.
+ Config: Pequeña clase dedicada para leer el archivo de condfiguraciones.

### Autor: Ezequiel Aciar
