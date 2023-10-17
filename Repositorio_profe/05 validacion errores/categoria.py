while True:
    try:
        cat = int(input("Ingrese una categoria (1, 2, o 3): "))
        if cat < 1 or cat > 3:
            print("Categoria inválida. Ingrese 1 o 2 o 3")
            continue
        break
    except ValueError:
        print("Error. Categoría inválida.")