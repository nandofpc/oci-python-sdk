# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .profile import Profile
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GroupProfile(Profile):
    """
    Definition of a registration profile of type GROUP.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GroupProfile object with values from keyword arguments. The default value of the :py:attr:`~oci.os_management_hub.models.GroupProfile.profile_type` attribute
        of this class is ``GROUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GroupProfile.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GroupProfile.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this GroupProfile.
        :type display_name: str

        :param description:
            The value to assign to the description property of this GroupProfile.
        :type description: str

        :param management_station_id:
            The value to assign to the management_station_id property of this GroupProfile.
        :type management_station_id: str

        :param profile_type:
            The value to assign to the profile_type property of this GroupProfile.
            Allowed values for this property are: "SOFTWARESOURCE", "GROUP", "LIFECYCLE", "STATION"
        :type profile_type: str

        :param vendor_name:
            The value to assign to the vendor_name property of this GroupProfile.
            Allowed values for this property are: "ORACLE"
        :type vendor_name: str

        :param os_family:
            The value to assign to the os_family property of this GroupProfile.
            Allowed values for this property are: "ORACLE_LINUX_9", "ORACLE_LINUX_8", "ORACLE_LINUX_7"
        :type os_family: str

        :param arch_type:
            The value to assign to the arch_type property of this GroupProfile.
            Allowed values for this property are: "X86_64", "AARCH64", "I686", "NOARCH", "SRC"
        :type arch_type: str

        :param time_created:
            The value to assign to the time_created property of this GroupProfile.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GroupProfile.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GroupProfile.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GroupProfile.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GroupProfile.
        :type system_tags: dict(str, dict(str, object))

        :param managed_instance_group:
            The value to assign to the managed_instance_group property of this GroupProfile.
        :type managed_instance_group: oci.os_management_hub.models.ManagedInstanceGroupDetails

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'management_station_id': 'str',
            'profile_type': 'str',
            'vendor_name': 'str',
            'os_family': 'str',
            'arch_type': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'managed_instance_group': 'ManagedInstanceGroupDetails'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'management_station_id': 'managementStationId',
            'profile_type': 'profileType',
            'vendor_name': 'vendorName',
            'os_family': 'osFamily',
            'arch_type': 'archType',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'managed_instance_group': 'managedInstanceGroup'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._management_station_id = None
        self._profile_type = None
        self._vendor_name = None
        self._os_family = None
        self._arch_type = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._managed_instance_group = None
        self._profile_type = 'GROUP'

    @property
    def managed_instance_group(self):
        """
        **[Required]** Gets the managed_instance_group of this GroupProfile.

        :return: The managed_instance_group of this GroupProfile.
        :rtype: oci.os_management_hub.models.ManagedInstanceGroupDetails
        """
        return self._managed_instance_group

    @managed_instance_group.setter
    def managed_instance_group(self, managed_instance_group):
        """
        Sets the managed_instance_group of this GroupProfile.

        :param managed_instance_group: The managed_instance_group of this GroupProfile.
        :type: oci.os_management_hub.models.ManagedInstanceGroupDetails
        """
        self._managed_instance_group = managed_instance_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other