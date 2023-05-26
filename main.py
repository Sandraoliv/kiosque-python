
from management.product_handler import *
from management.tab_handler import *


def main():
    # print(get_product_by_id(8))
    # print(get_products_by_type("drink"))
    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
    }

    # print(add_product(products, **new_product))
    # print(add_product([], **new_product))
    # print(products)
    table_1 = [{"_id": 21, "amount": 5}, {"_id": 102, "amount": 5}]
    print(calculate_tab(table_1))


if __name__ == "__main__":
     
    ...
    main()
