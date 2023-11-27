import requests as req
import sqlite3 as sql
import pandas as pd
import numpy as np

dataset = pd.read_csv("Supply_Chain_Shipment_Pricing_Data.csv")

###### Checking for NaN Values ######

for column in dataset:
        
    isna_dataset = dataset[column][dataset[column].isna() == True]
    print(f"{column}: {len(isna_dataset)}")


###### Filling NaN Values ######

dataset["dosage"].fillna("N/A", inplace=True)
dataset["shipment mode"].fillna("N/A", inplace=True)
dataset["line item insurance (usd)"].fillna(dataset["line item insurance (usd)"].mean(), inplace=True)
dataset = dataset.rename(columns=lambda x: x.replace(' ', '_'))
dataset = dataset.rename(columns=lambda x: x.replace('/', '_'))
dataset = dataset.rename(columns=lambda x: x.replace('(', ''))
dataset = dataset.rename(columns=lambda x: x.replace(')', ''))

# ###### Separating data into categorized CSV Files######

dataset.to_csv('Updated_Supply_Chain_Shipment_Pricing_Data.csv', mode = 'w', index=False)
dataset[["id", "project_code"]].to_csv('Categorized Data CSVs/Identification.csv', mode = 'w', index=False)
dataset[["id", "country"]].to_csv('Categorized Data CSVs/Geographical Information.csv', mode = 'w', index=False)
dataset[["id", "managed_by", "fulfill_via"]].to_csv('Categorized Data CSVs/Management and Fulfillment.csv', mode = 'w', index=False)
dataset[["id", "vendor_inco_term", "shipment_mode", "po_sent_to_vendor_date", "scheduled_delivery_date", "delivered_to_client_date", "delivery_recorded_date"]].to_csv('Categorized Data CSVs/Transaction Details.csv', mode = 'w', index=False)
dataset[["id", "product_group", "sub_classification", "vendor", "molecule_test_type", "brand", "dosage", "dosage_form", "unit_of_measure_per_pack"]].to_csv('Categorized Data CSVs/Product Details.csv', mode = 'w', index=False)
dataset[["id", "line_item_quantity", "line_item_value", "pack_price", "unit_price", "weight_kilograms", "freight_cost_usd", "line_item_insurance_usd"]].to_csv('Categorized Data CSVs/Financial Information.csv', mode = 'w', index=False)
dataset[["id", "manufacturing_site", "first_line_designation"]].to_csv('Categorized Data CSVs/Manufacturing Information.csv', mode = 'w', index=False)


###### Checking for NaN Values ######

for column in dataset:
        
    isna_dataset = dataset[column][dataset[column].isna() == True]
    print(f"{column}: {len(isna_dataset)}")


# ###### Separating data into categorized SQL tables######

# conn = sql.connect('Supply_Chain_Shipment_Pricing_Data.sql')
# data = pd.read_csv('Updated_Supply_Chain_Shipment_Pricing_Data.csv')
# data.to_sql('data', conn, if_exists='append', index = False)

# cursor = conn.cursor()

# cursor.execute("CREATE TABLE Identification AS SELECT id, project_code FROM data;")
# cursor.execute("CREATE TABLE Geographical_Information AS SELECT id, country FROM data;")
# cursor.execute("CREATE TABLE Management_and_Fulfillment AS SELECT id, managed_by, fulfill_via FROM data;")
# cursor.execute("CREATE TABLE Transaction_Details AS SELECT id, vendor_inco_term, shipment_mode, po_sent_to_vendor_date, scheduled_delivery_date, delivered_to_client_date, delivery_recorded_date FROM data;")
# cursor.execute("CREATE TABLE Product_Details AS SELECT id, product_group, sub_classification, vendor, molecule_test_type, brand, dosage, dosage_form, unit_of_measure_per_pack FROM data;")
# cursor.execute("CREATE TABLE Financial_Information AS SELECT id, line_item_quantity, line_item_value, pack_price, unit_price, weight_kilograms, freight_cost_usd, line_item_insurance_usd FROM data;")
# cursor.execute("CREATE TABLE Manufacturing_Information AS SELECT id, manufacturing_site, first_line_designation FROM data;")