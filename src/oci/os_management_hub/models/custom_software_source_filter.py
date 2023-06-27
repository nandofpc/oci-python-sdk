# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CustomSoftwareSourceFilter(object):
    """
    Used to apply filters to a VendorSoftwareSource to create/update CustomSoftwareSources.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CustomSoftwareSourceFilter object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param package_filters:
            The value to assign to the package_filters property of this CustomSoftwareSourceFilter.
        :type package_filters: list[oci.os_management_hub.models.PackageFilter]

        :param module_stream_profile_filters:
            The value to assign to the module_stream_profile_filters property of this CustomSoftwareSourceFilter.
        :type module_stream_profile_filters: list[oci.os_management_hub.models.ModuleStreamProfileFilter]

        :param package_group_filters:
            The value to assign to the package_group_filters property of this CustomSoftwareSourceFilter.
        :type package_group_filters: list[oci.os_management_hub.models.PackageGroupFilter]

        """
        self.swagger_types = {
            'package_filters': 'list[PackageFilter]',
            'module_stream_profile_filters': 'list[ModuleStreamProfileFilter]',
            'package_group_filters': 'list[PackageGroupFilter]'
        }

        self.attribute_map = {
            'package_filters': 'packageFilters',
            'module_stream_profile_filters': 'moduleStreamProfileFilters',
            'package_group_filters': 'packageGroupFilters'
        }

        self._package_filters = None
        self._module_stream_profile_filters = None
        self._package_group_filters = None

    @property
    def package_filters(self):
        """
        Gets the package_filters of this CustomSoftwareSourceFilter.
        The list of package filters.


        :return: The package_filters of this CustomSoftwareSourceFilter.
        :rtype: list[oci.os_management_hub.models.PackageFilter]
        """
        return self._package_filters

    @package_filters.setter
    def package_filters(self, package_filters):
        """
        Sets the package_filters of this CustomSoftwareSourceFilter.
        The list of package filters.


        :param package_filters: The package_filters of this CustomSoftwareSourceFilter.
        :type: list[oci.os_management_hub.models.PackageFilter]
        """
        self._package_filters = package_filters

    @property
    def module_stream_profile_filters(self):
        """
        Gets the module_stream_profile_filters of this CustomSoftwareSourceFilter.
        The list of module stream/profile filters.


        :return: The module_stream_profile_filters of this CustomSoftwareSourceFilter.
        :rtype: list[oci.os_management_hub.models.ModuleStreamProfileFilter]
        """
        return self._module_stream_profile_filters

    @module_stream_profile_filters.setter
    def module_stream_profile_filters(self, module_stream_profile_filters):
        """
        Sets the module_stream_profile_filters of this CustomSoftwareSourceFilter.
        The list of module stream/profile filters.


        :param module_stream_profile_filters: The module_stream_profile_filters of this CustomSoftwareSourceFilter.
        :type: list[oci.os_management_hub.models.ModuleStreamProfileFilter]
        """
        self._module_stream_profile_filters = module_stream_profile_filters

    @property
    def package_group_filters(self):
        """
        Gets the package_group_filters of this CustomSoftwareSourceFilter.
        The list of group filters.


        :return: The package_group_filters of this CustomSoftwareSourceFilter.
        :rtype: list[oci.os_management_hub.models.PackageGroupFilter]
        """
        return self._package_group_filters

    @package_group_filters.setter
    def package_group_filters(self, package_group_filters):
        """
        Sets the package_group_filters of this CustomSoftwareSourceFilter.
        The list of group filters.


        :param package_group_filters: The package_group_filters of this CustomSoftwareSourceFilter.
        :type: list[oci.os_management_hub.models.PackageGroupFilter]
        """
        self._package_group_filters = package_group_filters

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other