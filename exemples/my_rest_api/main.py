from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

#from fastapi.staticfiles import StaticFiles
from devise_api import router as devise_router
from fastapi.responses import HTMLResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(devise_router);

@app.get("/" , response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head><title>main</title></head>
    <body>
        <h3>devise-api rest</h3>
        <a href="./devise-api/v1/devises/EUR"> devise EUR</a> <br/>
        <a href="./devise-api/v1/devises"> all devises</a> <br/>
        <hr/>
        <a href="./docs" target="_new" >devise-api docs</a><br/>
        <hr/>
        <a href="./static/index.html" target="_new" >index of embedded mini front-end</a><br/>
    </body>
    </html>
    """
