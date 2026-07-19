from .database import Base
from sqlalchemy import Integer, Column, String, DECIMAL, Date, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func

class Client(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    company_name = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now()) # created_at -> this means when this company signed up, means when this company started using SlipSync, and server_default=func.now() tells the database itself to automatically fill this in with the current timestamp when a row is created, so I never have to manually set it in your code
    is_active = Column(Boolean, default=True) # There is no difference between default and server_default, default is handled by SQLAlchemy while server_default is handled by database

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, nullable=False) # Since id is made the primary key so it is already indexed, so writing index=True will have no meaning
    client_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    employee_code = Column(String, index=True, nullable=False)
    __table_args__ = (UniqueConstraint('client_id', 'employee_code', name='uq_client_employee_code'),)
    name = Column(String, index=True, nullable=False)
    base_salary = Column(DECIMAL, nullable=False)
    designation = Column(String, index=True, nullable=False)
    join_date = Column(Date, nullable=False) # nullable=False in every field because it is by default True, so this can lead to a problem of database accepting an employee row with no name or base salary etc, so nullable=False, or it simply means this field cannot be empty
