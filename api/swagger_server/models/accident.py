# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Accident(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, st_case: str=None, state: str=None, fatals: int=None):  # noqa: E501
        """Accident - a model defined in Swagger

        :param st_case: The st_case of this Accident.  # noqa: E501
        :type st_case: str
        :param state: The state of this Accident.  # noqa: E501
        :type state: str
        :param fatals: The fatals of this Accident.  # noqa: E501
        :type fatals: int
        """
        self.swagger_types = {
            'st_case': str,
            'state': str,
            'fatals': int
        }

        self.attribute_map = {
            'st_case': 'ST_CASE',
            'state': 'STATE',
            'fatals': 'FATALS'
        }

        self._st_case = st_case
        self._state = state
        self._fatals = fatals

    @classmethod
    def from_dict(cls, dikt) -> 'Accident':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Accident of this Accident.  # noqa: E501
        :rtype: Accident
        """
        return util.deserialize_model(dikt, cls)

    @property
    def st_case(self) -> str:
        """Gets the st_case of this Accident.


        :return: The st_case of this Accident.
        :rtype: str
        """
        return self._st_case

    @st_case.setter
    def st_case(self, st_case: str):
        """Sets the st_case of this Accident.


        :param st_case: The st_case of this Accident.
        :type st_case: str
        """

        self._st_case = st_case

    @property
    def state(self) -> str:
        """Gets the state of this Accident.


        :return: The state of this Accident.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this Accident.


        :param state: The state of this Accident.
        :type state: str
        """

        self._state = state

    @property
    def fatals(self) -> int:
        """Gets the fatals of this Accident.


        :return: The fatals of this Accident.
        :rtype: int
        """
        return self._fatals

    @fatals.setter
    def fatals(self, fatals: int):
        """Sets the fatals of this Accident.


        :param fatals: The fatals of this Accident.
        :type fatals: int
        """

        self._fatals = fatals
