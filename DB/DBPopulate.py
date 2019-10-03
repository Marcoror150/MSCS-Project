import psycopg2, csv, ast

def dataType(val, current_type):
    try:
        # Evaluates numbers to an appropriate type, and strings an error
        t = ast.literal_eval(val)
    except ValueError:
			return 'varchar'
    except SyntaxError:
			return 'varchar'
    if type(t) in [int, long, float]:
			if (type(t) in [int, long]) and current_type not in ['float', 'varchar']:
				# Use smallest possible int type
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

cur = conn.cursor()
with open('../Data/2015/accident.csv', 'r') as f:

	reader = csv.reader(f)
	
	# Used to store the properties of the columns.
	longest, headers, type_list = [], [], []


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

	# Create the master table declaration.
	statement = 'create table master ('
	for i in range(len(headers)):
			if type_list[i] == 'varchar':
				if longest[i] == 0:
					longest[i] = 255
					statement = (statement + '\n{} varchar({}),').format(headers[i].lower(), str(longest[i]))
			else:
					statement = (statement + '\n' + '{} {}' + ',').format(headers[i].lower(), type_list[i])

	statement = statement[:-1] + ');'

	print(statement)


	# Drop the table if it exists, to repopulate it.
	cur.execute("""
	DROP TABLE IF EXISTS Master;
	""")
	conn.commit()

	# Create the table using the constructed statement.
	cur.execute(statement)
	conn.commit()

	# Skip the header row.
	# f.readline()

	# cur.copy_from(f, 'Master', sep=',')
	# conn.commit()