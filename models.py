from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel
from enum import Enum 

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str
    phone_number: str 
    appointments: List["Appointments"] = Relationship(back_populates="user")

class Brands(Enum):
    HONDA="Honda"
    TOYOTA="Toyota"
    FORD="Ford"
    BMW="BMW"
    AUDI="Audi"
    TESLA="Tesla"
    MAZDA="Mazda"
    NISSAN="Nissan"
    SUBARU="Subaru"
    HYUNDAI="Hyundai"
    PORSCHE="Porsche"

class Appointments(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    car_description: Optional[str] = None
    repairs: str
    is_completed: bool = Field(default=False)
    # fk
    user_id: int = Field(foreign_key="user.id")
    user: Optional[User] = Relationship(back_populates="appointments")
    payment_status: bool = Field(default=False)
    price: float = Field(default=100)
    brands: Brands|None = None

