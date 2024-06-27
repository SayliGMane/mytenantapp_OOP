from src.db.database import Database
import json

def insert_data(floorno: int, flatno: int, furnished: str, facilities: str,propertytype:str,area_in_m2:int,price_range:str,available_from:str) -> None:
    conn = Database()
    
    query = """
     INSERT INTO private_data.flat_owner_details(
               floorno,
               flatno,
               furnished,
               facilities,
               propertytype,
               area_in_m2,
               price_range,
               available_from)
     VALUES (%s, %s, %s, %s,%s, %s, %s, %s) 
     RETURNING *;      
       """
    with conn.cursor() as cursor:

        cursor.execute(query, (floorno, flatno, furnished, facilities,propertytype,area_in_m2,price_range,available_from))
        owner = cursor.fetchone()
        conn.commit()
    return owner