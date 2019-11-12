import psycopg2, csv, ast

# Determines the data type of each column in the header 
# and selects the appropriate type for pgAdmin.
def dataType(val, current_type):
    try:
        # Evaluates numbers to an appropriate type, and strings as an error.
        t = ast.literal_eval(val)
    except ValueError:
      return 'varchar'
    except SyntaxError:
      return 'varchar'
    if type(t) in [int, long, float]:
      if (type(t) in [int, long]) and current_type not in ['float', 'varchar']:
        # Use smallest possible int type.
        if (-32768 < t < 32767) and current_type not in ['int', 'bigint']:
          return 'smallint'
        elif (-2147483648 < t < 2147483647) and current_type not in ['bigint']:
          return 'int'
        else:
          return 'bigint'
      if type(t) is float and current_type not in ['varchar']:
        return 'decimal'
    else:
      return 'varchar'

# Create connection to the DB.
conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres")

# Files we will use to populate the tables, the indexes must match with respective table.
FILES = ['../Data/2015/accident.csv', '../Data/2015/utilized-accident-data.csv', 
				'../Data/2015/vehicle.csv', '../Data/2015/accident_vehicle_merge.csv']

TABLE_NAMES = ['master_accidents', 'utilized_accidents', 'vehicles', 'accident_vehivle_master']

for index in range(0, len(FILES)):

  cur = conn.cursor()
  with open(FILES[index], 'r') as f:

    reader = csv.reader(f)

    # Used to store the properties of the columns.
    longest, headers, type_list = [], [], []

    # Builds the column definitions in SQL for each header and respective data type.
    for row in reader:
      if len(headers) == 0:
        headers = row
        for col in row:
          longest.append(0)
          type_list.append('')
      else:
        for i in range(len(row)):
          # NA is the csv null value
          if type_list[i] == 'varchar' or row[i] == 'NA':
            pass
          else:
            var_type = dataType(row[i], type_list[i])
            type_list[i] = var_type
        if len(row[i]) > longest[i]:
          longest[i] = len(row[i])

    # Create the table declaration.
    statement = 'create table ' + TABLE_NAMES[index] + ' ('
    for i in range(len(headers)):
        if type_list[i] == 'varchar':
          # Default to 255 if needed, 0 is not allowed.
          if longest[i] == 0:
            longest[i] = 255
            statement = (statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
        else:
            statement = (statement + '\n' + '{} {}' + ',').format(headers[i].lower(), type_list[i])

    statement = statement[:-1] + ');'

    # Drop the table, if it exists, to repopulate it.
    cur.execute("""
    DROP TABLE IF EXISTS """ + TABLE_NAMES[index])
    conn.commit()

    # Create the table using the constructed statement.
    cur.execute(statement)
    conn.commit()

    # Alter each table to make the ST_CASE the Primary Key except the vehicles table.
    if TABLE_NAMES[index] != 'vehicles' :
      statement = 'ALTER TABLE ' + TABLE_NAMES[index] + ' ADD PRIMARY KEY (st_case)'
      cur.execute(statement)
      conn.commit()

  # Reset cursor to beginning of the file and
  # populate the table with all the entries.
    f.seek(0)
    f.readline()
    cur.copy_from(f, TABLE_NAMES[index], sep=',')
    conn.commit()

print("Database constructed and populated successfully.")
