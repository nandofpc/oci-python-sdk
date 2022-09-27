# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .search_details import SearchDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StructuredSearchDetails(SearchDetails):
    """
    A request that uses Search's structured query language to specify filter conditions to apply to search results.
    For more information about writing queries, see `Search Language Syntax`__.

    __ https://docs.oracle.com/iaas/Content/Search/Concepts/querysyntax.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StructuredSearchDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_search.models.StructuredSearchDetails.type` attribute
        of this class is ``Structured`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this StructuredSearchDetails.
        :type type: str

        :param matching_context_type:
            The value to assign to the matching_context_type property of this StructuredSearchDetails.
            Allowed values for this property are: "NONE", "HIGHLIGHTS"
        :type matching_context_type: str

        :param query:
            The value to assign to the query property of this StructuredSearchDetails.
        :type query: str

        """
        self.swagger_types = {
            'type': 'str',
            'matching_context_type': 'str',
            'query': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'matching_context_type': 'matchingContextType',
            'query': 'query'
        }

        self._type = None
        self._matching_context_type = None
        self._query = None
        self._type = 'Structured'

    @property
    def query(self):
        """
        **[Required]** Gets the query of this StructuredSearchDetails.
        The structured query describing which resources to search for.


        :return: The query of this StructuredSearchDetails.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """
        Sets the query of this StructuredSearchDetails.
        The structured query describing which resources to search for.


        :param query: The query of this StructuredSearchDetails.
        :type: str
        """
        self._query = query

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
