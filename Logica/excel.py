import datetime

# Diccionarios para almacenar productos y ventas
products = {}  # clave: id del producto, valor: diccionario con datos del producto
sales = []     # lista de ventas, cada venta es un diccionario

# Funciones para la gestión de productos

def add_product():
    product_id = input("Ingrese el ID del producto: ")
    if product_id in products:
        print("El producto ya existe.")
        return
    name = input("Ingrese el nombre del producto: ")
    description = input("Ingrese la descripción del producto: ")
    try:
        price = float(input("Ingrese el precio unitario: "))
    except ValueError:
        print("Precio inválido.")
        return
    status = input("Estado (Activo/No activo): ")
    products[product_id] = {
        "name": name,
        "description": description,
        "price": price,
        "status": status
    }
    print("Producto agregado exitosamente.")

def update_product():
    product_id = input("Ingrese el ID del producto a actualizar: ")
    if product_id not in products:
        print("El producto no existe.")
        return
    print("Producto actual:")
    print(products[product_id])
    name = input("Ingrese el nuevo nombre (deje vacío para no cambiar): ")
    description = input("Ingrese la nueva descripción (deje vacío para no cambiar): ")
    price_input = input("Ingrese el nuevo precio unitario (deje vacío para no cambiar): ")
    status = input("Ingrese el nuevo estado (deje vacío para no cambiar): ")
    if name:
        products[product_id]["name"] = name
    if description:
        products[product_id]["description"] = description
    if price_input:
        try:
            price = float(price_input)
            products[product_id]["price"] = price
        except ValueError:
            print("Precio inválido, no se actualizó.")
    if status:
        products[product_id]["status"] = status
    print("Producto actualizado.")

def list_products():
    if not products:
        print("No hay productos registrados.")
        return
    print("\n--- Lista de Productos ---")
    for pid, info in products.items():
        print(f"ID: {pid}, Nombre: {info['name']}, Precio: {info['price']}, Estado: {info['status']}")

def delete_product():
    product_id = input("Ingrese el ID del producto a eliminar: ")
    if product_id in products:
        del products[product_id]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")

def manage_products():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Listar productos")
        print("4. Eliminar producto")
        print("5. Volver al menú principal")
        choice = input("Seleccione una opción: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            list_products()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Opción no válida.")

# Funciones para el registro de ventas

def register_sale():
    sale_id = "V" + str(len(sales)+1).zfill(3)
    sale_date = datetime.datetime.now()
    items = []
    total = 0.0
    while True:
        print("\n--- Agregar producto a la venta ---")
        product_id = input("Ingrese el ID del producto (o 'fin' para terminar): ")
        if product_id.lower() == 'fin':
            break
        if product_id not in products:
            print("Producto no encontrado.")
            continue
        try:
            quantity = int(input("Ingrese la cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            continue
        price = products[product_id]["price"]
        subtotal = quantity * price
        item = {
            "product_id": product_id,
            "quantity": quantity,
            "price": price,
            "subtotal": subtotal
        }
        items.append(item)
        total += subtotal
        print(f"Subtotal para este producto: {subtotal}")
    if not items:
        print("No se registraron productos en la venta.")
        return
    print(f"\nTotal de la venta: {total}")

    # Selección del método de pago
    print("\nSeleccione método de pago:")
    print("1. Efectivo")
    print("2. Transferencia")
    print("3. Cuenta (deuda)")
    payment_option = input("Ingrese opción: ")
    if payment_option == "1":
        payment_method = "Efectivo"
    elif payment_option == "2":
        payment_method = "Transferencia"
    elif payment_option == "3":
        payment_method = "Cuenta pendiente"
    else:
        print("Opción no válida, se considerará como 'Cuenta pendiente'")
        payment_method = "Cuenta pendiente"
    
    comprobante = ""
    if payment_method in ["Efectivo", "Transferencia"]:
        comprobante = input("Ingrese número de comprobante (opcional): ")

    sale = {
        "sale_id": sale_id,
        "date": sale_date,
        "items": items,
        "total": total,
        "payment_method": payment_method,
        "comprobante": comprobante
    }
    sales.append(sale)
    print(f"Venta {sale_id} registrada exitosamente.")

def list_sales():
    if not sales:
        print("No hay ventas registradas.")
        return
    print("\n--- Historial de Ventas ---")
    for sale in sales:
        print("\n---------------------------------")
        print(f"ID Venta: {sale['sale_id']}")
        print(f"Fecha: {sale['date'].strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Método de Pago: {sale['payment_method']}")
        if sale['comprobante']:
            print(f"N° Comprobante: {sale['comprobante']}")
        print("Productos:")
        for item in sale["items"]:
            product = products.get(item["product_id"], {})
            product_name = product.get("name", "Desconocido")
            print(f"  - {product_name} (ID: {item['product_id']}), Cantidad: {item['quantity']}, Precio: {item['price']}, Subtotal: {item['subtotal']}")
        print(f"Total de la venta: {sale['total']}")
        print("---------------------------------")

# Menú principal

def main_menu():
    while True:
        print("\n=== Sistema POS ===")
        print("1. Gestión de Productos")
        print("2. Registrar Venta")
        print("3. Listar Ventas")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        if option == "1":
            manage_products()
        elif option == "2":
            register_sale()
        elif option == "3":
            list_sales()
        elif option == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main_menu()
