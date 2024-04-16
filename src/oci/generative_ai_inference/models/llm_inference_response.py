# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LlmInferenceResponse(object):
    """
    The base class for inference responses.
    """

    #: A constant which can be used with the runtime_type property of a LlmInferenceResponse.
    #: This constant has a value of "COHERE"
    RUNTIME_TYPE_COHERE = "COHERE"

    #: A constant which can be used with the runtime_type property of a LlmInferenceResponse.
    #: This constant has a value of "LLAMA"
    RUNTIME_TYPE_LLAMA = "LLAMA"

    #: A constant which can be used with the runtime_type property of a LlmInferenceResponse.
    #: This constant has a value of "OPENAI"
    RUNTIME_TYPE_OPENAI = "OPENAI"

    #: A constant which can be used with the runtime_type property of a LlmInferenceResponse.
    #: This constant has a value of "DALLE3"
    RUNTIME_TYPE_DALLE3 = "DALLE3"

    def __init__(self, **kwargs):
        """
        Initializes a new LlmInferenceResponse object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.generative_ai_inference.models.LlamaLlmInferenceResponse`
        * :class:`~oci.generative_ai_inference.models.CohereLlmInferenceResponse`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param runtime_type:
            The value to assign to the runtime_type property of this LlmInferenceResponse.
            Allowed values for this property are: "COHERE", "LLAMA", "OPENAI", "DALLE3", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type runtime_type: str

        """
        self.swagger_types = {
            'runtime_type': 'str'
        }

        self.attribute_map = {
            'runtime_type': 'runtimeType'
        }

        self._runtime_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['runtimeType']

        if type == 'LLAMA':
            return 'LlamaLlmInferenceResponse'

        if type == 'COHERE':
            return 'CohereLlmInferenceResponse'
        else:
            return 'LlmInferenceResponse'

    @property
    def runtime_type(self):
        """
        **[Required]** Gets the runtime_type of this LlmInferenceResponse.
        The runtime of the provided model.

        Allowed values for this property are: "COHERE", "LLAMA", "OPENAI", "DALLE3", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The runtime_type of this LlmInferenceResponse.
        :rtype: str
        """
        return self._runtime_type

    @runtime_type.setter
    def runtime_type(self, runtime_type):
        """
        Sets the runtime_type of this LlmInferenceResponse.
        The runtime of the provided model.


        :param runtime_type: The runtime_type of this LlmInferenceResponse.
        :type: str
        """
        allowed_values = ["COHERE", "LLAMA", "OPENAI", "DALLE3"]
        if not value_allowed_none_or_none_sentinel(runtime_type, allowed_values):
            runtime_type = 'UNKNOWN_ENUM_VALUE'
        self._runtime_type = runtime_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
