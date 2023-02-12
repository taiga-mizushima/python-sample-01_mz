from dataclasses import dataclass

@dataclass
class DataClassCard:
    as_of_date: str
    business_key: str
    status: str
    amount: int