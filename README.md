# Employee Work Reports Dashboard

This is a web application built using Dash and Plotly to visualize employee performance and work reports. It includes filters for viewing data based on year, location, department, and position, and provides various charts to gain insights into employee work reports.

## Features

- Visualize employee work data with interactive charts, including bar charts, pie charts, heatmaps, and more.
- Filter data by year, location, department, and position to gain focused insights.
- User-friendly UI with Bootstrap styling.

## Prerequisites

- **Python 3.8+**
- **MySQL Database** with tables for employees and yearly work reports.

## Database Setup

The project requires a MySQL database named `esunscope`. You have two options for setting up the database: **importing the provided SQL file** or **creating the database manually**.

### Option 1: Importing the Provided Database

1. **Ensure MySQL is installed and running** on your machine.
2. **Import the provided SQL file** to set up the database structure and data:
   - Locate the file `esunscope.sql`.
   - Open a terminal (or command prompt) and run the following command to import the database:
     ```bash
     mysql -u root -p < esunscope.sql
     ```
   - Replace `root` with your MySQL username. You will be prompted to enter your MySQL password.

This will create a database named `esunscope` with the required tables and sample data.

### Option 2: Creating the Database Manually

If you prefer to set up the database from scratch, follow these steps:

1. **Create a new database**:
   ```sql
   CREATE DATABASE esunscope;
   USE esunscope;
   ```

2. **Create the `Employees` table**:
   ```sql
   CREATE TABLE Employees (
       EmployeeID INT PRIMARY KEY,
       Name VARCHAR(255),
       Location VARCHAR(255),
       Department VARCHAR(255),
       Position VARCHAR(255),
       FeedbackScore FLOAT
   );
   ```

3. **Create tables for each year's work reports**. For example, for Year 1:
   ```sql
   CREATE TABLE WorkReports_Year1 (
       EmployeeID INT,
       ProjectsCompleted INT,
       HoursWorked INT,
       PerformanceScore FLOAT,
       FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
   );
   ```

   Repeat this step for each additional year (e.g., `WorkReports_Year2`, `WorkReports_Year3`, etc.).

4. **Insert sample data** into the tables or populate it with your actual data.

### Database Schema

The project expects the following structure within the `esunscope` database:

1. **Employees** table: Holds employee information with columns like `EmployeeID`, `Name`, `Location`, `Department`, `Position`, and `FeedbackScore`.
2. **WorkReports_YearX** tables (for Year 1, Year 2, etc.): Each table should contain data like `EmployeeID`, `ProjectsCompleted`, `HoursWorked`, and `PerformanceScore`.

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine and navigate into the project directory.

### Step 2: Create and Activate a Virtual Environment

Create a virtual environment named `esun_env` and activate it.

For Windows:
- Run `esun_env\Scripts\activate`

For macOS/Linux:
- Run `source esun_env/bin/activate`

### Step 3: Install Dependencies

Install the required Python packages in the virtual environment by running:
```
pip install -r requirements.txt
```

### Step 4: Configure the Database Connection

Update the MySQL connection string in the code:
```python
engine = create_engine('mysql+pymysql://root:@localhost/esunscope')
```
Replace `root` with your MySQL username and add a password if necessary.

### Step 5: Run the Application

Run the application using:
```
python app.py
```
The application will start running on `http://127.0.0.1:8050`. Open this URL in your browser to view the dashboard.

## Usage

1. Use the dropdown filters at the top to select specific years, locations, departments, and positions to filter the data.
2. Explore the charts to gain insights into employee performance.

## Project Structure

```
project-directory/
│
├── esun_env/                  # Virtual environment directory
└── future_upgrades            # Prediction related files for future upgrades 
├── main.py                    # Main application file
├── requirements.txt           # Dependencies file
├── esunscope.sql              # Database setup file
└── README.md                  # Project README
```

### Known Issues

- Ensure that the database connection is correct.
- The application expects specific database columns. Verify that all required columns (`EmployeeID`, `ProjectsCompleted`, `HoursWorked`, `PerformanceScore`, etc.) are present in the database.

## Troubleshooting

1. **Database Connection Error**: Ensure the MySQL server is running and the connection string is correct.
2. **Missing Columns**: If the app fails due to missing columns, verify that all required columns are present in the database.

## License

This project is open-source and free to use under the MIT License.
