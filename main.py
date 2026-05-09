from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select
from typing import Optional
from database import create_db_and_tables, get_session
from models import Appointments, User

app = FastAPI()


# func to create tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users/", response_model=list[User])
def read_users(user_id: Optional[int] = None, session: Session = Depends(get_session)):
    if user_id:
        statement = select(User).where(User.id == user_id)
        results = session.exec(statement).all()

        if not results:
            raise HTTPException(status_code=404, detail="User not found")
        return results

    users = session.exec(select(User)).all()
    return users

@app.post("/appointments/", response_model=Appointments)
def create_todo(appointment: Appointments, session: Session = Depends(get_session)):
    session.add(appointment)
    session.commit()
    session.refresh(appointment)
    return appointment


# @app.get("/users/{user_id}/todos", response_model=list[Todo])
# def read_user_todos(user_id: int, session: Session = Depends(get_session)):
#     user = session.get(User, user_id)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user.todos