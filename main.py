import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Credentials - pulled from environment variables
DB_USER = os.getenv('DB_USER')
DB_PASS = quote_plus(os.getenv('DB_PASS'))
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_DRIVER = quote_plus('ODBC Driver 17 for SQL Server')

# Excel Config
FILE_PATH = os.getenv('EXCEL_FILE_PATH')
SHEET_NAME = 'Raw Data Redshift'

# Construct connection string
connection_string = f"mssql+pyodbc://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}?driver={DB_DRIVER}"

def load_excel_data(path, sheet):
    try:
        data = pd.read_excel(path, sheet_name=sheet)
        print("✅ Data loaded successfully from Excel.")
        return data
    except Exception as e:
        print(f"❌ Error loading Excel: {e}")
        return None

if __name__ == "__main__":
    df = load_excel_data(FILE_PATH, SHEET_NAME)
    
    if df is not None:
        try:
            engine = create_engine(connection_string)
            df.to_sql('Raw Data Redshift', con=engine, if_exists='replace', index=False)
            print("🚀 Data written successfully to SQL Server.")
        except Exception as e:
            print(f"❌ SQL Error: {e}")
