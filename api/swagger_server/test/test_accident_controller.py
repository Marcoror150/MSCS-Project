# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.accident import Accident  # noqa: E501
from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAccidentController(BaseTestCase):
    """AccidentController integration test stubs"""

    def test_accident_delete(self):
        """Test case for accident_delete

        Delete a record of an accident
        """
        body = Accident()
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/accident',
            method='DELETE',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_accident_get(self):
        """Test case for accident_get

        Get accident record(s)
        """
        query_string = [('st_case', 'st_case_example'),
                        ('state', 56)]
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/accident',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
