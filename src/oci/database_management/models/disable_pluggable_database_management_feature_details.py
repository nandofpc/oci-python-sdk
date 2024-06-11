# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DisablePluggableDatabaseManagementFeatureDetails(object):
    """
    The details required to disable a Database Management feature for an Oracle cloud pluggable database.
    """

    #: A constant which can be used with the feature property of a DisablePluggableDatabaseManagementFeatureDetails.
    #: This constant has a value of "DIAGNOSTICS_AND_MANAGEMENT"
    FEATURE_DIAGNOSTICS_AND_MANAGEMENT = "DIAGNOSTICS_AND_MANAGEMENT"

    def __init__(self, **kwargs):
        """
        Initializes a new DisablePluggableDatabaseManagementFeatureDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param feature:
            The value to assign to the feature property of this DisablePluggableDatabaseManagementFeatureDetails.
            Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT"
        :type feature: str

        """
        self.swagger_types = {
            'feature': 'str'
        }

        self.attribute_map = {
            'feature': 'feature'
        }

        self._feature = None

    @property
    def feature(self):
        """
        **[Required]** Gets the feature of this DisablePluggableDatabaseManagementFeatureDetails.
        The name of the Database Management feature.

        Allowed values for this property are: "DIAGNOSTICS_AND_MANAGEMENT"


        :return: The feature of this DisablePluggableDatabaseManagementFeatureDetails.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """
        Sets the feature of this DisablePluggableDatabaseManagementFeatureDetails.
        The name of the Database Management feature.


        :param feature: The feature of this DisablePluggableDatabaseManagementFeatureDetails.
        :type: str
        """
        allowed_values = ["DIAGNOSTICS_AND_MANAGEMENT"]
        if not value_allowed_none_or_none_sentinel(feature, allowed_values):
            raise ValueError(
                f"Invalid value for `feature`, must be None or one of {allowed_values}"
            )
        self._feature = feature

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other