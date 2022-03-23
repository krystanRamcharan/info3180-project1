from . import db
from werkzeug.security import generate_password_hash



class Properties(db.Model):
    __tablename__='properties'

    id= db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.String(80))
    description=db.Column(db.String(255))
    No_of_rooms=db.Column(db.Integer)
    No_of_bathrooms=db.Column(db.Integer)
    price=db.Column(db.Float)
    property_type=db.Column(db.String(50))
    location=db.Column(db.String(50))
    photo_filename=db.Column(db.String(50))
    
    
    def __init__(self,title,description,No_of_rooms,No_of_bathrooms,price,property_type,location,photo_filename):
        self.title=title
        self.description= description
        self.No_of_rooms= No_of_rooms
        self.No_of_bathrooms=No_of_bathrooms
        self.price=price
        self.property_type= property_type
        self.location= location
        self.photo_filename=photo_filename


    def is_authenticated(self):
        return True


    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    

        
