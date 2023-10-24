# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201005

from .database_tools_connection_oracle_database_proxy_client_details import DatabaseToolsConnectionOracleDatabaseProxyClientDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails(DatabaseToolsConnectionOracleDatabaseProxyClientDetails):
    """
    Proxy client information for user name based proxy authentication.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database_tools.models.DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.proxy_authentication_type` attribute
        of this class is ``USER_NAME`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param proxy_authentication_type:
            The value to assign to the proxy_authentication_type property of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
            Allowed values for this property are: "USER_NAME", "NO_PROXY"
        :type proxy_authentication_type: str

        :param user_name:
            The value to assign to the user_name property of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type user_name: str

        :param user_password:
            The value to assign to the user_password property of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type user_password: oci.database_tools.models.DatabaseToolsUserPasswordDetails

        :param roles:
            The value to assign to the roles property of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type roles: list[str]

        """
        self.swagger_types = {
            'proxy_authentication_type': 'str',
            'user_name': 'str',
            'user_password': 'DatabaseToolsUserPasswordDetails',
            'roles': 'list[str]'
        }

        self.attribute_map = {
            'proxy_authentication_type': 'proxyAuthenticationType',
            'user_name': 'userName',
            'user_password': 'userPassword',
            'roles': 'roles'
        }

        self._proxy_authentication_type = None
        self._user_name = None
        self._user_password = None
        self._roles = None
        self._proxy_authentication_type = 'USER_NAME'

    @property
    def user_name(self):
        """
        **[Required]** Gets the user_name of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        The user name.


        :return: The user_name of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        The user name.


        :param user_name: The user_name of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_password(self):
        """
        Gets the user_password of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.

        :return: The user_password of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :rtype: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        return self._user_password

    @user_password.setter
    def user_password(self, user_password):
        """
        Sets the user_password of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.

        :param user_password: The user_password of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type: oci.database_tools.models.DatabaseToolsUserPasswordDetails
        """
        self._user_password = user_password

    @property
    def roles(self):
        """
        Gets the roles of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        A list of database roles for the client. These roles are enabled if the proxy is authorized to use the roles on behalf of the client.


        :return: The roles of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        A list of database roles for the client. These roles are enabled if the proxy is authorized to use the roles on behalf of the client.


        :param roles: The roles of this DatabaseToolsConnectionOracleDatabaseProxyClientUserNameDetails.
        :type: list[str]
        """
        self._roles = roles

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other