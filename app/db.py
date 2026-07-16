from pathlib import Path
import psycopg2

def get_connection():

 return psycopg2.connect(
  host="postgres",
  database="warehouse"
  user="postgres",
  password="password"
  port=5432
)

def initialize_database():
 conn = get_connection()
 cur = conn.cursor()
 
 sql = Path("/app/sql/create_tables.sql").read_text()
 cur.execute(sql)
 conn.commit()
 
 cur.close()
 conn.close()
