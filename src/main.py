from fastapi import FastAPI
from pydantic import BaseModel
import uuid
from typing import List, Dict
import math

class Item(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    total: str
    items: List[Item]

receipts_store: Dict[str, Receipt] = {}

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post('/receipts/process')
def process_receipts(receipt: Receipt):
    id = str(uuid.uuid4())
    receipts_store[id] = receipt
    return {"id": id}


def calculate_points(receipt: Receipt):
    points = 0
    
    # One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt.retailer)

    # 50 points if the total is a round dollar amount with no cents
    try:
        total_value = float(receipt.total)
        if total_value.is_integer():
            points += 50
    except ValueError:
        pass

    # 25 points if the total is a multiple of 0.25
    if total_value % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt
    points += (len(receipt.items) // 2) * 5

    # If the trimmed length of the item description is a multiple of 3, 
    # multiply the price by 0.2 and round up to the nearest integer
    for item in receipt.items:
        description_trimmed = item.shortDescription.strip()
        if len(description_trimmed) % 3 == 0:
            item_price = float(item.price)
            points += math.ceil(item_price * 0.2)

    # 6 points if the day in the purchase date is odd
    day = int(receipt.purchaseDate.split("-")[2])
    if day % 2 == 1:
        points += 6

    # 10 points if the time of purchase is after 2:00 pm and before 4:00 pm
    purchase_hour = int(receipt.purchaseTime.split(":")[0])
    if 14 <= purchase_hour < 16:
        points += 10

    return points

@app.get('/receipts/{id}/points')
def get_points(id: str):
    resp = {}
    if id in receipts_store:
        resp['points'] = calculate_points(receipts_store[id])
    return resp 
