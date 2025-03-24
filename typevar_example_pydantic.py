from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class GenericResponse(BaseModel, Generic[T]):
    data: T
    status: str
    message: str


class User(BaseModel):
    id: int
    name: str


class Product(BaseModel):
    id: int
    price: float


class ErrorDetail(BaseModel):
    code: int
    detail: str


# Ответ с данными о пользователе
user_response = GenericResponse[User](
    data=User(id=1, name="Alice"), status="success", message="User data retrieved"
)

# Ответ с данными о продукте
product_response = GenericResponse[Product](
    data=Product(id=10, price=29.99), status="success",message="Product data retrieved"
)

# Ответ с ошибкой
error_response = GenericResponse[ErrorDetail](
    data=ErrorDetail(code=404, detail="Not found"),
    status="error",
    message="Resource not found",
)
