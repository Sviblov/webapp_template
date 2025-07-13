
from sqlalchemy import Column, Integer, String
from db.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import TIMESTAMP
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
    is_admin = Column(Integer, default=0)  
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    
    
    # 1 for admin, 0 for regular user
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, is_active={self.is_active}, is_admin={self.is_admin})>"