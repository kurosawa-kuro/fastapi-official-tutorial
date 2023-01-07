from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app/sql_app.sqlite3"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3306/training"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
