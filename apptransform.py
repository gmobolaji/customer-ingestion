def clean_customer(customer):

    customer["email"] = customer["email"].lower()

    return customer
