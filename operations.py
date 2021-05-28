from budget import categoria

def realizar_operacion(operacion, cantidad, descripcion, cat_a, cat_b, dict_categorias):
    if cat_a not in dict_categorias.keys():
        dict_categorias[cat_a] = categoria(cat_a)
    if cat_b not in dict_categorias.keys():
        dict_categorias[cat_b] = categoria(cat_b)

    cat_a_obj = dict_categorias[cat_a]
    cat_b_obj = dict_categorias[cat_b]

    if operacion == 1:
        cat_a_obj.deposito(cantidad, descripcion)
    elif operacion == 2:
        cat_a_obj.retiro(cantidad, descripcion)
    elif operacion == 3:
        if cat_a_obj.nombre == cat_b_obj.nombre:
            return False
        else:
            cat_a_obj.transferir(cantidad, cat_b)
    print(cat_a_obj.registro)
    return True