from fastapi import Depends, FastAPI
from controllers.apples import router as ApplesRouter

app = FastAPI()


app.include_router(ApplesRouter,prefix='/api/apples')