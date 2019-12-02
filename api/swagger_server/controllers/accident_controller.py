import connexion
import psycopg2
import six

from swagger_server.models.accident import Accident  # noqa: E501
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util


def accident_delete(body):  # noqa: E501
    """Delete a record of an accident

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Accident.from_dict(connexion.request.get_json())  # noqa: E501

    # Create connection to the DB and cursor.
    conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM utilized_accidents WHERE ST_CASE = " + body.st_case
    cur.execute(statement)

    # Print result from delete command
    print(cur.statusmessage)

    conn.commit()
    response = ApiResponse(code=200, type="Good", message="Successful delete")
    return response


def accident_get(st_case=None, state=None, fatals=None):  # noqa: E501
    """Get accident record(s)

    Get an accident&#39;s information by input ST_CASE # noqa: E501

    :param st_case: ST_CASE value of the object(s) to be returned
    :type st_case: List[str]
    :param state: STATE value of the object(s) to be returned
    :type state: List[int]

    :rtype: Accident
    """
    # Create connection to the DB and cursor.
    conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    if st_case != None and state != None and fatals != None:
        statement = "SELECT * FROM utilized_accidents WHERE ST_CASE IN ("
        if len(st_case > 1):
            for caseNum in st_case:
                statement += caseNum
                if caseNum != st_case[-1]:
                    statement += ", "
        else:
            statement += st_case[0]
        statement += ") "

        statement += "AND STATE IN ("
        if len(state > 1):
            for stateName in state:
                statement += stateName
                if stateName != state[-1]:
                    statement += ", "
        else:
            statement += state[0]
        statement += ") "

        statement += "AND FATALS IN ("
        if len(fatals > 1):
            for fatal in fatals:
                statement += fatal
                if fatals != fatals[-1]:
                    statement += ", "
        else:
            statement += fatals[0]
        statement += ")"

    else if st_case != None:
        statement = "SELECT * FROM utilized_accidents WHERE ST_CASE IN ("
        if len(st_case > 1):
            for caseNum in st_case:
                statement += caseNum
                if caseNum != st_case[-1]:
                    statement += ", "
        else:
            statement += st_case[0]
        statement += ")"

    else if state != None:
        statement += "AND STATE IN ("
        if len(state > 1):
            for stateName in state:
                statement += stateName
                if stateName != state[-1]:
                    statement += ", "
        else:
            statement += state[0]
        statement += ")"

    else if fatals != None:
        statement += "AND FATALS IN ("
        if len(fatals > 1):
            for fatal in fatals:
                statement += fatal
                if fatals != fatals[-1]:
                    statement += ", "
        else:
            statement += fatals[0]
        statement += ")"
        
    else:
        statement = "SELECT * FROM utilized_accidents"
    statement += ";"
    cur.execute(statement)

    returnAcc = []
    for record in cur.fetchall():
        tempAccident = Accident(state=record[0], st_case=record[1], 
        fatals=record[-2])
        returnAcc.append(tempAccident)
    return returnAcc
