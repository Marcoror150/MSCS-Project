"""
Author: Marc Christensen
C.A.R.S. DB Call script

This script is used to make calls to the C.A.R.S. database as part of the API.
"""

import psycopg2

""" Builds and executes the statements for insert, select, and delete.
    Each item in values must be a string type. """

def insert_call(values):
  # Create connection to the DB and cursor.
  conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres")
  cur = conn.cursor()

  # Requires values contain 5 strings.
  if len(values) == 5:
    statement = "INSERT INTO accident_vehicle_master VALUES ("

    # Query the DB to see the last p_key used.
    cur.execute(""" SELECT MAX(p_key) FROM accident_vehicle_master """)

    # Get next p_key and store it.
    p_key = cur.fetchone()[0] + 1

    statement += str(p_key) + ", " + values[0] + ", " + values[1] + ", " + values[2] + ", " + values[3] + ", " + values[4] + ")"

    # Execute the statement
    cur.execute(statement)
    conn.commit()

    # Print result from insert command
    print(cur.statusmessage)

  else:
    print("Not enough arguments supplied to insert an entry. A list of strings with five values are required.")

def select_call(values):
  # Create connection to the DB and cursor.
  conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres")
  cur = conn.cursor()

  # Requires values contain 2 strings. The first is the attribute, the second is the value, otherwise, print all records.
  if len(values) == 2:
    statement = "SELECT * FROM accident_vehicle_master WHERE " + str(values[0]) + " = " + str(values[1])
    cur.execute(statement)

    # Print all the results from the cursor.
    for record in cur:
      print(record)

  elif len(values) < 2:
    statement = "SELECT * FROM accident_vehicle_master"
    cur.execute(statement)

    # Print all the results from the cursor.
    for record in cur:
      print(record)

def delete_call(values):
  # Create connection to the DB and cursor.
  conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres")
  cur = conn.cursor()

  # Requires values contain 2 strings. The first is the attribute, the second is the value.
  if len(values) == 2:
    statement = "DELETE FROM accident_vehicle_master WHERE " + str(values[0]) + " = " + str(values[1])
    cur.execute(statement)

    # Print result from delete command
    print(cur.statusmessage)

    conn.commit()
  
  else:
    print("Not enough arguments supplied to delete an entry. A list of strings with two values are required.")
