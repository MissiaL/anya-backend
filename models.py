from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship


class Base(DeclarativeBase):
    pass


class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)


class Specialist(Base):
    __tablename__ = "specialists"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    service_id = Column(Integer, ForeignKey("services.id"))


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_phone = Column(String)
    message = Column(Text)


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    picture = Column(Text)
    text = Column(Text)


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    type = Column(Integer)


class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    user_phone = Column(String)
    message = Column(Text)
    service_id = Column(Integer, ForeignKey("services.id"))
    specialist_id = Column(Integer, ForeignKey("specialists.id"))
