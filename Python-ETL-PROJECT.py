import glob
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime

log_file = "log_file.txt"
target_file = "transformed_data.csv"

-- extract csv file
def extract_from_csv(input_file):
    dataframe = pd.read_csv(input_file)
    return dataframe

-- extract json file
def extract_from_json(input_file):
    datagrame = pd.read_json(input_file,lines=True)
    return dataframe

--extract xml file
def extract_from_xml(input_file):
    dataframe = pd.DataFrame(columns = ["name","height","weight"])
    tree = ET.parse(input_file)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = pd.concat([dataframe,pd.DataFrame([{"name":name, "height":height, "weight":weight}])], ignore_index=True)
    return dataframe

def extract(): 
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data 
     
    # process all csv files 
    for csvfile in glob.glob("*.csv"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 
         
    # process all json files 
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True) 
     
    # process all xml files 
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
         
    return extracted_data 