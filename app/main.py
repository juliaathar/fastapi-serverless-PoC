from fastapi import FastAPI
from .routers import user
from .database import Base, engine
from mangum import Mangum

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='PoC FastAPI com AWS',
    description='Teste de projeto de API python com FastAPI fazendo deploy pra AWS'
)

handler = Mangum(app)

app.include_router(user.router)

@app.get('/')
def read_root():
    return {'Hello': 'World'} 