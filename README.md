# my_tenant_db # 

### Mission Statement:
     To effectively manage and maintain the records of all properties, owners, tenants, and rental transactions. (In simple words data will help us not managing the all properties bt also to track all records of rented properties)

### Mission Objective:
- Know yearly income of each owner.
- know when he can post the advertisement or send notification to tenant to renewal of new contract
- To know the max and min rent.
- To get all details like : properties, who owns which property, and tenant info.

### Instructions To Run The Program: 
1. prerequisites :  
    - Open Terminal
    - Set the working directory in you computer: using below command in terminal
    ```python
        cd desktop/my_tenant_db/src
    ```

    - Run the below command in terminal to switch to postgres, and to create the database and add data into tables to use the program. 

    ```sql
    cd src/flat_file/sql files
    psql -U postgres
    \i flat_details.sql
    \i flat_owner_details.sql
    \i rent_details.sql
    \i tenant_details.sql
    \q
    ```  
    - Creating the virtual Environment and to install psycopg2 follow the instructions 
    ```python
        cd .. 
        cd .. 
        python3 -m venv .venv --prompt my_tenant
        source .venv/bin/activate
        pip install psycopg2-binary
    ```     

2. To Run the main program : 
    ```python 
        cd ..
        python3 -m src.main
    ```