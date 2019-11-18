# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.data import Data  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDataController(BaseTestCase):
    """DataController integration test stubs"""

    def test_data_delete(self):
        """Test case for data_delete

        Delete a record from training data
        """
        query_string = [('st_case', 'st_case_example')]
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/data',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data(self):
        """Test case for get_data

        Get data from our model training set
        """
        query_string = [('st_case', 'st_case_example'),
                        ('make', 'make_example'),
                        ('model', 'model_example'),
                        ('mod_year', 56),
                        ('fatals', 56)]
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/data',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_data(self):
        """Test case for post_data

        Post data to our model training set
        """
        body = Data()
        response = self.client.open(
            '/dannymulick1/CARS_Capping2019/1.0.2/data',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
