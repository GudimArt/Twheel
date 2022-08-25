from database import create_db_and_tables


from controllers.tour_controller import router_tour_controller
from controllers.route_controller import router_route_controller
from controllers.place_controller import router_place_controller
from controllers.user_conroller import auth_backend, current_active_user, fastapi_users


from models.user import User
from schemas.user_schema import UserCreate, UserRead, UserUpdate

from fastapi import FastAPI, Depends
from fastapi import APIRouter


app = FastAPI()
router = APIRouter()

app.include_router(router_tour_controller, tags=["tour_controller"])
app.include_router(router_route_controller, tags=["rout_controller"])
app.include_router(router_place_controller, tags=["place_controller"])

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.name}!"}


@app.get("/")
async def root():
    return '1'

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
    