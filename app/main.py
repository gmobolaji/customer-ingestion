from db import initialize_database
initialize_database()

from extract import get_customers
from transform import clean_customer
from load import load_customer

customers = get_customers()

for customer in customers:

    cleaned_customer = clean_customer(customer)
    load_customer(cleaned)


    print("Pipeline completed successfully.")
