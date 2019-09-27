import psycopg2

# Create connection to the DB.
conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres")

cur = conn.cursor()
with open('Test_Python_Insert.csv', 'r') as f:

# cur.execute('')

	# Drop the table if it exists, to repopulate it.
	cur.execute("""
	DROP TABLE IF EXISTS Master;
	""")
	conn.commit()

	# Create master table containing all information fromd data set.
	cur.execute("""
	CREATE TABLE Master(
	STATE integer PRIMARY KEY,
	ST_CASE integer,
	VE_TOTAL integer,
	VE_FORMS integer,
	PVH_INVL integer
	)
	""")
	conn.commit()

	# Skip the header row.
	next(f)

	cur.copy_from(f, 'Master', sep=',')
	conn.commit()