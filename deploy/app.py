from fastapi import FastAPI, Request, Form  
from fastapi.templating import Jinja2Templates  
import csv  
from datetime import datetime  
import uvicorn
import csv  
from datetime import datetime  
  
app = FastAPI()
csv_file_path = 'birthdays.csv'

def lookup_birthday(csv_file_path):  
    today = datetime.today().strftime('%d/%m')  
    birthdays = []  
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:  
        reader = csv.DictReader(csvfile)  
        for row in reader:  
            if row['Birthday'] == today:  
                birth_year = int(row['Birthyear'])  
                age = datetime.now().year - birth_year  
                birthdays.append((row['fullName'], age))  
        return birthdays if len(birthdays) > 0 else None  
    
def lookup_merkeday(csv_file_path):
    today = datetime.today().strftime('%d/%m')
    merkedag = []  
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:  
        reader = csv.DictReader(csvfile, delimiter=';')  
        for row in reader: 
            if row['dato'] == today:  
                merkedag.append((row['merkedag'])) 
        return merkedag if len(merkedag) > 0 else None
    
def lookup_sitat(csv_file_path):
    today = datetime.today().strftime('%d/%m')  
    sitat = []  
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:  
        reader = csv.DictReader(csvfile)  
        sitat = reader.sample(1)
        return sitat if len(sitat) > 0 else None

@app.get("/")  
def read_root():  
    return {"message": "Hello World"}  
  
@app.get("/bursdag")  
def index(request: Request):
    birthdays = lookup_birthday(csv_file_path)  
    return birthdays if birthdays else "Ingen bursdager idag"

@app.get("/merkedag")  
def index(request: Request):
    merkedag = lookup_merkeday(csv_file_path)  
    return merkedag if merkedag else "Ingen merkedag idag"

@app.get("/sitat")  
def index(request: Request):
    sitat = 'Ipso facto'
    return sitat if sitat else "Ingen sitat idag"

if __name__ == "__main__":  
    uvicorn.run(app, host="0.0.0.0", port=8080)