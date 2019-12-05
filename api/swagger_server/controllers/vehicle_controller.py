import connexion
import psycopg2
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server import util


def get_vehicle(st_case=None, make=None, model=None, mod_year=None):  # noqa: E501
    """Get a vehicle record

    This can only be done by the logged in user. # noqa: E501

    :param st_case: ST_CASE value of the object(s) to be returned
    :type st_case: List[str]
    :param make: MAKE value of the object(s) to be returned
    :type make: List[str]
    :param model: Model value of the object(s) to be returned
    :type model: List[str]

    :rtype: Vehicle
    """
    # Create connection to the DB and cursor.
    conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()
    statement = "SELECT * FROM vehicles WHERE"
    toCheck = [st_case, make, model, mod_year]
    toRemove = []
    for i in range(len(toCheck)):
        if toCheck[i] == None:
            toRemove.append(i)
            # toCheck.pop(i)
    toRemove.reverse()
    for j in toRemove:
        toCheck.pop(j)

    if toCheck == []:
        statement = "SELECT * FROM vehicles"

    if st_case != None and make != None and model != None and mod_year != None:
        statement += " ST_CASE IN ("
        if len(st_case) > 1:
            for caseNum in st_case:
                statement += caseNum
                if caseNum != st_case[-1]:
                    statement += ", "
        else:
            statement += st_case[0]

        statement += ") AND MAKE IN ("
        if len(make) > 1:
            for makeName in make:
                statement += makeName
                if makeName != make[-1]:
                    statement += ", "
        else:
            statement += make[0]

        statement += ") AND MODEL IN ("
        if len(model) > 1:
            for modelName in model:
                statement += modelName
                if modelName != model[-1]:
                    statement += ", "
        else:
            statement += model[0]

        statement += ") AND MOD_YEAR IN ("
        if len(mod_year) > 1:
            for year in mod_year:
                statement += year
                if year != mod_year[-1]:
                    statement += ", "
        else:
            statement += mod_year[0]
        statement += ")"

    else:
        if st_case != None:
            statement += " ST_CASE IN ("
            if len(st_case) > 1:
                for caseNum in st_case:
                    statement += caseNum
                    if caseNum != st_case[-1]:
                        statement += ", "
            else:
                statement += st_case[0]
            toCheck.remove(st_case)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

        if make != None:
            statement += " MAKE IN ("
            if len(make) > 1:
                for makeName in make:
                    statement += makeName
                    if makeName != make[-1]:
                        statement += ", "
            else:
                statement += make[0]
            toCheck.remove(make)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

        if model != None:
            statement += " MODEL IN ("
            if len(model) > 1:
                for makeName in model:
                    statement += makeName
                    if makeName != model[-1]:
                        statement += ", "
            else:
                statement += model[0]
            toCheck.remove(model)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

        if mod_year != None:
            statement += " MOD_YEAR IN ("
            if len(mod_year) > 1:
                for year in mod_year:
                    statement += year
                    if year != mod_year[-1]:
                        statement += ", "
            else:
                statement += mod_year[0]
            toCheck.remove(mod_year)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

    statement += ";"
    cur.execute(statement)

    returnVeh = []
    for record in cur.fetchall():
        tempVehicle = Vehicle(st_case=record[1], make=record[15], 
            model=record[16], mod_year=record[19])
        returnVeh.append(tempVehicle)
    return returnVeh


def vehicle_delete(body):  # noqa: E501
    """Delete a record of a vehicle

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Vehicle.from_dict(connexion.request.get_json())  # noqa: E501
     # Create connection to the DB and cursor.
    conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM vehicles WHERE ST_CASE = " + body.st_case
    cur.execute(statement)

    # Print result from delete command
    print(cur.statusmessage)

    conn.commit()
    response = ApiResponse(code=200, type="Good", message="Successful delete")
    return response
