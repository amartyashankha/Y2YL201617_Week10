from model import *

def verify_password(session, email, password):
    customer = session.query(Customer).filter_by(email=email).first()
    if not customer or not customer.verify_password(password):
        return False
    return True
