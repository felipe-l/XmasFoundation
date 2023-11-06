from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secretsanta_db_setup import SecretSantaInstance  # Update with your actual setup

# Create an SQLite database engine
engine = create_engine('sqlite:///secretsanta.db')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE Secret Santa Instance
def create_secret_santa_instance(name):
    new_instance = SecretSantaInstance(name=name)
    session.add(new_instance)
    session.commit()

# READ Secret Santa Instance by ID
def get_secret_santa_instance_by_id(instance_id):
    instance = session.query(SecretSantaInstance).filter(SecretSantaInstance.id == instance_id).first()
    return instance

# UPDATE Secret Santa Instance
def update_secret_santa_instance(instance_id, new_name):
    instance = get_secret_santa_instance_by_id(instance_id)
    if instance:
        instance.name = new_name
        session.commit()

# DELETE Secret Santa Instance
def delete_secret_santa_instance(instance_id):
    instance = get_secret_santa_instance_by_id(instance_id)
    if instance:
        session.delete(instance)
        session.commit()

# Close the session
session.close()