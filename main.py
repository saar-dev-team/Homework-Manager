from fastapi import FastAPI


app = FastAPI()
homework_dict = {"00/00/0000":"a string"}

@app.get("/all_homework")
def get_all_homework ():
    return homework_dict