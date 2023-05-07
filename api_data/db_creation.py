from sqlalchemy import String, DateTime, Integer, Boolean
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class PersonalData(Base):
    __tablename__ = "personal_data"
    id: Mapped[int] = mapped_column(primary_key=True)
    pdata_name: Mapped[str] = mapped_column(String(30))
    pdata_description: Mapped[Optional[str]] = mapped_column(String(50))
    pdata_value: Mapped[Optional[str]] = mapped_column(String(200))

    def __repr__(self) -> str:
        return f"PersonalData(id={self.id!r}, data_name={self.data_name!r}, data_value={self.data_value!r})"


class HardSkills(Base):
    __tablename__ = 'hard_skills'
    id: Mapped[int] = mapped_column(primary_key=True)
    hskill_name = mapped_column(String(30))
    hskill_descripion = mapped_column(String(200))
    hskill_time = mapped_column(Integer, nullable=False)
    hskill_type1 = mapped_column(String(50))
    hskill_type2 = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"HardSkills(id={self.id!r}, hskill_name={self.data_name!r}, hskill_time={self.data_value!r})"


class Experiences(Base):
    __tablename__ = 'experiences'
    id: Mapped[int] = mapped_column(primary_key=True)
    exp_ini_date = mapped_column(DateTime, nullable=False)
    exp_end_date = mapped_column(DateTime, nullable=True)
    exp_company_name = mapped_column(String(30))
    exp_company_role = mapped_column(String(30))
    exp_description = mapped_column(String(200))
    exp_display = mapped_column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"Experiences(id={self.id!r}, exp_company_name={self.data_name!r}, exp_company_role={self.data_value!r})"

class Formation(Base):
    __tablename__ = 'formation'
    id: Mapped[int] = mapped_column(primary_key=True)
    course_name = mapped_column(String(200))
    course_descripion = mapped_column(String(200))
    course_school = mapped_column(String(30))
    course_type = mapped_column(String(30))
    course_period = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"Experiences(id={self.id!r}, exp_company_name={self.data_name!r}, exp_company_role={self.data_value!r})"
