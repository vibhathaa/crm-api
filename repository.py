import re
from config import db
from sqlalchemy import update,text,bindparam
from models import Customer,Opportunity, customer_schema, opportunity_schema


class CustomerRepository:

    def get_all():
        customers = db.session.query(Customer).all()
        return customers

    def get_by_id(id):
        customer = db.session.get(Customer,id)
        return customer
    
    def get_by_filter(filter):       
       
        s = ""
        params = []
        #escape special charcters
        last_key = list(filter.keys()).pop()
        print(filter)
        #construct the WHERE clause and wrap search parameters
        for key in filter:
            value = re.sub('[*_\[\\]^]','',filter[key])
            print("value", value)
            params.append(bindparam(key, value=f"%{value}%"))
            if key != last_key:
                s += f"{key} LIKE :{key} AND "                
            else:
                s += f"{key} LIKE :{key};"
        

        query = text(s)
        p_tuple = tuple(params)
        query = query.bindparams(*p_tuple)       

        customers = db.session().query(Customer).filter(query).all()      
        
        return customers

    def update_status_by_id(id,new_status):
        customer = db.session.get(Customer,id)

        if customer:
            db.session.execute(
                update(Customer)
                .where(Customer.id == id )
                .values(status = new_status )
            )
            db.session.commit()            
        
        return customer


class OpportunityRepository:

    def get_opportunity_by_id(id):
        opportunity = db.session.get(Opportunity,id)
        
        return opportunity
    
    def get_opportunity_by_customer_id(customerId):
        opportunities = db.session.query(Opportunity).filter(Opportunity.customer_id == customerId).all()

        return opportunities
    
    def create_opportunity(customerId,opportunity):        
        opp = opportunity_schema.load(opportunity)
        opp.customer_id = customerId       

        opportunity = db.session.add(opp)
        db.session().commit()
      
        return opp
    
    def update_opportunity_by_id(id, opportunity):
        original_opportunity = db.session.get(Opportunity,id)
        
        if original_opportunity:
            db.session.execute(
                update(Opportunity)
                .where(Opportunity.id == id )
                .values( name = opportunity['name'], status = opportunity['status'] )
            )
            db.session.commit()          
        
        return original_opportunity


    

