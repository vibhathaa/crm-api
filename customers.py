from flask import jsonify,abort
from models import customer_schema,customers_schema
from repository import CustomerRepository
  

def get_all_customers():    

    customers = CustomerRepository.get_all()
    data = customers_schema.dump(customers)

    return jsonify({ 'results' : data }),200

def get_customer_by_id(customerId):    
    
    customer = CustomerRepository.get_by_id(customerId)
    data = customer_schema.dump(customer)

    if data:
        return jsonify({ 'results' : [ data ] }), 200  
        
def get_customer_by_filter(**kwargs):  
    
    filter = dict()
    fieldList = ['name', 'id', 'contact', 'createdTimestamp']

    for key in kwargs:
        if kwargs[key] != '' or fieldList.get(key) != None:
            filter[key] = kwargs[key]
    
    if len(filter) == 0:
        abort(200, f"Filter not supported")    

    customers = CustomerRepository.get_by_filter(filter)
    data = customers_schema.dump(customers)
    
    if data:            
        return jsonify( { "results" : data }),200
    else :
        return jsonify( { "results" : [] }),200
    

def change_customer_status(customerId, status):    

    customer = CustomerRepository.update_status_by_id(customerId,status)
    data = customer_schema.dump(customer)

    if data:
        return jsonify( { "results" : data })
    else:
        abort(404, f"No such customer")

def cors():
     return jsonify({}),200