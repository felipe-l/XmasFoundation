from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secretsanta_db_setup import user_secret_santa_association  # Update with your actual setup

# Create an SQLite database engine
engine = create_engine('sqlite:///secretsanta.db')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE User-Secret Santa Association
def create_user_secret_santa_association(user_id, secret_santa_instance_id):
    new_association = user_secret_santa_association.insert().values(
        user_id=user_id,
        secret_santa_instance_id=secret_santa_instance_id
    )
    session.execute(new_association)
    session.commit()

# READ User-Secret Santa Association by User ID
def get_association_by_user_id(user_id):
    result = session.execute(
        user_secret_santa_association.select().where(user_secret_santa_association.c.user_id == user_id)
    )
    return result.fetchall()

# READ User-Secret Santa Association by Secret Santa Instance ID
def get_association_by_instance_id(instance_id):
    result = session.execute(
        user_secret_santa_association.select().where(
            user_secret_santa_association.c.secret_santa_instance_id == instance_id
        )
    )
    return result.fetchall()

# DELETE User-Secret Santa Association by User ID and Instance ID
def delete_user_secret_santa_association(user_id, secret_santa_instance_id):
    session.execute(
        user_secret_santa_association.delete().where(
            user_secret_santa_association.c.user_id == user_id
            and user_secret_santa_association.c.secret_santa_instance_id == secret_santa_instance_id
        )
    )
    session.commit()

# Close the session
session.close()