from fastapi import FastAPI,status,HTTPException
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("application startup")
    yield 
    print("application shutdown")


app = FastAPI()
homework_dict = {"00/00/0000":"a string"}

@app.get("/all_homework")
def get_all_homework ():
    return homework_dict

@app.post("/new-homework")
def creat_a_new_homework(date: str, homework: str):
    homework_dict[date] = homework
    raise HTTPException(status_code=status.HTTP_201_CREATED,detail="homework succesfully created")

@app.get("/homework")
def get_one_homework(date: str):
    homework_in = homework_dict.get(date)
    if homework_in is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Homework not found"
        )
    return homework_in