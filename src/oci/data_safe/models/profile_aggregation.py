# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProfileAggregation(object):
    """
    The profile aggregation provides information about the user profiles available on the database.
    For example, the user profile details include how many users have a given profile assigned
    and how many profiles have password verification function.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProfileAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this ProfileAggregation.
        :type items: list[dict(str, object)]

        :param user_assessment_id:
            The value to assign to the user_assessment_id property of this ProfileAggregation.
        :type user_assessment_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ProfileAggregation.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this ProfileAggregation.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this ProfileAggregation.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'items': 'list[dict(str, object)]',
            'user_assessment_id': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'items': 'items',
            'user_assessment_id': 'userAssessmentId',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._items = None
        self._user_assessment_id = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def items(self):
        """
        Gets the items of this ProfileAggregation.
        The array of profile aggregation data.


        :return: The items of this ProfileAggregation.
        :rtype: list[dict(str, object)]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ProfileAggregation.
        The array of profile aggregation data.


        :param items: The items of this ProfileAggregation.
        :type: list[dict(str, object)]
        """
        self._items = items

    @property
    def user_assessment_id(self):
        """
        **[Required]** Gets the user_assessment_id of this ProfileAggregation.
        The OCID of the latest user assessment corresponding to the target under consideration. A compartment
        type assessment can also be passed to profiles from all the targets from the corresponding compartment.


        :return: The user_assessment_id of this ProfileAggregation.
        :rtype: str
        """
        return self._user_assessment_id

    @user_assessment_id.setter
    def user_assessment_id(self, user_assessment_id):
        """
        Sets the user_assessment_id of this ProfileAggregation.
        The OCID of the latest user assessment corresponding to the target under consideration. A compartment
        type assessment can also be passed to profiles from all the targets from the corresponding compartment.


        :param user_assessment_id: The user_assessment_id of this ProfileAggregation.
        :type: str
        """
        self._user_assessment_id = user_assessment_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ProfileAggregation.
        The OCID of the compartment that contains the user assessment.


        :return: The compartment_id of this ProfileAggregation.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ProfileAggregation.
        The OCID of the compartment that contains the user assessment.


        :param compartment_id: The compartment_id of this ProfileAggregation.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this ProfileAggregation.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this ProfileAggregation.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this ProfileAggregation.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this ProfileAggregation.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this ProfileAggregation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this ProfileAggregation.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this ProfileAggregation.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this ProfileAggregation.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
