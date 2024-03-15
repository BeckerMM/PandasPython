from typing import Union
import teste
from fastapi import FastAPI

app = FastAPI()


@app.get("/{time}/{ano}")
async def read_root(time: str, ano: int):
    return teste.obter_resultados_do_time(time,ano)
