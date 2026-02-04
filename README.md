Excel-to-SQL Data Pipeline


📌 Project Overview

This repository contains a Python-based ETL (Extract, Transform, Load) script designed to automate the transfer of KPI data from a complex Excel workbook into an Azure SQL Server database.

The script is specifically optimized to handle the Company KPIs V4 file, processing the Raw Data Redshift worksheet which contains high-density data spanning from Column A to JI (~243 columns).


🚀 Getting Started
1. Prerequisites

    Python 3.8+

    ODBC Driver 17 for SQL Server (Ensure this is installed on your OS)

    Access to the company OneDrive/Shared Network path for the source file.

2. Installation

Clone the repository and install the required Python libraries:
Bash

git clone https://github.com/YOUR_USERNAME/excel-to-sql-pipeline.git
cd excel-to-sql-pipeline
pip install -r requirements.txt

3. Configuration

The script uses a .env file to manage sensitive credentials.

    Copy the template: cp .env.example .env

    Open .env and fill in your actual details:
    Plaintext

    DB_USER=your_username
    DB_PASS=your_password
    DB_HOST=your_server.database.windows.net
    DB_NAME=Finance
    EXCEL_FILE_PATH=C:/Users/.../Company KPIs V4.xlsx

🛠️ Technical Details

    Data Source: Excel (.xlsx) - Sheet: Raw Data Redshift.

    Data Volume: Handles wide-format data (Columns A through JI).

    Database Engine: SQLAlchemy with pyodbc.

    Upload Strategy: if_exists='replace'. The script refreshes the target table entirely on each run to ensure data consistency with the master Excel file.

🔒 Security Note

This project utilizes .gitignore to ensure that:

    No credentials are pushed to version control.

    No actual business data (Excel files) are stored in the repository.

    Environment variables are used for all connection strings.

🤝 Contributing

    Fork the Project

    Create your Feature Branch (git checkout -b feature/AmazingFeature)

    Commit your Changes (git commit -m 'Add some AmazingFeature')

    Push to the Branch (git push origin feature/AmazingFeature)

    Open a Pull Request

