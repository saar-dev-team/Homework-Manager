from fastapi import FastAPI,status,HTTPException
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("application startup")
    yield 
    print("application shutdown")


app = FastAPI()
homework_dict = {}


@app.get("/all_homework")
def get_all_homework ():
    return homework_dict

@app.post("/new-homework")
def creat_a_new_homework(lesson: str, topic: str, deadline: str, priority: int):  
    if not 1 <= priority <= 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Priority must be between 1 and 5.")
    if topic.lower() == "exam":
        priority = 1
    homework_id = 1
    while f"homework_{homework_id}" in homework_dict:
        homework_id += 1
    homework_dict[f"homework_{homework_id}"] = {
        "lesson": lesson,
        "topic": topic,
        "deadline for homework": deadline,
        "priority(1 to 5)": priority
    }
    raise HTTPException(
        status_code = status.HTTP_201_CREATED,
        detail = "new homework succesfuly created !"
    )


@app.get("/homework")
def get_one_homework(homework_id: int):
    homework_in = homework_dict.get(f"homework_{homework_id}")
    if homework_in is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Homework not found"
        )
    return homework_in