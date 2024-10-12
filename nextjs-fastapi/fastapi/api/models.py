from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

workout_routine_association = Table(
    'workout_routine', Base.metadata,
    Column('workout_id', Integer, ForeignKey('workouts.id')),
    Column('routine_id', Integer, ForeignKey('routines.id'))
)

doc_compare_user_association = Table(
    'doc_compare_user', Base.metadata,
    Column('user_id', String, ForeignKey('users.id')),
    Column('document_compare_id', String, ForeignKey('document_compare.id'))
)

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(String, unique=True, index=True)
    email = Column(String)
    
class DocumentCompare(Base):
    __tablename__='document_compare'
    id = Column(String, primary_key=True, index=True)
    