from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Building REST APIs com FastAPI")


class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = ""
    price: float = Field(..., gt=0)


class Item(ItemCreate):
    id: int


items_db: dict[int, Item] = {}
next_id = 1


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    global next_id
    item = Item(id=next_id, **payload.model_dump())
    items_db[next_id] = item
    next_id += 1
    return item


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    return list(items_db.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate) -> Item:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    updated = Item(id=item_id, **payload.model_dump())
    items_db[item_id] = updated
    return updated


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int) -> None:
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")

    del items_db[item_id]
