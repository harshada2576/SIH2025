# Proposed Workflow

---

## Backend Dev Workflow

- Create a model: app/db/models/appointment.py
- Create schema: app/schemas/appointment.py
- Write CRUD: app/crud/appointment.py
- Write route: app/api/endpoints/appointments.py
- Register route in main.py
- Test route in Postman or frontend

---

## Frontend Dev Workflow

- Work inside frontend/templates/ and frontend/static/
- Link to backend via JS fetch() or HTML forms (FastAPI Jinja2)

---

## Docs Team Workflow

- Use docs/README.md for internal notes
- Place all PPTs, design diagrams in docs/
