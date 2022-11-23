# CRM-API - Backend REST API for CRM-UI
## CRM API
Technologies/Frameworks
- Python3.8 + Python Flask
- Connexion
- SQLAlchemy + Marshmellow

## Getting Started

- pull the git repo to the desired directory
- Install python-pip and fetch dependecies using pip install -r requirements.txt
- Make Changes to config.py as necessary for DB connection. SQLite is used by default and a some test data is provided.
- Run the application using python3 app.py. 

## Modifications - contributions
The project structure is as follows
- openapi/swagger.yml - contains the API specification. Any new endpoints must be defined here and mapped to respective controllers. 
- customers.py/opportunities.py - respective controllers for the resources
- models.py - contains the model definitions and serializations
- repository.py - Repository for resources 
- config.py - Config file 

## TODO ##
