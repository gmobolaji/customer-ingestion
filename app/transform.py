def clean_customer(customer):

	return{
		"id": customer["id"],
		"name": customer["name"],
		"email": customer["email"].lower()

	}

