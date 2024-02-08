
import sqlite3


# Connect to the database
connection = sqlite3.connect("crowdworks_jobs.db")
cursor = connection.cursor()

# Create a table to store job data
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs 
                  (id INTEGER PRIMARY KEY, 
                   title TEXT, 
                   link TEXT, 
                   category TEXT, 
                   employer_name TEXT, 
                   payment TEXT, 
                   post_date TEXT, 
                   bid TEXT)''')


# Define a function to check if a row with the given title and employer already exists
def row_exists(title, employer_name, post_date):
    cursor.execute('''SELECT COUNT(*) 
                      FROM jobs 
                      WHERE title=? AND employer_name=? AND post_date=?''', (title, employer_name, post_date))
    return cursor.fetchone()[0] > 0