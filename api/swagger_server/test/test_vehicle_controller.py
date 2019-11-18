# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.vehicle import Vehicle  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVehicleController(BaseTestCase):
    """VehicleController integration test stubs"""

    def test_get_vehicle(self):
        """Test case for get_vehicle

        Get a vehicle record
        """
        query_string = [('st_case', 'st_case_example'),
                        ('make', 'make_example'),
                        ('model', 'model_example')]
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/vehicle',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vehicle_delete(self):
        """Test case for vehicle_delete

        Delete a record of a vehicle
        """
        body = Vehicle()
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/vehicle',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
