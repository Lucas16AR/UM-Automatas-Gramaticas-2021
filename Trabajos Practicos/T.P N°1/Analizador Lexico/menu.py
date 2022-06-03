import email
import url
import ip
import contraseña

def main():
   while True:

      print("Bienvenidos, seleccione una opción")
      print("Opción 1 EMAIL")
      print("Opción 2 URL")
      print("Opción 3 DIRECCIÓN IP")
      print("Opción 4 CONTRASEÑA")
      print("Opción 5 SALIR\n")
      opcion = int(input("Opción: "))
      if (opcion == 1):
         email.mail()
         input("\nPresione enter para continuar ")
      elif (opcion == 2):
         url.dir()
         input("\nPresione enter para continuar ")
      elif (opcion == 3):
         ip.direccion()
         input("\nPresione enter para continuar ")
      elif (opcion == 4):
         contraseña.contra()
         input("\nPresione enter para continuar ")
      elif (opcion == 5):
         exit(print("""Gracias por usar este analizador
Un trabajo realizado por Daniel Beato & Lucas Galdame"""))
      else:
         print("La opcion ingresada es incorrecta")

main()