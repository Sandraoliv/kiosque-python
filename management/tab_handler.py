from menu import products


def calculate_tab(table: list[dict]):
    subtotal = 0

    for item in table:
        product_id = item["_id"]
        amount = item["amount"] 
        
        for product in products:     
            if product_id == product["_id"]:
                price = product["price"]
               
                subtotal += price * amount

    subtotal = round(subtotal, 2)
   
    return {"subtotal": f'${subtotal}'}
