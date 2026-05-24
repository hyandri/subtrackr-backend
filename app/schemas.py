from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List

#user Schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name : Optional[str] = None

class UserCreate(UserBase):
    password : str

class UserResponse(UserBase):
    id : int
    is_active : bool
    created_at : datetime

    class Config:
        from_attributes = True      #allows converting from sqlalchemy to model


#subscription Schemas
class SubscriptionBase(BaseModel):
    name : str
    price : float = Field(gt=0)
    billing_cycle : str = Field(pattern="^(monthly|yearly)$")
    next_billing_date : datetime
    category : Optional[str] = None
    is_active : bool =True

class SubscriptionCreate(SubscriptionBase):
    pass

class SubscriptionResponse(SubscriptionBase):
    id : int
    user_id : int
    created_at : datetime
    updated_at : datetime

    class Config:
        from_attributes = True

#token schema (for login)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None