import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server import util


def get_vehicle(st_case=None, make=None, model=None):  # noqa: E501
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
    return 'do some magic!'


def vehicle_delete(body):  # noqa: E501
    """Delete a record of a vehicle

     # noqa: E501

    :param body: Created user object
    :type body: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        body = Vehicle.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
