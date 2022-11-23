from flask import jsonify,abort
from models import opportunity_schema, opportunities_schema
from repository import OpportunityRepository

def get_opportunities(customerId): 

    opp = OpportunityRepository.get_opportunity_by_customer_id(customerId)
    data = opportunities_schema.dump(opp)    
   
    return jsonify( { "results" : data }),200

def add_opportunities(customerId, opportunity):

    opp = OpportunityRepository.create_opportunity(customerId,opportunity)
    data = opportunity_schema.dump(opp)

    if data:
        return jsonify( { "results" : [ data ] }),200
    else:
        abort(500, f"Error while adding the opportunity")

def edit_opportunity(opportunityId, opportunity):

    opp = OpportunityRepository.update_opportunity_by_id(opportunityId, opportunity)
    data = opportunity_schema.dump(opp)

    if data:
        return jsonify( { "results" : [ data ] }),200
    else:
       abort(500, f"Error while adding the opportunity") 

def cors():

    return jsonify(),200

def cors_v2():
    
    return jsonify(),200