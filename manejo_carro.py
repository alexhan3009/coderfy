def encender_carro():
    print("\n🔑 Girando la llave... ¡Carro encendido!")

def apagar_carro():
    print("\n🛑 Apagando el carro...")

def acelerar():
    print("\n🚗💨 Acelerando...")

def frenar():
    print("\n✋ Frenando...")

def girar(direccion):
    print(f"\n🔄 Girando a la {direccion}...")

def manejar_carro():
    gasolina = input("⛽ ¿El carro tiene gasolina? (si/no): ").strip().lower()

    if gasolina != "si":
        print("\n⚠️ No puedes encender el carro. ¡No hay gasolina!")
        return

    encender_carro()

    while True:
        print("\n--- Opciones ---")
        print("1. Acelerar")
        print("2. Frenar")
        print("3. Girar a la izquierda")
        print("4. Girar a la derecha")
        print("5. Apagar el carro")

        opcion = input("\nElige una opción (1-5): ").strip()

        if opcion == "1":
            acelerar()
        elif opcion == "2":
            frenar()
        elif opcion == "3":
            girar("izquierda ↩️")
        elif opcion == "4":
            girar("derecha ↪️")
        elif opcion == "5":
            apagar_carro()
            break
        else:
            print("\n❌ Opción no válida, intenta de nuevo.")

    print("\n✅ Fin del programa. 🚗")

# Ejecutar la función principal
manejar_carro()
