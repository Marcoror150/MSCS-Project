import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.data import Data  # noqa: E501
from swagger_server import util


def data_delete(st_case=None):  # noqa: E501
    """Delete a record from training data

     # noqa: E501

    :param st_case: ST_CASE value of the object(s) to be deleted
    :type st_case: List[str]

    :rtype: ApiResponse
    """
    # Create connection to the DB and cursor.
    conn = psycopg2.connect(
        "host=localhost dbname=accidents_raw user=postgres password=password")
    cur = conn.cursor()

    statement = "DELETE FROM accident_vehicle_master WHERE ST_CASE = " + body.st_case
    cur.execute(statement)

    # Print result from delete command
    print(cur.statusmessage)

    conn.commit()
    response = ApiResponse(code=200, type="Good", message="Successful delete")
    return response


def get_data(st_case=None, make=None, model=None, mod_year=None, fatals=None):  # noqa: E501
    """Get data from our model training set

     # noqa: E501

    :param st_case: ST_CASE value of the object(s) to be returned
    :type st_case: List[str]
    :param make: MAKE value of the object(s) to be returned
    :type make: List[str]
    :param model: MODEL value of the object(s) to be returned
    :type model: List[str]
    :param mod_year: MOD_YEAR value of the object(s) to be returned
    :type mod_year: List[int]
    :param fatals: FATALS value of the object(s) to be returned
    :type fatals: List[int]

    :rtype: Data
    """
    return 'do some magic!'


def post_data(body):  # noqa: E501
    """Post data to our model training set

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
