from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='items'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False,unique=True)
    description=Column(Text)
    price=Column(Integer,nullable=False)
    on_offer=Column(Boolean,default=False)

    # Creating a string representation of our object
    # We created the object by (in the python terminal):
    # python
    # from models import Item
    # new_user=Item(name="Milk,description="Nice Milk",price=2000,on_offer=True)
    # And we can view it by :
    # new_user
    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"


