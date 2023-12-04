# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SystemVersionSummary(object):
    """
    List of compatible Exadata system versions for a given shape and GI version.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SystemVersionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param shape:
            The value to assign to the shape property of this SystemVersionSummary.
        :type shape: str

        :param gi_version:
            The value to assign to the gi_version property of this SystemVersionSummary.
        :type gi_version: str

        :param system_versions:
            The value to assign to the system_versions property of this SystemVersionSummary.
        :type system_versions: list[str]

        """
        self.swagger_types = {
            'shape': 'str',
            'gi_version': 'str',
            'system_versions': 'list[str]'
        }

        self.attribute_map = {
            'shape': 'shape',
            'gi_version': 'giVersion',
            'system_versions': 'systemVersions'
        }

        self._shape = None
        self._gi_version = None
        self._system_versions = None

    @property
    def shape(self):
        """
        **[Required]** Gets the shape of this SystemVersionSummary.
        Exadata shape.


        :return: The shape of this SystemVersionSummary.
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """
        Sets the shape of this SystemVersionSummary.
        Exadata shape.


        :param shape: The shape of this SystemVersionSummary.
        :type: str
        """
        self._shape = shape

    @property
    def gi_version(self):
        """
        **[Required]** Gets the gi_version of this SystemVersionSummary.
        Grid Infrastructure version.


        :return: The gi_version of this SystemVersionSummary.
        :rtype: str
        """
        return self._gi_version

    @gi_version.setter
    def gi_version(self, gi_version):
        """
        Sets the gi_version of this SystemVersionSummary.
        Grid Infrastructure version.


        :param gi_version: The gi_version of this SystemVersionSummary.
        :type: str
        """
        self._gi_version = gi_version

    @property
    def system_versions(self):
        """
        Gets the system_versions of this SystemVersionSummary.
        Compatible Exadata system versions for a given shape and GI version.


        :return: The system_versions of this SystemVersionSummary.
        :rtype: list[str]
        """
        return self._system_versions

    @system_versions.setter
    def system_versions(self, system_versions):
        """
        Sets the system_versions of this SystemVersionSummary.
        Compatible Exadata system versions for a given shape and GI version.


        :param system_versions: The system_versions of this SystemVersionSummary.
        :type: list[str]
        """
        self._system_versions = system_versions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other