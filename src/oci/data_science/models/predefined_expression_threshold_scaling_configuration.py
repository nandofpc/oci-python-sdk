# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .scaling_configuration import ScalingConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PredefinedExpressionThresholdScalingConfiguration(ScalingConfiguration):
    """
    The scaling configuration for the predefined metric expression rule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PredefinedExpressionThresholdScalingConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.PredefinedExpressionThresholdScalingConfiguration.scaling_configuration_type` attribute
        of this class is ``THRESHOLD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param scaling_configuration_type:
            The value to assign to the scaling_configuration_type property of this PredefinedExpressionThresholdScalingConfiguration.
            Allowed values for this property are: "THRESHOLD", "QUERY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type scaling_configuration_type: str

        :param pending_duration:
            The value to assign to the pending_duration property of this PredefinedExpressionThresholdScalingConfiguration.
        :type pending_duration: str

        :param instance_count_adjustment:
            The value to assign to the instance_count_adjustment property of this PredefinedExpressionThresholdScalingConfiguration.
        :type instance_count_adjustment: int

        :param threshold:
            The value to assign to the threshold property of this PredefinedExpressionThresholdScalingConfiguration.
        :type threshold: int

        """
        self.swagger_types = {
            'scaling_configuration_type': 'str',
            'pending_duration': 'str',
            'instance_count_adjustment': 'int',
            'threshold': 'int'
        }

        self.attribute_map = {
            'scaling_configuration_type': 'scalingConfigurationType',
            'pending_duration': 'pendingDuration',
            'instance_count_adjustment': 'instanceCountAdjustment',
            'threshold': 'threshold'
        }

        self._scaling_configuration_type = None
        self._pending_duration = None
        self._instance_count_adjustment = None
        self._threshold = None
        self._scaling_configuration_type = 'THRESHOLD'

    @property
    def threshold(self):
        """
        **[Required]** Gets the threshold of this PredefinedExpressionThresholdScalingConfiguration.
        A metric value at which the scaling operation will be triggered.


        :return: The threshold of this PredefinedExpressionThresholdScalingConfiguration.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """
        Sets the threshold of this PredefinedExpressionThresholdScalingConfiguration.
        A metric value at which the scaling operation will be triggered.


        :param threshold: The threshold of this PredefinedExpressionThresholdScalingConfiguration.
        :type: int
        """
        self._threshold = threshold

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other