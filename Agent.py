def recordDeparture(database, flightno, dep_date, time):
	query = """UPDATE sch_flights
			SET act_dep_time = TO_DATE('{0}', 'HH24:MI:SS')
			WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'YYYY-MM-DD')""".format(time, flightno, dep_date)

	database.cursor.execute(query)
	database.commit()

def recordArrival(database, flightno, dep_date, time):
	query = """UPDATE sch_flights
			SET act_arr_time = TO_DATE('{0}', 'HH24:MI:SS')
			WHERE flightno = '{1}' AND dep_date = TO_DATE('{2}', 'YYYY-MM-DD')""".format(time, flightno, dep_date)

	database.cursor.execute(query)
	database.commit()
