import psycopg2

con = psycopg2.connect(
  database="postgres_db", 
  user="postgres_user", 
  password="PasswordWithExtraSecurity", 
  host="localhost",
  port="5432:5432"
)

print("Database opened successfully")
