from appextract import get_customers
from apptransform import clean_customer
from appload import load_customer


customers = get_customers()

for customer in customers:

    clean = clean_customer(customer)

    load_customer(clean)
