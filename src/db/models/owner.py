from typing import Optional
from src.db.queries import owner as owner_queries
import json

class Owner:
    def __init__(self, flat_owner_id: int, flatno: int, bank_details: str, owner: dict) -> None:
        self.flat_owner_id = flat_owner_id
        self.flatno = flatno
        self.bank_details = bank_details
        self.owner = owner

    @classmethod
    def insert_data(cls, flat_owner_id: int, flatno: int, bank_details: str, owner: dict) -> Optional['Owner']:
        owner: tuple[str] = owner_queries.insert_data(flat_owner_id, flatno, bank_details, owner)

        return cls(*owner) if owner else None
    
