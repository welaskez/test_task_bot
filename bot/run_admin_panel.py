import uvicorn
from fastapi import FastAPI
from utils.init_admin_panel import create_admin_panel

app = FastAPI()
create_admin_panel(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
