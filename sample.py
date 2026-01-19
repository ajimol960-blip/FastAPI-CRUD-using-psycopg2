import psycopg2

# 1. Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="taskdb",
    user="postgres",
   password="MyPostgres@2026",
    port="5432"
)







