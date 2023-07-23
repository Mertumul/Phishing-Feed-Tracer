from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


#
class Phishing(Base):
    __tablename__ = "phishing"

    __table_args__ = (UniqueConstraint("url", name="unique_phishing"),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(1000), nullable=False)
