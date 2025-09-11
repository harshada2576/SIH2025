from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Template and static file setup
templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Dummy user for demonstration
DUMMY_USER = {
    "username": "admin",
    "password": "password123"
}


@app.get("/", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})


@app.post("/login", response_class=HTMLResponse)
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    if username == DUMMY_USER["username"] and password == DUMMY_USER["password"]:
        # Replace this with a redirect or dashboard
        return HTMLResponse(f"<h2>Welcome, {username}!</h2>")
    else:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Invalid username or password."
        })

