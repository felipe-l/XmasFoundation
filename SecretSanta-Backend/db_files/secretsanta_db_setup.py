from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create an SQLite database
engine = create_engine('sqlite:///secretsanta.db', echo=True)  # Set 'echo' to True to see SQL statements

Base = declarative_base()

# Define the User Table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    wishlists = relationship('WishList', back_populates='user')
    secret_santa_instances = relationship('SecretSantaInstance', secondary='user_secret_santa_association')

# Define the SecretSantaInstance Table
class SecretSantaInstance(Base):
    __tablename__ = 'secret_santa_instances'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    users = relationship('User', secondary='user_secret_santa_association')

# Define the User_SecretSanta_Association Table
user_secret_santa_association = Table(
    'user_secret_santa_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('secret_santa_instance_id', Integer, ForeignKey('secret_santa_instances.id'))
)

# Define the WishList Table
class WishList(Base):
    __tablename__ = 'wishlists'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    product_link = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='wishlists')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Close the session when done
session.close()