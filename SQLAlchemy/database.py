from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# After creating the DB using pgAdmin
engine=create_engine("postgresql://postgres:usman367@localhost/item_db",
                     echo=True
                     )

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)

