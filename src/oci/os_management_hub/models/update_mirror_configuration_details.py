# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMirrorConfigurationDetails(object):
    """
    Information for updating a mirror configuration
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMirrorConfigurationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param directory:
            The value to assign to the directory property of this UpdateMirrorConfigurationDetails.
        :type directory: str

        :param port:
            The value to assign to the port property of this UpdateMirrorConfigurationDetails.
        :type port: str

        :param sslport:
            The value to assign to the sslport property of this UpdateMirrorConfigurationDetails.
        :type sslport: str

        :param sslcert:
            The value to assign to the sslcert property of this UpdateMirrorConfigurationDetails.
        :type sslcert: str

        """
        self.swagger_types = {
            'directory': 'str',
            'port': 'str',
            'sslport': 'str',
            'sslcert': 'str'
        }

        self.attribute_map = {
            'directory': 'directory',
            'port': 'port',
            'sslport': 'sslport',
            'sslcert': 'sslcert'
        }

        self._directory = None
        self._port = None
        self._sslport = None
        self._sslcert = None

    @property
    def directory(self):
        """
        **[Required]** Gets the directory of this UpdateMirrorConfigurationDetails.
        Directory for the mirroring


        :return: The directory of this UpdateMirrorConfigurationDetails.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """
        Sets the directory of this UpdateMirrorConfigurationDetails.
        Directory for the mirroring


        :param directory: The directory of this UpdateMirrorConfigurationDetails.
        :type: str
        """
        self._directory = directory

    @property
    def port(self):
        """
        **[Required]** Gets the port of this UpdateMirrorConfigurationDetails.
        Default port for the mirror


        :return: The port of this UpdateMirrorConfigurationDetails.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this UpdateMirrorConfigurationDetails.
        Default port for the mirror


        :param port: The port of this UpdateMirrorConfigurationDetails.
        :type: str
        """
        self._port = port

    @property
    def sslport(self):
        """
        **[Required]** Gets the sslport of this UpdateMirrorConfigurationDetails.
        Default sslport for the mirror


        :return: The sslport of this UpdateMirrorConfigurationDetails.
        :rtype: str
        """
        return self._sslport

    @sslport.setter
    def sslport(self, sslport):
        """
        Sets the sslport of this UpdateMirrorConfigurationDetails.
        Default sslport for the mirror


        :param sslport: The sslport of this UpdateMirrorConfigurationDetails.
        :type: str
        """
        self._sslport = sslport

    @property
    def sslcert(self):
        """
        Gets the sslcert of this UpdateMirrorConfigurationDetails.
        Local path for the sslcert


        :return: The sslcert of this UpdateMirrorConfigurationDetails.
        :rtype: str
        """
        return self._sslcert

    @sslcert.setter
    def sslcert(self, sslcert):
        """
        Sets the sslcert of this UpdateMirrorConfigurationDetails.
        Local path for the sslcert


        :param sslcert: The sslcert of this UpdateMirrorConfigurationDetails.
        :type: str
        """
        self._sslcert = sslcert

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other