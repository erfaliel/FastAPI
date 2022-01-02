from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# first create engine connection (sqllight, or postgres)
# session is used to map object (blog) to the database connection
# declarative_base will be the base object instance

# model : engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
# Prod (postgres) # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine( 
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} 
) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()