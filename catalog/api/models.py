from django.db import models
from ninja import Schema
from typing import List

class MessageSchema(Schema):
    message: str

#input el usuario crea el articulo
    #crea el articulo
class ServiceInputSchema(Schema): 
    price: float
    thru_date: str 

class ContactOutputSchema(Schema):
    id: int
    provider: str
    type: str
    first_name: str
    last_name: str
    phone: str
    email: str
    mobile: str

class AddressOutputSchema(Schema):
    id: int
    address1: str
    address2: str
    zipcode: str
    country: str
    city: str
    region: str

class ProviderOutputSchema(Schema):
    id: int
    fantasy_name: str
    text_name: str
    taxt_id: str
    is_active: bool
    contacts: List[ContactOutputSchema]
    addresses: List[AddressOutputSchema]

class ServiceOutputSchema(Schema): 
    id: int
    name: str
    description: str
    price: float
    from_date: str 
    thru_date: str 
    provider: ProviderOutputSchema


