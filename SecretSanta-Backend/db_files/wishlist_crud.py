from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from secretsanta_db_setup import WishList  # Update with your actual setup

# Create an SQLite database engine
engine = create_engine('sqlite:///secretsanta.db')
Session = sessionmaker(bind=engine)
session = Session()

# CREATE Wish List Item
def create_wishlist_item(item_name, product_link, user_id):
    new_item = WishList(item_name=item_name, product_link=product_link, user_id=user_id)
    session.add(new_item)
    session.commit()

# READ Wish List Item by ID
def get_wishlist_item_by_id(item_id):
    item = session.query(WishList).filter(WishList.id == item_id).first()
    return item

# UPDATE Wish List Item
def update_wishlist_item(item_id, new_item_name, new_product_link):
    item = get_wishlist_item_by_id(item_id)
    if item:
        item.item_name = new_item_name
        item.product_link = new_product_link
        session.commit()

# DELETE Wish List Item
def delete_wishlist_item(item_id):
    item = get_wishlist_item_by_id(item_id)
    if item:
        session.delete(item)
        session.commit()

# Close the session
session.close()