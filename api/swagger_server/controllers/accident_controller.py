import connexion
import psycopg2
import six
import os

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
    if os.environ["DATABASE_URL"]:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
    else:
        conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM utilized_accidents WHERE ST_CASE = " \
        + body.st_case + ";"
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

    :rtype: List[Accident]
    """
    # Create connection to the DB and cursor.
    if os.environ["DATABASE_URL"]:
        conn = psycopg2.connect(os.environ["DATABASE_URL"])
    else:
        conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")    
    cur = conn.cursor()
    statement = "SELECT * FROM utilized_accidents WHERE"
    toCheck = [st_case, state, fatals]
    toRemove = []
    for i in range(len(toCheck)):
        if toCheck[i] == None:
            toRemove.append(i)
            # toCheck.pop(i)
    toRemove.reverse()
    for j in toRemove:
        toCheck.pop(j)

    if toCheck == []:
        statement = "SELECT * FROM utilized_accidents"

    if st_case != None and state != None and fatals != None:
        statement += " ST_CASE IN ("
        if len(st_case) > 1:
            for caseNum in st_case:
                statement += caseNum
                if caseNum != st_case[-1]:
                    statement += ", "
        else:
            statement += st_case[0]

        statement += ") AND STATE IN ("
        if len(state) > 1:
            for stateName in state:
                statement += str(stateName)
                if stateName != state[-1]:
                    statement += ", "
        else:
            statement += str(state[0])

        statement += ") AND FATALS IN ("
        if len(fatals) > 1:
            for fatal in fatals:
                statement += str(fatal)
                if fatal != fatals[-1]:
                    statement += ", "
        else:
            statement += str(fatals[0])
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
            print(len(toCheck))

            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

        if state != None:
            statement += " STATE IN ("
            if len(state) > 1:
                for stateNum in state:
                    statement += str(stateNum)
                    if stateNum != state[-1]:
                        statement += ", "
            else:
                statement += str(state[0])
            toCheck.remove(state)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

        if fatals != None:
            statement += " FATALS IN ("
            if len(fatals) > 1:
                for fatal in fatals:
                    statement += str(fatal)
                    if fatal != fatals[-1]:
                        statement += ", "
            else:
                statement += str(fatals[0])
            toCheck.remove(fatals)
            if len(toCheck) > 0:
                statement += ") AND"
            else:
                statement += ")"

    statement += ";"
    cur.execute(statement)

    returnAcc = []
    for record in cur.fetchall():
        tempAccident = Accident(state=record[0], st_case=record[1], 
            fatals=record[-2])
        returnAcc.append(tempAccident)
    return returnAcc
