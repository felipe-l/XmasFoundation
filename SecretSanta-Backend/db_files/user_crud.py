from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secretsanta_db_setup import User  # Update with your actual setup

# Create an SQLite database engine
engine = create_engine('sqlite:///secretsanta.db')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE User
def create_user(username, email):
    new_user = User(username=username, email=email)
    session.add(new_user)
    session.commit()

# READ User by ID
def get_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user

# READ User by Username
def get_user_by_username(username):
    user = session.query(User).filter(User.username == username).first()
    return user

# UPDATE User
def update_user(user_id, new_username, new_email):
    user = get_user_by_id(user_id)
    if user:
        user.username = new_username
        user.email = new_email
        session.commit()

# DELETE User
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        session.delete(user)
        session.commit()

# Close the session
session.close()