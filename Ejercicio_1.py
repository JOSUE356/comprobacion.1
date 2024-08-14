import tkinter as tk
 
def mostrar_menu():
    """
    Función que muestra el menú de opciones del diccionario informático en una ventana Tkinter.
    """
    ventana = tk.Tk()
    ventana.title("Diccionario Informático de Jefferson ")
 
    etiqueta_titulo = tk.Label(ventana, text="Bienvenido al Diccionario Informático de Fernando")
    etiqueta_titulo.pack()
 
    etiqueta_instrucciones = tk.Label(ventana, text="Seleccione una opción:")
    etiqueta_instrucciones.pack()
 
    boton_buscar = tk.Button(ventana, text="Buscar definición", command=buscar_termino)
    boton_buscar.pack()
 
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack()
 
    ventana.mainloop()
 
def buscar_termino():
    """
    Función que crea una ventana para que el usuario ingrese el término a buscar.
    """
    ventana_busqueda = tk.Toplevel()
    ventana_busqueda.title("Buscar Término")
 
    etiqueta_busqueda = tk.Label(ventana_busqueda, text="Ingrese el término que desee buscar:")
    etiqueta_busqueda.pack()
 
    entrada_termino = tk.Entry(ventana_busqueda)
    entrada_termino.pack()
 
    boton_buscar = tk.Button(ventana_busqueda, text="Buscar", command=lambda: buscar_definicion(entrada_termino.get()))
    boton_buscar.pack()
 
def buscar_definicion(termino):
    """
    Función que busca la definición de un término en el diccionario y muestra el resultado en una ventana Tkinter.
    Parameters:
    - termino (str): Término a buscar en el diccionario.
    """
    ventana_resultado = tk.Toplevel()
    ventana_resultado.title("Resultado de la Búsqueda")
 
    try:
        definicion = diccionario_informatico[termino]
        resultado = f"Definición de {termino}: {definicion}"
    except KeyError:
        resultado = "¡Término no encontrado en el diccionario!"
 
    etiqueta_resultado = tk.Label(ventana_resultado, text=resultado)
    etiqueta_resultado.pack()
 
# Aquí va tu diccionario informático...
diccionario_informatico = {
    "Python": "Lenguaje de programación de alto nivel",
    "HTML": "Lenguaje de marcado para el desarrollo web",
    "CPU": "Unidad Central de Procesamiento",
    "RAM": "Memoria de Acceso Aleatorio",
    "GPU": "Unidad de Procesamiento Gráfico",
    "API": "Interfaz de Programación de Aplicaciones",
    "IDE": "Entorno de Desarrollo Integrado",
    "DNS": "Sistema de Nombres de Dominio",
    "URL": "Localizador de Recursos Uniforme",
    "LAN": "Red de Área Local",
    "WAN": "Red de Área Extensa",
    "VPN": "Red Privada Virtual",
    "python": "lenguaje de programación",
    "tkinter": "biblioteca de interfaz gráfica",
    "Red Lan" :" red de área local o LAN es una red de computadoras que permite la comunicación y el intercambio de datos entre diferentes dispositivos a nivel local, ya que está limitada a distancias cortas",
    "ALGORITMO" : " Conjunto de pasos para una determinada tarea",
    "CODIGO": "conjunto de palabras o simbolos que contienen instrucciones para la computadora",
    "c#": "lenguaje de programacion orientado a objetos desarrollados por microsoft y que forma parte de la plataforma",
   "LINUX": "sistema operativo gratuito para computadoras personales derivado de Unix.",
    "JAVA" : "va es un lenguaje de programación multiplataforma orientado a objetos que se ejecuta en miles de millones de dispositivos de todo el mundo. ",
    "HTML" : "Se utiliza en documentos y en el mantenimiento de sitios web. En esencia, es un lenguaje de marcado que permite dar formato a la apariencia de la información en un sitio web.",
    "JAVASCRIPT" : "JavaScript, que se utiliza en desarrollo web, desarrollo de videojuegos, aplicaciones móviles y construcción de servidores web, sigue siendo entonces el lenguaje de programación más utilizado en la actualidad, en todo el mundo.",
    "NoSQL" : "Si bien no es un lenguaje de programación, NoSQL se refiere a una amplia clase de sistemas de gestión de bases de datos que se diferencian de los modelos relacionales tradicionales.",
    "Rust" : "Rust es un lenguaje de programación compilado, de propósito general y multiparadigma, desarrollado por la Fundación Mozilla. ",
    "APLICACIÓN WEB": "Programa que se ejecuta en un servidor web y se accede a través de un navegador",
    "ARQUITECTURA DE SOFTWARE": "Diseño y estructura de un sistema de software",
    "BASE DE DATOS": "Colección de datos organizados para facilitar su acceso y manipulación",
    "BÚSQUEDA DE DATOS": "Proceso de encontrar y recuperar información en una base de datos",
    "CLOUD COMPUTING": "Modelo de entrega de servicios de computación a través de Internet",
    "COMPUTACIÓN EN LA NUBE": "Modelo de entrega de servicios de computación a través de Internet",
    "virtualizacion" : "La virtualización es una tecnología que se puede usar para crear representaciones virtuales de servidores, almacenamiento, redes y otras máquinas físicas. ",
    "DESARROLLO WEB" : "Creación de sitios web y aplicaciones web",
    "DISEÑO DE INTERFAZ": "Creación de interfaces de usuario para sistemas de software",
    "DISEÑO DE SOFTWARE": "Proceso de crear y mejorar la estructura y el funcionamiento de un sistema de software",
    "CSS": "Lenguaje de hoja de estilos en cascada, utilizado para dar formato a documentos HTML",  
    "VIRTUAL BOX" : "Oracle VM VirtualBox es un software de virtualización para arquitecturas x86/amd64. Actualmente es desarrollado por Oracle Corporation como parte de su familia de productos de virtualización.",
    "VPS" : "Un servidor virtual privado, término que proviene del inglés virtual private server, es un sistema de alojamiento web. Su uso es cada vez más popular y, debido a su estructura de funcionamiento, es un servicio IaaS",
    "VPN" : "Una VPN o red privada virtual crea una conexión de red privada entre dispositivos a través de Internet",
    "CABLE COAXIAL " : " es el tipo de cable usado por las compañías de televisión por cable para establecer la conexión entre la central emisora y el usuario.",
    "REBOOT":"rebutear.",
    "SERVER": "servidor.",
    "VIRUS": "pequeño programa que infecta una computadora; puede causar efectos indeseables y hasta daños irreparables.",
    "ZIP": "formato de los archivos comprimidos."
   "UNIX" "sistema operativo multiusuario, fue muy importante en el desarrollo de Internet",
   "SOSTWARE": "término general que designa los diversos tipos de programas usados en computación",
   "TCP/IP": "Transfer Control Protocol / Internet Protocol. Es el protocolo que se utiliza en Internet.",
   "ROUTER" : "ruteador Sistema constituido por hardware y software para la transmisión de datos en Internet."
   "PUERTO SERIAL" "conexión por medio de la cual se envían datos a través de un solo conducto Por ejemplo, el mouse se conecta a un puerto serial.",
   "PROTOCOLO": "lenguaje que utilizan dos computadoras para comunicarse entre sí",
   "PROCESADOR": "conjunto de circuitos lógicos que procesa las instrucciones básicas de una computadora",
   "ONLINE": "en línea, conectado. Estado en que se encuentra una computadora cuando se conecta directamente con la red a través de un dispositivo",
   "NANOSEGUNDO": "una milmillonésima de segundo. Es una medida común del tiempo de acceso a la memoria RAM.",
   "NAVEGADOR": "programa para recorrer la World Wide Web. Algunos de los más conocidos son Netscape Navigator, Microsoft Explorer, Opera y Neoplanet.",
   "MODEM": "modulador-demodulador. Dispositivo periférico que conecta la computadora a la línea telefónica.",
   "MEMORIA CACHE": "pequeña cantidad de memoria de alta velocidad que incrementa el rendimiento de la computadora almacenando datos temporariamente.",
   "LATECIA": "lapso necesario para que un paquete de información viaje desde la fuente hasta su destino. La latencia y el ancho de banda, juntos, definen la capacidad y la velocidad de una red.",
   "LAN MANAGER": "sistema operativo de red",
   "IP":"Protocolo de Internet.",
   "ISP": "Internet ServiceProvider. Proveedor de servicios de Internet.",
   "HARD DISK": "disco rígido",
   "FIBRA OPTICA": "tecnología para transmitir información como pulsos luminosos a través de un conducto de fibra de vidrio.",
    "EMULACION":"emulation. Proceso de compatibilización entre computadoras mediante un software",
    "DOWNLOAD": "descargar, bajar. Transferencia de información desde Internet a una computadora.",
   "DATA": "datos información.",
   "COOKIE": "pequeño archivo de texto que un sitio web coloca en el disco rígido de una computadora que lo visita.",
   "BASE DE DATOS": "conjunto de datos organizados de modo tal que resulte fácil acceder a ellos gestionarlos y actualizarlos",
   "AUTOCAD": "programa de dibujo técnico.",
   "ANTIVIRUS": "programa que busca y eventualmente elimina los virus informáticos que pueden haber infectado un disco rígido o disquete.",
   "ANCHO DE BANDA" : "expresa la cantidad de datos que pueden ser transmitidos en determinado lapso En las redes se expresa en bps.",
   "ACCESO DIRECTO": "es un ícono que permite abrir más fácilmente un determinado programa o archivo.",
   "Hosting": "alojamiento. Servicio ofrecido por algunos proveedores, que brindan a sus clientes ",
   "HARWARE": "todos los componentes físicos de la computadora y sus periféricos",
   "Firewall": "mecanismo de seguridad que impide el acceso a una red.",
    "Ethernet": "tecnología para red de área local. Fue desarrollada originalmente por Xerox y posteriormente por Xerox, DEC e Intel. Ha sido aceptada como estándar por la ",
    "HTTP": "Hypertext Transfer Protocol Protocolo de transferencia de hipertextos Es un protocolo que permite transferir información en archivos de texto gráficos de video de audio y otros recursos multimedia.",
   "Jpg": "extensión de ciertos archivos gráficos. Véase JPEG.",
   "USB": "es una interfase de tipo plug  play entre una computadora y ciertos dispositivos por ejemplo teclados teléfonos escáneres e impresoras.",
   "Troyano" : "programa que contiene un código dañino dentro de datos aparentemente inofensivos.",
   "Toolbar": "barra de herramientas.",
   "Screen": "pantalla.",
}

 
# Luego llamas a la función mostrar_menu() para iniciar la interfaz gráfica
mostrar_menu()

