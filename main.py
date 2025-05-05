from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir chamadas do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados simulado
products = []

# Modelo de dados
class Product(BaseModel):
    name: str
    price: float
    category: str

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message": "Produto adicionado com sucesso!", "product": product}

@app.get("/products")
def get_products():
    return products
