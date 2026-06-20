# USE CASES IN REAL TIME PROJECTS....:}

# Representing a single Row from a Database or API
row = {
    "id": 101,
    "name": "John",
    "country": "DE",
    "age": 29, 
    "status": "active"
}

#2 Use case: Mapping To Friendly Values
status_map = {
    "01": "Open",
    "02": "In Progress",
    "03": "Done"
}

#3 Mapping Abbreviations

country_map = {
    "DE": "Germany",
    "FR": "France",
    "IN": "India" 
     }

# Storing Enviornment Variables & Configuration
system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytics_warehouse"
}

print(system_conn)