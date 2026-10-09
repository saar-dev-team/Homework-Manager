from fastapi import FastAPI,status,HTTPException


app = FastAPI()
homework_dict = {"00/00/0000":"a string"}

@app.get("/all_homework")
def get_all_homework ():
    return homework_dict

@app.post("/new-homework")
def creat_a_new_homework(date: str, homework: str):
    homework_dict[date] = homework
    raise HTTPException(status_code=status.HTTP_201_CREATED,detail="homework succesfully created")