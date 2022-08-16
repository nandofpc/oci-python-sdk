# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RecommendationExampleLine(object):
    """
    An example line of the recommendation
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RecommendationExampleLine object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this RecommendationExampleLine.
        :type operation: str

        :param comment:
            The value to assign to the comment property of this RecommendationExampleLine.
        :type comment: str

        """
        self.swagger_types = {
            'operation': 'str',
            'comment': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'comment': 'comment'
        }

        self._operation = None
        self._comment = None

    @property
    def operation(self):
        """
        Gets the operation of this RecommendationExampleLine.
        The details of the example operation.


        :return: The operation of this RecommendationExampleLine.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this RecommendationExampleLine.
        The details of the example operation.


        :param operation: The operation of this RecommendationExampleLine.
        :type: str
        """
        self._operation = operation

    @property
    def comment(self):
        """
        Gets the comment of this RecommendationExampleLine.
        The comments about the operation.


        :return: The comment of this RecommendationExampleLine.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this RecommendationExampleLine.
        The comments about the operation.


        :param comment: The comment of this RecommendationExampleLine.
        :type: str
        """
        self._comment = comment

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other