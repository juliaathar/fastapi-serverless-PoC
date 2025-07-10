from fastapi import FastAPI
from .routers import user
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='PoC FastAPI com AWS',
    description='Teste de projeto de API python com FastAPI fazendo deploy pra AWS'
)

app.include_router(user.router)

@app.get('/')
def read_root():
    return {'Hello': 'World'} 