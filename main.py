from typing import AsyncGenerator

from fastapi import FastAPI
from fastcrud import FastCRUD, crud_router
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Item, Service, Specialist, Feedback, Event, Request, Article
from schemas import (
    ItemCreateSchema,
    ItemUpdateSchema,
    SpecialistCreateSchema,
    ServiceCreateSchema,
    SpecialistUpdateSchema,
    ServiceUpdateSchema,
    FeedbackCreateSchema,
    FeedbackUpdateSchema,
    ArticleCreateSchema,
    ArticleUpdateSchema,
    EventCreateSchema,
    EventUpdateSchema,
    RequestCreateSchema,
    RequestUpdateSchema,
)

# Database setup (Async SQLAlchemy)
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Database session dependency
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# Create tables before the app start
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


# FastAPI app
app = FastAPI(lifespan=lifespan)

service_router = crud_router(
    session=get_session,
    model=Service,
    create_schema=ServiceCreateSchema,
    update_schema=ServiceUpdateSchema,
    path="/services",
    tags=["Services"],
    deleted_methods=["db_delete", "read_paginated"],
)

specialist_router = crud_router(
    session=get_session,
    model=Specialist,
    create_schema=SpecialistCreateSchema,
    update_schema=SpecialistUpdateSchema,
    path="/specialist",
    tags=["Specialist"],
    deleted_methods=["db_delete", "read_paginated"],
)

feedback_router = crud_router(
    session=get_session,
    model=Feedback,
    create_schema=FeedbackCreateSchema,
    update_schema=FeedbackUpdateSchema,
    path="/feedback",
    tags=["Feedback"],
    deleted_methods=["db_delete", "read_paginated"],
)

article_router = crud_router(
    session=get_session,
    model=Article,
    create_schema=ArticleCreateSchema,
    update_schema=ArticleUpdateSchema,
    path="/article",
    tags=["Article"],
    deleted_methods=["db_delete", "read_paginated"],
)

event_router = crud_router(
    session=get_session,
    model=Event,
    create_schema=EventCreateSchema,
    update_schema=EventUpdateSchema,
    path="/event",
    tags=["Event"],
    deleted_methods=["db_delete", "read_paginated"],
)

request_router = crud_router(
    session=get_session,
    model=Request,
    create_schema=RequestCreateSchema,
    update_schema=RequestUpdateSchema,
    path="/request",
    tags=["Request"],
    deleted_methods=["db_delete", "read_paginated"],
)


app.include_router(service_router)
app.include_router(specialist_router)
app.include_router(feedback_router)
app.include_router(article_router)
app.include_router(event_router)
app.include_router(request_router)
