from typing import Optional
from src.db.queries import flat as flat_queries


class Flat: 
    def __init__(self, floorno: int, flatno: int, furnished: str, facilities: str,propertytype:str,area_in_m2:int,price_range:str,available_from:str) -> None:
        self.floorno = floorno
        self.flatno = flatno
        self.furnished = furnished
        self.facilities = facilities
        self.propertytype = propertytype
        self.area_in_m2 = area_in_m2
        self.price_range = price_range
        self.available_from = available_from

    @classmethod
    def insert_data(cls, floorno: int, flatno: int, furnished: str, facilities: str,propertytype:str,area_in_m2:int,price_range:str,available_from:str) -> Optional['Flat']:
        flat: tuple[str] = flat_queries.insert_data(floorno, flatno, furnished, facilities,propertytype,area_in_m2,price_range,available_from)

        return cls(*flat) if flat else None
