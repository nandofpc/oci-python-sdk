# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20170907


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Configuration(object):
    """
    Tenancy level customer email configuration details.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Configuration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this Configuration.
        :type compartment_id: str

        :param http_submit_endpoint:
            The value to assign to the http_submit_endpoint property of this Configuration.
        :type http_submit_endpoint: str

        :param smtp_submit_endpoint:
            The value to assign to the smtp_submit_endpoint property of this Configuration.
        :type smtp_submit_endpoint: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'http_submit_endpoint': 'str',
            'smtp_submit_endpoint': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'http_submit_endpoint': 'httpSubmitEndpoint',
            'smtp_submit_endpoint': 'smtpSubmitEndpoint'
        }

        self._compartment_id = None
        self._http_submit_endpoint = None
        self._smtp_submit_endpoint = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Configuration.
        The root compartment `OCID`__ (same as the tenancy OCID)

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Configuration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Configuration.
        The root compartment `OCID`__ (same as the tenancy OCID)

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Configuration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def http_submit_endpoint(self):
        """
        **[Required]** Gets the http_submit_endpoint of this Configuration.
        Endpoint used to submit emails via the HTTP email submission API


        :return: The http_submit_endpoint of this Configuration.
        :rtype: str
        """
        return self._http_submit_endpoint

    @http_submit_endpoint.setter
    def http_submit_endpoint(self, http_submit_endpoint):
        """
        Sets the http_submit_endpoint of this Configuration.
        Endpoint used to submit emails via the HTTP email submission API


        :param http_submit_endpoint: The http_submit_endpoint of this Configuration.
        :type: str
        """
        self._http_submit_endpoint = http_submit_endpoint

    @property
    def smtp_submit_endpoint(self):
        """
        **[Required]** Gets the smtp_submit_endpoint of this Configuration.
        Endpoint used to submit emails via the standard SMTP submission protocol. Note that TLS 1.2 and standard SMTP authentication is required for submission.


        :return: The smtp_submit_endpoint of this Configuration.
        :rtype: str
        """
        return self._smtp_submit_endpoint

    @smtp_submit_endpoint.setter
    def smtp_submit_endpoint(self, smtp_submit_endpoint):
        """
        Sets the smtp_submit_endpoint of this Configuration.
        Endpoint used to submit emails via the standard SMTP submission protocol. Note that TLS 1.2 and standard SMTP authentication is required for submission.


        :param smtp_submit_endpoint: The smtp_submit_endpoint of this Configuration.
        :type: str
        """
        self._smtp_submit_endpoint = smtp_submit_endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other