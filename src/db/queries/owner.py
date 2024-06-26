from src.db.database import Database
import json

def insert_data(flat_owner_id:int , flatno: int, bank_details: str, owner: json) -> None:
    conn = Database()
    print(owner)
    query = """
     INSERT INTO private_data.flat_owner_details(
               flat_owner_id,
               flatno,
               bank_details,
               owner)
     VALUES (%s, %s, %s, %s::jsonb) 
     RETURNING *;      
       """
    with conn.cursor() as cursor:

        cursor.execute(query, (flat_owner_id, flatno, bank_details, owner))
        owner = cursor.fetchone()
        conn.commit()
    return owner