# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SdmMaskingPolicyDifference(object):
    """
    A SDM masking policy difference resource. It helps track the difference between sensitive columns of SDM and masking columns of the masking policy.
    """

    #: A constant which can be used with the difference_type property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "ALL"
    DIFFERENCE_TYPE_ALL = "ALL"

    #: A constant which can be used with the difference_type property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "NEW"
    DIFFERENCE_TYPE_NEW = "NEW"

    #: A constant which can be used with the difference_type property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "MODIFIED"
    DIFFERENCE_TYPE_MODIFIED = "MODIFIED"

    #: A constant which can be used with the difference_type property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "DELETED"
    DIFFERENCE_TYPE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SdmMaskingPolicyDifference.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SdmMaskingPolicyDifference object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this SdmMaskingPolicyDifference.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this SdmMaskingPolicyDifference.
        :type compartment_id: str

        :param difference_type:
            The value to assign to the difference_type property of this SdmMaskingPolicyDifference.
            Allowed values for this property are: "ALL", "NEW", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type difference_type: str

        :param display_name:
            The value to assign to the display_name property of this SdmMaskingPolicyDifference.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this SdmMaskingPolicyDifference.
        :type time_created: datetime

        :param time_creation_started:
            The value to assign to the time_creation_started property of this SdmMaskingPolicyDifference.
        :type time_creation_started: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SdmMaskingPolicyDifference.
            Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param sensitive_data_model_id:
            The value to assign to the sensitive_data_model_id property of this SdmMaskingPolicyDifference.
        :type sensitive_data_model_id: str

        :param masking_policy_id:
            The value to assign to the masking_policy_id property of this SdmMaskingPolicyDifference.
        :type masking_policy_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SdmMaskingPolicyDifference.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SdmMaskingPolicyDifference.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this SdmMaskingPolicyDifference.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'difference_type': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_creation_started': 'datetime',
            'lifecycle_state': 'str',
            'sensitive_data_model_id': 'str',
            'masking_policy_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'difference_type': 'differenceType',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_creation_started': 'timeCreationStarted',
            'lifecycle_state': 'lifecycleState',
            'sensitive_data_model_id': 'sensitiveDataModelId',
            'masking_policy_id': 'maskingPolicyId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._difference_type = None
        self._display_name = None
        self._time_created = None
        self._time_creation_started = None
        self._lifecycle_state = None
        self._sensitive_data_model_id = None
        self._masking_policy_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this SdmMaskingPolicyDifference.
        The OCID of the SDM masking policy difference.


        :return: The id of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SdmMaskingPolicyDifference.
        The OCID of the SDM masking policy difference.


        :param id: The id of this SdmMaskingPolicyDifference.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this SdmMaskingPolicyDifference.
        The OCID of the compartment that contains the SDM masking policy difference.


        :return: The compartment_id of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SdmMaskingPolicyDifference.
        The OCID of the compartment that contains the SDM masking policy difference.


        :param compartment_id: The compartment_id of this SdmMaskingPolicyDifference.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def difference_type(self):
        """
        **[Required]** Gets the difference_type of this SdmMaskingPolicyDifference.
        The type of the SDM masking policy difference. It defines the difference scope.
        NEW identifies new sensitive columns in the sensitive data model that are not in the masking policy.
        DELETED identifies columns that are present in the masking policy but have been deleted from the sensitive data model.
        MODIFIED identifies columns that are present in the sensitive data model as well as the masking policy but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.

        Allowed values for this property are: "ALL", "NEW", "MODIFIED", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The difference_type of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._difference_type

    @difference_type.setter
    def difference_type(self, difference_type):
        """
        Sets the difference_type of this SdmMaskingPolicyDifference.
        The type of the SDM masking policy difference. It defines the difference scope.
        NEW identifies new sensitive columns in the sensitive data model that are not in the masking policy.
        DELETED identifies columns that are present in the masking policy but have been deleted from the sensitive data model.
        MODIFIED identifies columns that are present in the sensitive data model as well as the masking policy but some of their attributes have been modified.
        ALL covers all the above three scenarios and reports new, deleted and modified columns.


        :param difference_type: The difference_type of this SdmMaskingPolicyDifference.
        :type: str
        """
        allowed_values = ["ALL", "NEW", "MODIFIED", "DELETED"]
        if not value_allowed_none_or_none_sentinel(difference_type, allowed_values):
            difference_type = 'UNKNOWN_ENUM_VALUE'
        self._difference_type = difference_type

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SdmMaskingPolicyDifference.
        The display name of the SDM masking policy difference.


        :return: The display_name of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SdmMaskingPolicyDifference.
        The display name of the SDM masking policy difference.


        :param display_name: The display_name of this SdmMaskingPolicyDifference.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this SdmMaskingPolicyDifference.
        The date and time the SDM masking policy difference was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this SdmMaskingPolicyDifference.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SdmMaskingPolicyDifference.
        The date and time the SDM masking policy difference was created, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this SdmMaskingPolicyDifference.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_creation_started(self):
        """
        **[Required]** Gets the time_creation_started of this SdmMaskingPolicyDifference.
        The date and time the SDM masking policy difference creation started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_creation_started of this SdmMaskingPolicyDifference.
        :rtype: datetime
        """
        return self._time_creation_started

    @time_creation_started.setter
    def time_creation_started(self, time_creation_started):
        """
        Sets the time_creation_started of this SdmMaskingPolicyDifference.
        The date and time the SDM masking policy difference creation started, in the format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_creation_started: The time_creation_started of this SdmMaskingPolicyDifference.
        :type: datetime
        """
        self._time_creation_started = time_creation_started

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SdmMaskingPolicyDifference.
        The current state of the SDM masking policy difference.

        Allowed values for this property are: "CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SdmMaskingPolicyDifference.
        The current state of the SDM masking policy difference.


        :param lifecycle_state: The lifecycle_state of this SdmMaskingPolicyDifference.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def sensitive_data_model_id(self):
        """
        **[Required]** Gets the sensitive_data_model_id of this SdmMaskingPolicyDifference.
        The OCID of the sensitive data model associated with the SDM masking policy difference.


        :return: The sensitive_data_model_id of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._sensitive_data_model_id

    @sensitive_data_model_id.setter
    def sensitive_data_model_id(self, sensitive_data_model_id):
        """
        Sets the sensitive_data_model_id of this SdmMaskingPolicyDifference.
        The OCID of the sensitive data model associated with the SDM masking policy difference.


        :param sensitive_data_model_id: The sensitive_data_model_id of this SdmMaskingPolicyDifference.
        :type: str
        """
        self._sensitive_data_model_id = sensitive_data_model_id

    @property
    def masking_policy_id(self):
        """
        **[Required]** Gets the masking_policy_id of this SdmMaskingPolicyDifference.
        The OCID of the masking policy associated with the SDM masking policy difference.


        :return: The masking_policy_id of this SdmMaskingPolicyDifference.
        :rtype: str
        """
        return self._masking_policy_id

    @masking_policy_id.setter
    def masking_policy_id(self, masking_policy_id):
        """
        Sets the masking_policy_id of this SdmMaskingPolicyDifference.
        The OCID of the masking policy associated with the SDM masking policy difference.


        :param masking_policy_id: The masking_policy_id of this SdmMaskingPolicyDifference.
        :type: str
        """
        self._masking_policy_id = masking_policy_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SdmMaskingPolicyDifference.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SdmMaskingPolicyDifference.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SdmMaskingPolicyDifference.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SdmMaskingPolicyDifference.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SdmMaskingPolicyDifference.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SdmMaskingPolicyDifference.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SdmMaskingPolicyDifference.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SdmMaskingPolicyDifference.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this SdmMaskingPolicyDifference.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this SdmMaskingPolicyDifference.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this SdmMaskingPolicyDifference.
        System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this SdmMaskingPolicyDifference.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
