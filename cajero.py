# cajero.py

class Cajero:
    def __init__(self):
        self.usuario_correcto = "Wesley Rivera"
        self.pin_correcto = "2007"
        self.saldo_actual = 10000.0
        self.intentos = 0
        self.max_intentos = 3

    def iniciar_sesion(self):
        while self.intentos < self.max_intentos:
            usuario = input("Ingrese su usuario: ")
            pin = input("Ingrese su contaceña: ")

            if usuario == self.usuario_correcto and pin == self.pin_correcto:
                print("Inicio de secion exitoso.")
                return True
            else:
                self.intentos += 1
                print(f"Usuario o la contraceña son incorrectos. Intento {self.intentos}/{self.max_intentos}.")

            if self.intentos == self.max_intentos:
                print("Muchos intentos fallidos. La Cuenta ha sido bloqueada.")
                return False

    def mostrar_menu(self):
        while True:
            print("Menú de opciones")
            print("1. Consultar saldo")
            print("2. Realizar un retiro")
            print("3. Salir")

            opcion = input("Seleccione una occion: ")

            if opcion == "1":
                self.consultar_saldo()
            elif opcion == "2":
                self.realizar_retiro()
            elif opcion == "3":
                print("Gracias por usar el cajero automatico, saliendo.")
                break
            else:
                print("Opcion no valida, intente nuevamente.")

    def consultar_saldo(self):
        print(f"Su saldo actual es: ${self.saldo_actual:.2f}")

    def realizar_retiro(self):
        try:
            monto = float(input("Ingrese la cantidad a retirar: "))
            if monto <= 0:
                print("Ingrese un monto válido.")
            elif monto > self.saldo_actual:
                print("su saldo es insuficiente para realizar el retiro.")
            else:
                self.saldo_actual -= monto
                print(f"El retiro se ha hecho con exito. Su nuevo saldo es: ${self.saldo_actual:.2f}")
        except ValueError:
            print("Ingrese un numero valido.")
