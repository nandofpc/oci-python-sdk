# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAddonDetails(object):
    """
    The properties that define to update addon details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAddonDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param version:
            The value to assign to the version property of this UpdateAddonDetails.
        :type version: str

        :param configurations:
            The value to assign to the configurations property of this UpdateAddonDetails.
        :type configurations: list[oci.container_engine.models.AddonConfiguration]

        """
        self.swagger_types = {
            'version': 'str',
            'configurations': 'list[AddonConfiguration]'
        }

        self.attribute_map = {
            'version': 'version',
            'configurations': 'configurations'
        }

        self._version = None
        self._configurations = None

    @property
    def version(self):
        """
        Gets the version of this UpdateAddonDetails.
        The version of the installed addon.


        :return: The version of this UpdateAddonDetails.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this UpdateAddonDetails.
        The version of the installed addon.


        :param version: The version of this UpdateAddonDetails.
        :type: str
        """
        self._version = version

    @property
    def configurations(self):
        """
        Gets the configurations of this UpdateAddonDetails.
        Addon configuration details.


        :return: The configurations of this UpdateAddonDetails.
        :rtype: list[oci.container_engine.models.AddonConfiguration]
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """
        Sets the configurations of this UpdateAddonDetails.
        Addon configuration details.


        :param configurations: The configurations of this UpdateAddonDetails.
        :type: list[oci.container_engine.models.AddonConfiguration]
        """
        self._configurations = configurations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other