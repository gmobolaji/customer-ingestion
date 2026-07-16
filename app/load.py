from db import get_connection
def load_customer(customer):
 conn = get_connection()
 cursor = conn.cursor()
 cursor.execute(
  """
  INSERT INTO customers
  (customer_id, customer_name, email)
  VALUES (%s,%s,%s)
  ON CONFLICT (customer_id)
  DO NOTHING
  """,
  (
   customer["id"],
   customer["name"],
   customer["email"]
  )
)

conn.commit()

cursor.close()
conn.close()
