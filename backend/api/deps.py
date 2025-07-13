from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")