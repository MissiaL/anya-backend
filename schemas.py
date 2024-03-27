from pydantic import BaseModel


class ServiceCreateSchema(BaseModel):
    name: str = None
    description: str = None


class ServiceUpdateSchema(BaseModel):
    name: str = None
    description: str = None


class SpecialistCreateSchema(BaseModel):
    name: str = None
    service_id: int = None


class SpecialistUpdateSchema(BaseModel):
    name: str = None
    service_id: int = None


class FeedbackCreateSchema(BaseModel):
    user_name: str = None
    user_phone: str = None
    message: str = None


class FeedbackUpdateSchema(BaseModel):
    user_name: str = None
    user_phone: str = None
    message: str = None


class ArticleCreateSchema(BaseModel):
    name: str = None
    date: str = None
    picture: str = None
    text: str = None


class ArticleUpdateSchema(BaseModel):
    name: str = None
    date: str = None
    picture: str = None
    text: str = None


class EventCreateSchema(BaseModel):
    name: str = None
    date: str = None
    type: int = None


class EventUpdateSchema(BaseModel):
    name: str = None
    date: str = None
    type: int = None


class RequestCreateSchema(BaseModel):
    user_name: str = None
    user_phone: str = None
    message: str = None
    service_id: int = None
    specialist_id: int = None


class RequestUpdateSchema(BaseModel):
    user_name: str = None
    user_phone: str = None
    message: str = None
    service_id: int = None
    specialist_id: int = None
