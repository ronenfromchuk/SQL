from sqlalchemy import Table, Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref

class Lessons(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    student = relationship("Student", backref=backref("lessons", uselist=True))
    teacher = relationship("Teacher", backref=backref("lessons", uselist=True))
    subject = relationship("Subject", backref=backref("lessons", uselist=True))

    def __str__(self):
        return f'<Lessons> id:{self.id} student_id:{self.student_id} teacher_id:{self.teacher_id} subject_id:{self.subject_id}\n'

    def __repr__(self):
        return f'<Lessons> id:{self.id} student_id:{self.student_id} teacher_id:{self.teacher_id} subject_id:{self.subject_id}\n'

class Student(Base):
    __tablename__ = 'students'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=True)

    def __str__(self):
        return f'<orders> id:{self.id} name:{self.name}'

    def __repr__(self):
        return f'<orders> id:{self.id} name:{self.name}'

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=True)

    def __str__(self):
        return f'<Teacher> id:{self.id} name:{self.name}'

    def __repr__(self):
        return f'<Teacher> id:{self.id} name:{self.name}'

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50), nullable=True)

    def __str__(self):
        return f'<Subject> id:{self.id} name:{self.name}'

    def __repr__(self):
        return f'<Subject> id:{self.id} name:{self.name}'
