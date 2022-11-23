from config import db,ma

class Opportunity(db.Model):
    __tablename__ = "opportunity"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)    
    status = db.Column(db.String(50), nullable=False) 
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))   
    

    def json(self):
        return { 'id':self.id,'name': self.name, 'status': self.status }

class OpportunitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Opportunity
        load_instance = True
        sqla_session = db.session

class Customer(db.Model):
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    createdTimestamp = db.Column(db.String(), nullable=False)    
    opportunities = db.relationship("Opportunity")
    

    def json(self):
        return { 'id':self.id,'name': self.name, 'contact': self.contact, 'status': self.status, 'createdTimestamp': self.createdTimestamp }

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True
        sqla_session = db.session

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
opportunity_schema = OpportunitySchema()
opportunities_schema =OpportunitySchema(many=True)





