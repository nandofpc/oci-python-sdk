# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceAdditionalDetails(object):
    """
    Optional details of a resource
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceAdditionalDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param os_info:
            The value to assign to the os_info property of this ResourceAdditionalDetails.
        :type os_info: str

        """
        self.swagger_types = {
            'os_info': 'str'
        }

        self.attribute_map = {
            'os_info': 'osInfo'
        }

        self._os_info = None

    @property
    def os_info(self):
        """
        Gets the os_info of this ResourceAdditionalDetails.
        Type of OS present in the resource


        :return: The os_info of this ResourceAdditionalDetails.
        :rtype: str
        """
        return self._os_info

    @os_info.setter
    def os_info(self, os_info):
        """
        Sets the os_info of this ResourceAdditionalDetails.
        Type of OS present in the resource


        :param os_info: The os_info of this ResourceAdditionalDetails.
        :type: str
        """
        self._os_info = os_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other