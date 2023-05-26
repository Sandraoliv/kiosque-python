from menu import products


def get_product_by_id(num):
    
    for product in products:
        if product['_id'] == num:
            return product
    return {}        


def get_products_by_type(product_type):
    found_products = []
    for product in products:

        if product['type'] == product_type:
            found_products.append(product)   
    return found_products       


def add_product(products, **kwargs):
    if len(products) == 0:
        new_id = 1
    else:
        max_id = max(product["_id"] for product in products)
        new_id = max_id + 1

    kwargs["_id"] = new_id

    products.append(kwargs)

    return kwargs