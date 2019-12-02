# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Data(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, st_case: str=None, make: str=None, model: str=None, mod_year: int=None, fatals: int=None):  # noqa: E501
        """Data - a model defined in Swagger

        :param st_case: The st_case of this Data.  # noqa: E501
        :type st_case: str
        :param make: The make of this Data.  # noqa: E501
        :type make: str
        :param model: The model of this Data.  # noqa: E501
        :type model: str
        :param mod_year: The mod_year of this Data.  # noqa: E501
        :type mod_year: int
        :param fatals: The fatals of this Data.  # noqa: E501
        :type fatals: int
        """
        self.swagger_types = {
            'st_case': str,
            'make': str,
            'model': str,
            'mod_year': int,
            'fatals': int
        }

        self.attribute_map = {
            'st_case': 'ST_CASE',
            'make': 'MAKE',
            'model': 'MODEL',
            'mod_year': 'MOD_YEAR',
            'fatals': 'FATALS'
        }

        self._st_case = st_case
        self._make = make
        self._model = model
        self._mod_year = mod_year
        self._fatals = fatals

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def st_case(self) -> str:
        """Gets the st_case of this Data.


        :return: The st_case of this Data.
        :rtype: str
        """
        return self._st_case

    @st_case.setter
    def st_case(self, st_case: str):
        """Sets the st_case of this Data.


        :param st_case: The st_case of this Data.
        :type st_case: str
        """

        self._st_case = st_case

    @property
    def make(self) -> str:
        """Gets the make of this Data.


        :return: The make of this Data.
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make: str):
        """Sets the make of this Data.


        :param make: The make of this Data.
        :type make: str
        """

        self._make = make

    @property
    def model(self) -> str:
        """Gets the model of this Data.


        :return: The model of this Data.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model: str):
        """Sets the model of this Data.


        :param model: The model of this Data.
        :type model: str
        """

        self._model = model

    @property
    def mod_year(self) -> int:
        """Gets the mod_year of this Data.


        :return: The mod_year of this Data.
        :rtype: int
        """
        return self._mod_year

    @mod_year.setter
    def mod_year(self, mod_year: int):
        """Sets the mod_year of this Data.


        :param mod_year: The mod_year of this Data.
        :type mod_year: int
        """

        self._mod_year = mod_year

    @property
    def fatals(self) -> int:
        """Gets the fatals of this Data.


        :return: The fatals of this Data.
        :rtype: int
        """
        return self._fatals

    @fatals.setter
    def fatals(self, fatals: int):
        """Sets the fatals of this Data.


        :param fatals: The fatals of this Data.
        :type fatals: int
        """

        self._fatals = fatals