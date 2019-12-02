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
    conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM utilized_accidents WHERE ST_CASE = " + body.st_case
    cur.execute(statement)

    # Print result from delete command
    print(cur.statusmessage)

    conn.commit()
    response = ApiResponse(code=200, type="Good", message="Successful delete")
    return response


def accident_get(st_case=None, state=None):  # noqa: E501
    """Get accident record(s)

    Get an accident&#39;s information by input ST_CASE # noqa: E501

    :param st_case: ST_CASE value of the object(s) to be returned
    :type st_case: List[str]
    :param state: STATE value of the object(s) to be returned
    :type state: List[int]

    :rtype: Accident
    """
    # Create connection to the DB and cursor.
    conn = psycopg2.connect("host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM utilized_accidents WHERE ST_CASE = " + body.st_case
    cur.execute(statement)
    return st_case
