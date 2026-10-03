from fastapi import FastAPI
from pydantic import BaseModel
import json
import datetime
from datetime import date

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category : str
    description: str
    transaction_date : datetime.date

@app.post("/items/")
async def add_expense(item: Expense):
    item_dict = item.model_dump()
    data_existed = []
    #read existed file to count id
    try :
        with open('user.json', 'r', encoding='utf-8') as file:
            data_existed = json.load(file)
            if data_existed:
                new_data_id = max(data_existed, key=lambda x:x['id'])["id"]+1
            else:
                new_data_id = 1 
    except FileNotFoundError:
        new_data_id = 1
    
    item_dict["id"] = new_data_id
    item_dict["created_at"] = date.today()
    data_existed.append(item_dict) #append new data to existed data and write it to file
    try :
        with open("user.json", "w") as file:
            json.dump(data_existed, file, default=str)
    except Exception as e: 
        print(e)
    return item_dict