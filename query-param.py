''''''


import fastapi
import json
from fastapi import fastapi ,path, HTTPException

app=fastapi()


def load_data():
    with open ('patient.json' , 'r') as f:
        data=json.load(f)

    return data

@app.get('/')
def hello():



@app.get('view/')
def view():
    data=load_data()
    return data
 

@app.get('/patient/{patient_id}')

'''path paramenter'''


def view_patient(patient_id: str = Path(..., description='ID of the patient in database , example: patient_id=P001')):
    data=load_data();


    if patient_id in data:
        return data[patient_id]
    else:
        return { 'Patient nopt found' }

@app.get('/sort')
def sort_patients(sort_by: str=Query(..., description='sorted patients by height, weight , bmi'), order:str=Query('asc', description= 'sort by asc or desc')):
    fields=['bmi', 'height', 'weight']
    if sort_by not in fields:
        raise HTTPException(status_code= 400, detail='invalid field')
    if order_by not in fields:
            raise HTTPException(status_code= 400, detail='invalid field')

    data=load_data()
    sort_order=True if order == 'desc' else false
    sorted_data=sorted(data.values(), key=lambda x: x.get(sort_by , 0) reverse=sort_order)

    return sorted_data