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
        print(cat_a_obj.registro)
        return True
    elif operacion == 2:
        alerta_retiro = cat_a_obj.retiro(cantidad, descripcion)
        return alerta_retiro
    elif operacion == 3:
        alerta_transferencia = ''
        if cat_a_obj == cat_b_obj:
            alerta_operacion = 'catg_igual'
            return alerta_operacion
        else:
            cat_a_obj.transferir(cantidad, cat_b_obj)
            print(cat_a_obj.registro)
            print(cat_b_obj.registro)