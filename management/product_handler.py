from menu import products


def get_product_by_id(num):

    if type(num) is not int:
        raise TypeError("product id must be an int")
    for product in products:
        if product['_id'] == num:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) is not str:
        raise TypeError("product type must be a str")

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


def menu_report():
   
    product_count = len(products)
    total_price = 0
    for product in products:
        total_price += product['price']
    
    average_price = round(total_price / product_count, 2)
    type_counts = {}
    for product in products:
        product_type = product['type']
        type_counts[product_type] = type_counts.get(product_type, 0) + 1
    
    most_common_type = max(type_counts, key=type_counts.get)
    report = f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"
                
    return report
