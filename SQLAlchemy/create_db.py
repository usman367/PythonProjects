from database import Base,engine
from models import Item

print("Create database ....")

# This is to create the database
# In the terminal:
# python create_db.py
Base.metadata.create_all(engine)
