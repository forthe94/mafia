import random

from fastapi import FastAPI

app = FastAPI(title="Mafia Game API")


roles = ['p', 'p', 'm', 'm']
roles_count = len(roles)

@app.get("/role/")
def read_games():
    print(roles)
    return roles.pop(random.randrange(len(roles))), roles_count

@app.post("/roles/{mafia_count}/{peace_count}")
def set_roles(mafia_count: int, peace_count: int):
    roles = 'm' * mafia_count + 'p' * peace_count
    roles_count = len(roles)
    return 'ok'

@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}
