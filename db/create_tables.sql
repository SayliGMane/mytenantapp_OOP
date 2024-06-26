

-- Create table for flat_details
-- Create table
CREATE TABLE private_data.flat_details (
    flatno INTEGER NOT NULL PRIMARY KEY,
    floorno INTEGER NOT NULL,
    furnished VARCHAR(5) NOT NULL,
    facilities TEXT[],
    propertytype VARCHAR(5),
    area_in_m2 INTEGER,
    price_range INT4RANGE,
    available_from DATE,
    CHECK (propertytype::text = ANY (ARRAY['2BHK', '1BHK', 'SHOP']::text[]))
);



-- Create table for flat_owner_details
CREATE TABLE private_data.flat_owner_details (
    flat_owner_id SERIAL PRIMARY KEY,
    flatno INTEGER,
    bank_details CHARACTER VARYING(200),
    owner JSON,
    FOREIGN KEY (flatno) REFERENCES private_data.flat_details(flatno)
);


CREATE TABLE private_data.rent_details (
    FlatNo INT REFERENCES private_data.flat_details(flatno),
    TenantID CHAR(5) PRIMARY KEY,
    ContractStartDate DATE CHECK (ContractStartDate < ContractEndDate),
    ContractEndDate DATE,
    Rent INT CHECK(Rent > 10000)
);





CREATE TABLE private_data.tenant_details(
    TenantID CHAR(5) REFERENCES private_data.rent_details(TenantID),
    TenantName TEXT UNIQUE,
    Gender CHAR(1) ,
    PermanentAddress VARCHAR(70),
    Occupation TEXT,
    UID_Number VARCHAR(10),
    ContactNumber VARCHAR(12)
    CHECK(GENDER IN ('M','F')) 
);