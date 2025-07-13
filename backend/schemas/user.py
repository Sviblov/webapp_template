from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str
