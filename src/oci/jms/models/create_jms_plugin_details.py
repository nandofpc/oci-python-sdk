# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210610


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateJmsPluginDetails(object):
    """
    The details for creating a JmsPlugin.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateJmsPluginDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param agent_id:
            The value to assign to the agent_id property of this CreateJmsPluginDetails.
        :type agent_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateJmsPluginDetails.
        :type compartment_id: str

        :param fleet_id:
            The value to assign to the fleet_id property of this CreateJmsPluginDetails.
        :type fleet_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateJmsPluginDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateJmsPluginDetails.
        :type freeform_tags: dict(str, str)

        """
        self.swagger_types = {
            'agent_id': 'str',
            'compartment_id': 'str',
            'fleet_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'compartment_id': 'compartmentId',
            'fleet_id': 'fleetId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags'
        }

        self._agent_id = None
        self._compartment_id = None
        self._fleet_id = None
        self._defined_tags = None
        self._freeform_tags = None

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this CreateJmsPluginDetails.
        The `OCID`__ of the Management Agent (OMA) or the Oracle Cloud Agent (OCA) instance where the JMS plugin is deployed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this CreateJmsPluginDetails.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this CreateJmsPluginDetails.
        The `OCID`__ of the Management Agent (OMA) or the Oracle Cloud Agent (OCA) instance where the JMS plugin is deployed.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this CreateJmsPluginDetails.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateJmsPluginDetails.
        The OMA/OCA agent's compartment `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateJmsPluginDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateJmsPluginDetails.
        The OMA/OCA agent's compartment `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateJmsPluginDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fleet_id(self):
        """
        Gets the fleet_id of this CreateJmsPluginDetails.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The fleet_id of this CreateJmsPluginDetails.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this CreateJmsPluginDetails.
        The `OCID`__ of the fleet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param fleet_id: The fleet_id of this CreateJmsPluginDetails.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateJmsPluginDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :return: The defined_tags of this CreateJmsPluginDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateJmsPluginDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`. (See `Understanding Free-form Tags`__).

        __ https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm


        :param defined_tags: The defined_tags of this CreateJmsPluginDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateJmsPluginDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :return: The freeform_tags of this CreateJmsPluginDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateJmsPluginDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`. (See `Managing Tags and Tag Namespaces`__.)

        __ https://docs.cloud.oracle.com/Content/Tagging/Concepts/understandingfreeformtags.htm


        :param freeform_tags: The freeform_tags of this CreateJmsPluginDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other