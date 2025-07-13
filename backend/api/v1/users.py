from fastapi import APIRouter, Depends
from db.session import get_repo
from db.repo.requests import RequestsRepo
from api.deps import get_current_user
from db.models.user import User

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/verify", summary="Verify User Authentication")
async def verify_token():
    return {"status": "ok"}


@router.get("/getuser", summary="Verify User Authentication")
async def get_user_info(repo: RequestsRepo = Depends(get_repo), current_user = Depends(get_current_user)):
    user: User = await repo.users.get_by_username(current_user["username"])
    return user
