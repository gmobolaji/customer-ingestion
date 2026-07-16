from extract import get_customers
from transform import clean_customer


customers = get_customers()

for customer in customers:

    cleaned_customer = clean_customer(customer)

    print(cleaned_customer)
