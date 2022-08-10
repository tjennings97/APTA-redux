from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='TRUE')
    role = Column(Integer, nullable=False)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    code = Column(String, nullable=False, unique=True)
    section = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    title = Column(String, nullable=False)
    professor = Column(String, nullable=False)
    professor_email = Column(String, nullable=False)
    role = Column(Integer, nullable=False)
    days = Column(String, nullable=False)
    location = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)

class UserCourse(Base):
    __tablename__ = "users_courses"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False)
    
    course = relationship("Course")
    user = relationship("User")

class Assignment(Base):
    __tablename__ = "assignments"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    due_date = Column(TIMESTAMP(timezone=True), nullable=True)
    grade = Column(String, nullable=False)
    grade_type = Column(String, nullable=False)
    
    user_course_id = Column(Integer, ForeignKey("users_courses.id", ondelete="CASCADE"), nullable=False)

    user_course = relationship("UserCourse")

class Requests(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    request_type = Column(String, nullable=False)
    request_item_id = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    is_resolved = Column(Boolean, nullable=False, server_default='FALSE')
    resolution = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user = relationship("User")
