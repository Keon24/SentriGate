from fastapi import FastAPI, Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from users.auth import create_access_token
from database.schema import User, Token, UserInDB
from users import UserModel, get_password_hash, authenticate_user
from database import get_db
from core.dependecies import get_current_user


app = FastAPI()

@app.post('/token', response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db,form_data.username, form_data.password )
    print(user)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="inccorect username and passowrd",
            headers={'WWW-Authentication': "Bearer"},
        )
    access_token = create_access_token(data={'sub':user.username})
    return {"access_token":access_token, "token_type:": "bearer"}
    
@app.get('users/me')    
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("create/users")
def create_users(user: User, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="username aleadye exist"
        )

@app.get('/')
def home_page():
    return{"message":"backend is now running"}


    