# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ObjectLifecycleRule(object):
    """
    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the time_unit property of a ObjectLifecycleRule.
    #: This constant has a value of "DAYS"
    TIME_UNIT_DAYS = "DAYS"

    #: A constant which can be used with the time_unit property of a ObjectLifecycleRule.
    #: This constant has a value of "YEARS"
    TIME_UNIT_YEARS = "YEARS"

    def __init__(self, **kwargs):
        """
        Initializes a new ObjectLifecycleRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ObjectLifecycleRule.
        :type name: str

        :param action:
            The value to assign to the action property of this ObjectLifecycleRule.
        :type action: str

        :param time_amount:
            The value to assign to the time_amount property of this ObjectLifecycleRule.
        :type time_amount: int

        :param time_unit:
            The value to assign to the time_unit property of this ObjectLifecycleRule.
            Allowed values for this property are: "DAYS", "YEARS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type time_unit: str

        :param is_enabled:
            The value to assign to the is_enabled property of this ObjectLifecycleRule.
        :type is_enabled: bool

        :param object_name_filter:
            The value to assign to the object_name_filter property of this ObjectLifecycleRule.
        :type object_name_filter: ObjectNameFilter

        """
        self.swagger_types = {
            'name': 'str',
            'action': 'str',
            'time_amount': 'int',
            'time_unit': 'str',
            'is_enabled': 'bool',
            'object_name_filter': 'ObjectNameFilter'
        }

        self.attribute_map = {
            'name': 'name',
            'action': 'action',
            'time_amount': 'timeAmount',
            'time_unit': 'timeUnit',
            'is_enabled': 'isEnabled',
            'object_name_filter': 'objectNameFilter'
        }

        self._name = None
        self._action = None
        self._time_amount = None
        self._time_unit = None
        self._is_enabled = None
        self._object_name_filter = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ObjectLifecycleRule.
        The name of the lifecycle rule to be applied.


        :return: The name of this ObjectLifecycleRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ObjectLifecycleRule.
        The name of the lifecycle rule to be applied.


        :param name: The name of this ObjectLifecycleRule.
        :type: str
        """
        self._name = name

    @property
    def action(self):
        """
        **[Required]** Gets the action of this ObjectLifecycleRule.
        The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the
        `Archival Storage tier`__. Rules using the action
        'DELETE' permanently delete objects from buckets. 'ARCHIVE' and 'DELETE' are the only two supported
        actions at this time.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Archive/Concepts/archivestorageoverview.htm


        :return: The action of this ObjectLifecycleRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ObjectLifecycleRule.
        The action of the object lifecycle policy rule. Rules using the action 'ARCHIVE' move objects into the
        `Archival Storage tier`__. Rules using the action
        'DELETE' permanently delete objects from buckets. 'ARCHIVE' and 'DELETE' are the only two supported
        actions at this time.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/Archive/Concepts/archivestorageoverview.htm


        :param action: The action of this ObjectLifecycleRule.
        :type: str
        """
        self._action = action

    @property
    def time_amount(self):
        """
        **[Required]** Gets the time_amount of this ObjectLifecycleRule.
        Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the
        timeUnit parameter, and is calculated in relation to each object's Last-Modified time.


        :return: The time_amount of this ObjectLifecycleRule.
        :rtype: int
        """
        return self._time_amount

    @time_amount.setter
    def time_amount(self, time_amount):
        """
        Sets the time_amount of this ObjectLifecycleRule.
        Specifies the age of objects to apply the rule to. The timeAmount is interpreted in units defined by the
        timeUnit parameter, and is calculated in relation to each object's Last-Modified time.


        :param time_amount: The time_amount of this ObjectLifecycleRule.
        :type: int
        """
        self._time_amount = time_amount

    @property
    def time_unit(self):
        """
        **[Required]** Gets the time_unit of this ObjectLifecycleRule.
        The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC.
        Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.

        Allowed values for this property are: "DAYS", "YEARS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The time_unit of this ObjectLifecycleRule.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """
        Sets the time_unit of this ObjectLifecycleRule.
        The unit that should be used to interpret timeAmount.  Days are defined as starting and ending at midnight UTC.
        Years are defined as 365.2425 days long and likewise round up to the next midnight UTC.


        :param time_unit: The time_unit of this ObjectLifecycleRule.
        :type: str
        """
        allowed_values = ["DAYS", "YEARS"]
        if not value_allowed_none_or_none_sentinel(time_unit, allowed_values):
            time_unit = 'UNKNOWN_ENUM_VALUE'
        self._time_unit = time_unit

    @property
    def is_enabled(self):
        """
        **[Required]** Gets the is_enabled of this ObjectLifecycleRule.
        A boolean that determines whether this rule is currently enabled.


        :return: The is_enabled of this ObjectLifecycleRule.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this ObjectLifecycleRule.
        A boolean that determines whether this rule is currently enabled.


        :param is_enabled: The is_enabled of this ObjectLifecycleRule.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def object_name_filter(self):
        """
        Gets the object_name_filter of this ObjectLifecycleRule.
        A filter limiting object names that the rule will apply to.


        :return: The object_name_filter of this ObjectLifecycleRule.
        :rtype: ObjectNameFilter
        """
        return self._object_name_filter

    @object_name_filter.setter
    def object_name_filter(self, object_name_filter):
        """
        Sets the object_name_filter of this ObjectLifecycleRule.
        A filter limiting object names that the rule will apply to.


        :param object_name_filter: The object_name_filter of this ObjectLifecycleRule.
        :type: ObjectNameFilter
        """
        self._object_name_filter = object_name_filter

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other