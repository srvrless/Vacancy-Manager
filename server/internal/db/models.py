import uuid
from internal.utils.base import Base
from sqlalchemy import JSON, UUID, Boolean, Column, ForeignKey, Integer, String, Table

role = Table(
    "role",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(50), nullable=False, unique=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    city = Column(String(50), nullable=False)
    role_id = Column(Integer, ForeignKey(role.c.id))


class Application(Base):
    __tablename__ = 'applications'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(50), nullable=False)  # имя
    second_name = Column(String(50), nullable=False)  # фамилия
    surname = Column(String(50), nullable=False)  # отчество
    cv_file = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)