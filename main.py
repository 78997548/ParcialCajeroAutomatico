from cajero import Cajero

def main():
    cajero = Cajero()

    if cajero.iniciar_sesion():
        cajero.mostrar_menu()

if __name__ == "__main__":
    main()
