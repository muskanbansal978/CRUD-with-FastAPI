from fastapi import FastAPI,Path
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
student_details ={
    1:{
        "name":"Muskan",
        "age":25,
        "gender":"Female"
        }
}

class Student(BaseModel):
    name:str
    age:int
    gender:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    gender:Optional[str]=None


@app.get('/')
def index():
    return "Hi Students! Let's practice FastAPI."

@app.get('/student-info/{student_id}')
def students_by_id(student_id:int = Path(description ="Enter the Student ID you want to view",gt=0)):
    return student_details[student_id]

@app.get('/student-info-by-name')
def students_by_name(*,student_id:int=None,name:str=None):
    for id in student_details:
        if student_details[id]["name"] == name or id==student_id:
            return student_details[student_id]
    return {"message":"Data not found"}

@app.post('/create-student/{student_id}')
def create_student(student_id:int,student:Student):
    for id in student_details:
        if id == student_id:
            return {"Error":"Student already exists"}
    student_details[student_id]=student
    return student_details[student_id]

@app.put('/update-student/{student_id}')
def update_student(student_id:int,student:UpdateStudent):
    if student_id not in student_details:
        return {"Error":"Student does not exist"}
    if student.name != None:
        student_details[student_id]["name"] = student.name
    
    if student.age != None:
        student_details[student_id]["age"] = student.age
    
    if student.gender != None:
        student_details[student_id]["gender"] = student.gender

    return student_details[student_id]

@app.delete('/delete-student/{student_id}')
def delete_student(student_id:int):
    if student_id not in student_details:
        return {"Error":"Student doesn't exist"}
    del student_details[student_id]
    return {"Message":"Student record deleted successfully"}




