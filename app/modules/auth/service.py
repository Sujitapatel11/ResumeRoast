from sqlmodel import Session, select
from typing import Optional
from app.modules.auth.models import User
from app.modules.auth.schemas import UserCreate
from app.modules.auth.security import get_password_hash, verify_password
from fastapi import HTTPException, status

def get_user_by_email(session: Session, email: str) -> Optional[User]:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()

def register_user(session: Session, user_in: UserCreate) -> User:
    existing = get_user_by_email(session, user_in.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )
    db_user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        full_name=user_in.full_name or ""
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def authenticate_user(session: Session, email: str, password: str) -> User:
    user = get_user_by_email(session, email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password."
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User account is inactive."
        )
    return user
