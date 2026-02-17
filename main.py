import uvicorn
from fastapi import FastAPI

from routers.optimize import router

app = FastAPI(title="GMPRO Optimization Service", version="1.0.0")
app.include_router(router, prefix="/optimize", tags=["optimize"])


@app.get("/")
def read_root():
    return {"message": "GMPRO API is running"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
