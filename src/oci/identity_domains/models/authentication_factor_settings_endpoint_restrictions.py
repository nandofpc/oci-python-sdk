# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsEndpointRestrictions(object):
    """
    Settings that describe the set of restrictions that the system should apply to devices and trusted endpoints of a user

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsEndpointRestrictions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param max_enrolled_devices:
            The value to assign to the max_enrolled_devices property of this AuthenticationFactorSettingsEndpointRestrictions.
        :type max_enrolled_devices: int

        :param max_trusted_endpoints:
            The value to assign to the max_trusted_endpoints property of this AuthenticationFactorSettingsEndpointRestrictions.
        :type max_trusted_endpoints: int

        :param max_endpoint_trust_duration_in_days:
            The value to assign to the max_endpoint_trust_duration_in_days property of this AuthenticationFactorSettingsEndpointRestrictions.
        :type max_endpoint_trust_duration_in_days: int

        :param trusted_endpoints_enabled:
            The value to assign to the trusted_endpoints_enabled property of this AuthenticationFactorSettingsEndpointRestrictions.
        :type trusted_endpoints_enabled: bool

        :param max_incorrect_attempts:
            The value to assign to the max_incorrect_attempts property of this AuthenticationFactorSettingsEndpointRestrictions.
        :type max_incorrect_attempts: int

        """
        self.swagger_types = {
            'max_enrolled_devices': 'int',
            'max_trusted_endpoints': 'int',
            'max_endpoint_trust_duration_in_days': 'int',
            'trusted_endpoints_enabled': 'bool',
            'max_incorrect_attempts': 'int'
        }

        self.attribute_map = {
            'max_enrolled_devices': 'maxEnrolledDevices',
            'max_trusted_endpoints': 'maxTrustedEndpoints',
            'max_endpoint_trust_duration_in_days': 'maxEndpointTrustDurationInDays',
            'trusted_endpoints_enabled': 'trustedEndpointsEnabled',
            'max_incorrect_attempts': 'maxIncorrectAttempts'
        }

        self._max_enrolled_devices = None
        self._max_trusted_endpoints = None
        self._max_endpoint_trust_duration_in_days = None
        self._trusted_endpoints_enabled = None
        self._max_incorrect_attempts = None

    @property
    def max_enrolled_devices(self):
        """
        **[Required]** Gets the max_enrolled_devices of this AuthenticationFactorSettingsEndpointRestrictions.
        Maximum number of enrolled devices per user

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_enrolled_devices of this AuthenticationFactorSettingsEndpointRestrictions.
        :rtype: int
        """
        return self._max_enrolled_devices

    @max_enrolled_devices.setter
    def max_enrolled_devices(self, max_enrolled_devices):
        """
        Sets the max_enrolled_devices of this AuthenticationFactorSettingsEndpointRestrictions.
        Maximum number of enrolled devices per user

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_enrolled_devices: The max_enrolled_devices of this AuthenticationFactorSettingsEndpointRestrictions.
        :type: int
        """
        self._max_enrolled_devices = max_enrolled_devices

    @property
    def max_trusted_endpoints(self):
        """
        **[Required]** Gets the max_trusted_endpoints of this AuthenticationFactorSettingsEndpointRestrictions.
        Max number of trusted endpoints per user

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_trusted_endpoints of this AuthenticationFactorSettingsEndpointRestrictions.
        :rtype: int
        """
        return self._max_trusted_endpoints

    @max_trusted_endpoints.setter
    def max_trusted_endpoints(self, max_trusted_endpoints):
        """
        Sets the max_trusted_endpoints of this AuthenticationFactorSettingsEndpointRestrictions.
        Max number of trusted endpoints per user

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_trusted_endpoints: The max_trusted_endpoints of this AuthenticationFactorSettingsEndpointRestrictions.
        :type: int
        """
        self._max_trusted_endpoints = max_trusted_endpoints

    @property
    def max_endpoint_trust_duration_in_days(self):
        """
        **[Required]** Gets the max_endpoint_trust_duration_in_days of this AuthenticationFactorSettingsEndpointRestrictions.
        Maximum number of days until an endpoint can be trusted

        **SCIM++ Properties:**
         - idcsMaxValue: 180
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_endpoint_trust_duration_in_days of this AuthenticationFactorSettingsEndpointRestrictions.
        :rtype: int
        """
        return self._max_endpoint_trust_duration_in_days

    @max_endpoint_trust_duration_in_days.setter
    def max_endpoint_trust_duration_in_days(self, max_endpoint_trust_duration_in_days):
        """
        Sets the max_endpoint_trust_duration_in_days of this AuthenticationFactorSettingsEndpointRestrictions.
        Maximum number of days until an endpoint can be trusted

        **SCIM++ Properties:**
         - idcsMaxValue: 180
         - idcsMinValue: 1
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_endpoint_trust_duration_in_days: The max_endpoint_trust_duration_in_days of this AuthenticationFactorSettingsEndpointRestrictions.
        :type: int
        """
        self._max_endpoint_trust_duration_in_days = max_endpoint_trust_duration_in_days

    @property
    def trusted_endpoints_enabled(self):
        """
        **[Required]** Gets the trusted_endpoints_enabled of this AuthenticationFactorSettingsEndpointRestrictions.
        Specify if trusted endpoints are enabled

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The trusted_endpoints_enabled of this AuthenticationFactorSettingsEndpointRestrictions.
        :rtype: bool
        """
        return self._trusted_endpoints_enabled

    @trusted_endpoints_enabled.setter
    def trusted_endpoints_enabled(self, trusted_endpoints_enabled):
        """
        Sets the trusted_endpoints_enabled of this AuthenticationFactorSettingsEndpointRestrictions.
        Specify if trusted endpoints are enabled

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: boolean
         - uniqueness: none


        :param trusted_endpoints_enabled: The trusted_endpoints_enabled of this AuthenticationFactorSettingsEndpointRestrictions.
        :type: bool
        """
        self._trusted_endpoints_enabled = trusted_endpoints_enabled

    @property
    def max_incorrect_attempts(self):
        """
        **[Required]** Gets the max_incorrect_attempts of this AuthenticationFactorSettingsEndpointRestrictions.
        An integer that represents the maximum number of failed MFA logins before an account is locked

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 5
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :return: The max_incorrect_attempts of this AuthenticationFactorSettingsEndpointRestrictions.
        :rtype: int
        """
        return self._max_incorrect_attempts

    @max_incorrect_attempts.setter
    def max_incorrect_attempts(self, max_incorrect_attempts):
        """
        Sets the max_incorrect_attempts of this AuthenticationFactorSettingsEndpointRestrictions.
        An integer that represents the maximum number of failed MFA logins before an account is locked

        **SCIM++ Properties:**
         - idcsMaxValue: 20
         - idcsMinValue: 5
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: integer
         - uniqueness: none


        :param max_incorrect_attempts: The max_incorrect_attempts of this AuthenticationFactorSettingsEndpointRestrictions.
        :type: int
        """
        self._max_incorrect_attempts = max_incorrect_attempts

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other