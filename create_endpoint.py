import fastapi
import json
import pydantic from BaseModel
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


    ''' HTTP Exception'''
'''raise HTTPException(status_code=404 , details='patient not found')'''
