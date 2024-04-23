# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ResourceRiskScoreAggregationCollection(object):
    """
    Collection of risk score aggregations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ResourceRiskScoreAggregationCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param filter_type:
            The value to assign to the filter_type property of this ResourceRiskScoreAggregationCollection.
        :type filter_type: str

        :param filter_id:
            The value to assign to the filter_id property of this ResourceRiskScoreAggregationCollection.
        :type filter_id: str

        :param risk_threshold:
            The value to assign to the risk_threshold property of this ResourceRiskScoreAggregationCollection.
        :type risk_threshold: int

        :param items:
            The value to assign to the items property of this ResourceRiskScoreAggregationCollection.
        :type items: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]

        """
        self.swagger_types = {
            'filter_type': 'str',
            'filter_id': 'str',
            'risk_threshold': 'int',
            'items': 'list[ResourceRiskScoreAggregation]'
        }

        self.attribute_map = {
            'filter_type': 'filterType',
            'filter_id': 'filterId',
            'risk_threshold': 'riskThreshold',
            'items': 'items'
        }

        self._filter_type = None
        self._filter_id = None
        self._risk_threshold = None
        self._items = None

    @property
    def filter_type(self):
        """
        **[Required]** Gets the filter_type of this ResourceRiskScoreAggregationCollection.
        Type of filter


        :return: The filter_type of this ResourceRiskScoreAggregationCollection.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """
        Sets the filter_type of this ResourceRiskScoreAggregationCollection.
        Type of filter


        :param filter_type: The filter_type of this ResourceRiskScoreAggregationCollection.
        :type: str
        """
        self._filter_type = filter_type

    @property
    def filter_id(self):
        """
        **[Required]** Gets the filter_id of this ResourceRiskScoreAggregationCollection.
        ID for filter that to be used to filter risk scores


        :return: The filter_id of this ResourceRiskScoreAggregationCollection.
        :rtype: str
        """
        return self._filter_id

    @filter_id.setter
    def filter_id(self, filter_id):
        """
        Sets the filter_id of this ResourceRiskScoreAggregationCollection.
        ID for filter that to be used to filter risk scores


        :param filter_id: The filter_id of this ResourceRiskScoreAggregationCollection.
        :type: str
        """
        self._filter_id = filter_id

    @property
    def risk_threshold(self):
        """
        Gets the risk_threshold of this ResourceRiskScoreAggregationCollection.
        Risk score value that triggers a problem


        :return: The risk_threshold of this ResourceRiskScoreAggregationCollection.
        :rtype: int
        """
        return self._risk_threshold

    @risk_threshold.setter
    def risk_threshold(self, risk_threshold):
        """
        Sets the risk_threshold of this ResourceRiskScoreAggregationCollection.
        Risk score value that triggers a problem


        :param risk_threshold: The risk_threshold of this ResourceRiskScoreAggregationCollection.
        :type: int
        """
        self._risk_threshold = risk_threshold

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ResourceRiskScoreAggregationCollection.
        List of ResourceRiskScoreAggregation resources


        :return: The items of this ResourceRiskScoreAggregationCollection.
        :rtype: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ResourceRiskScoreAggregationCollection.
        List of ResourceRiskScoreAggregation resources


        :param items: The items of this ResourceRiskScoreAggregationCollection.
        :type: list[oci.cloud_guard.models.ResourceRiskScoreAggregation]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
