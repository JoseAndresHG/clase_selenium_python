# language: es
Característica: Registro e inicio de sesión de usuario
  
Escenario: Registro exitoso de un usuario
    Dado que la pagina abre el registro
    Cuando el usuario se registra
    Entonces el usuario ve el mensaje "Your resgistration completed"


#Escenario: Inicio de sesión exitoso
  #  Dado que el usuario abre la página de inicio de sesión
   # Cuando inicia sesión con sus credenciales configuradas
    #Entonces el inicio de sesión es exitoso

##Escenario: Inicio de sesión rechazado con credenciales incorrectas
    #Dado que el usuario abre la página de inicio de sesión
    #Cuando intenta iniciar sesión con credenciales incorrectas
    #Entonces se muestra un error de credenciales