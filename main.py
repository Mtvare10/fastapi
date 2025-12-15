from fastapi import FastAPI


app = FastAPI()


@app.get("/")

def index():
    return {"data": {"name" : "nika"}}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished data"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data" : id}

@app.get("/blog/{id}/comments")
def comments(id: int):
    return {"data" : {"1", "2", "3"}}



