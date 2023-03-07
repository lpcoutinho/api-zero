from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    nome: str
    valor: float
    disponivel: bool = None


@app.get("/")
def read_root():
    return {"API": "funcionando"}


@app.get("/itens/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/itens/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_nome": item.nome, "item_id": item_id}
