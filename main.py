from fastapi import FastAPI
from pydantic import BaseModel
import json
import datetime
from datetime import date
from operator import itemgetter
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Expense(BaseModel):
    amount: float
    category : str
    description: str
    transaction_date : datetime.date

@app.post("/add_expense/")
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


@app.get("/list_expense/")
async def list_expense(item_category: str | None = None):
    data = []
    new_data = []
    try :
        with open('user.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            if data:
                if item_category is not None:
                    if item_category in map(itemgetter('category'), data):
                        new_data[:] = [d for d in data if d.get('category') == item_category]
                        return new_data
                    else:
                        raise HTTPException(status_code=404, detail="No expense have been recorded for given category")
                else :
                    return data
            else :
                raise HTTPException(status_code=404, detail="No expense recorded")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No expense recorded")
    
@app.delete("/delete_expense/{expense_id}")
async def delete_expense(expense_id: int):
    new_data=[]
    data=[]
    try :
        with open('user.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="No expense recorded")
    except Exception as e:
        return {"message": f"Error: {e}"}
         
    if expense_id in map(itemgetter('id'), data):
        new_data[:] = [d for d in data if d.get('id') != expense_id]
        try :
            with open("user.json", "w") as file:
                json.dump(new_data, file, default=str)
            return {"message" : "Expense have been deleted"}
        except Exception as e: 
            return {"message": f"Error: {e}"}
    else :
        raise HTTPException(status_code=404, detail="The id you entered is not in the list")    
    
    