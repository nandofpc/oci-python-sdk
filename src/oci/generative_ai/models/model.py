# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Model(object):
    """
    You can create a custom model by using your dataset to fine-tune an out-of-the-box text generation base model. Have your dataset ready before you create a custom model. See `Training Data Requirements`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an administrator who gives OCI resource access to users. See
    `Getting Started with Policies`__ and `Getting Access to Generative AI Resouces`__.

    __ https://docs.cloud.oracle.com/iaas/Content/generative-ai/training-data-requirements.htm
    __ https://docs.cloud.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm
    __ https://docs.cloud.oracle.com/iaas/Content/generative-ai/iam-policies.htm
    """

    #: A constant which can be used with the capabilities property of a Model.
    #: This constant has a value of "TEXT_GENERATION"
    CAPABILITIES_TEXT_GENERATION = "TEXT_GENERATION"

    #: A constant which can be used with the capabilities property of a Model.
    #: This constant has a value of "TEXT_SUMMARIZATION"
    CAPABILITIES_TEXT_SUMMARIZATION = "TEXT_SUMMARIZATION"

    #: A constant which can be used with the capabilities property of a Model.
    #: This constant has a value of "TEXT_EMBEDDINGS"
    CAPABILITIES_TEXT_EMBEDDINGS = "TEXT_EMBEDDINGS"

    #: A constant which can be used with the capabilities property of a Model.
    #: This constant has a value of "FINE_TUNE"
    CAPABILITIES_FINE_TUNE = "FINE_TUNE"

    #: A constant which can be used with the capabilities property of a Model.
    #: This constant has a value of "CHAT"
    CAPABILITIES_CHAT = "CHAT"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Model.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the type property of a Model.
    #: This constant has a value of "BASE"
    TYPE_BASE = "BASE"

    #: A constant which can be used with the type property of a Model.
    #: This constant has a value of "CUSTOM"
    TYPE_CUSTOM = "CUSTOM"

    def __init__(self, **kwargs):
        """
        Initializes a new Model object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Model.
        :type id: str

        :param description:
            The value to assign to the description property of this Model.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Model.
        :type compartment_id: str

        :param capabilities:
            The value to assign to the capabilities property of this Model.
            Allowed values for items in this list are: "TEXT_GENERATION", "TEXT_SUMMARIZATION", "TEXT_EMBEDDINGS", "FINE_TUNE", "CHAT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type capabilities: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Model.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Model.
        :type lifecycle_details: str

        :param vendor:
            The value to assign to the vendor property of this Model.
        :type vendor: str

        :param version:
            The value to assign to the version property of this Model.
        :type version: str

        :param display_name:
            The value to assign to the display_name property of this Model.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this Model.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Model.
        :type time_updated: datetime

        :param base_model_id:
            The value to assign to the base_model_id property of this Model.
        :type base_model_id: str

        :param type:
            The value to assign to the type property of this Model.
            Allowed values for this property are: "BASE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param fine_tune_details:
            The value to assign to the fine_tune_details property of this Model.
        :type fine_tune_details: oci.generative_ai.models.FineTuneDetails

        :param model_metrics:
            The value to assign to the model_metrics property of this Model.
        :type model_metrics: oci.generative_ai.models.ModelMetrics

        :param is_long_term_supported:
            The value to assign to the is_long_term_supported property of this Model.
        :type is_long_term_supported: bool

        :param time_deprecated:
            The value to assign to the time_deprecated property of this Model.
        :type time_deprecated: datetime

        :param previous_state:
            The value to assign to the previous_state property of this Model.
        :type previous_state: oci.generative_ai.models.Model

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Model.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Model.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Model.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'capabilities': 'list[str]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'vendor': 'str',
            'version': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'base_model_id': 'str',
            'type': 'str',
            'fine_tune_details': 'FineTuneDetails',
            'model_metrics': 'ModelMetrics',
            'is_long_term_supported': 'bool',
            'time_deprecated': 'datetime',
            'previous_state': 'Model',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'capabilities': 'capabilities',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'vendor': 'vendor',
            'version': 'version',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'base_model_id': 'baseModelId',
            'type': 'type',
            'fine_tune_details': 'fineTuneDetails',
            'model_metrics': 'modelMetrics',
            'is_long_term_supported': 'isLongTermSupported',
            'time_deprecated': 'timeDeprecated',
            'previous_state': 'previousState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._description = None
        self._compartment_id = None
        self._capabilities = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._vendor = None
        self._version = None
        self._display_name = None
        self._time_created = None
        self._time_updated = None
        self._base_model_id = None
        self._type = None
        self._fine_tune_details = None
        self._model_metrics = None
        self._is_long_term_supported = None
        self._time_deprecated = None
        self._previous_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Model.
        An ID that uniquely identifies a pretrained or fine-tuned model.


        :return: The id of this Model.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Model.
        An ID that uniquely identifies a pretrained or fine-tuned model.


        :param id: The id of this Model.
        :type: str
        """
        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Model.
        An optional description of the model.


        :return: The description of this Model.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Model.
        An optional description of the model.


        :param description: The description of this Model.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Model.
        The compartment OCID for fine-tuned models. For pretrained models, this value is null.


        :return: The compartment_id of this Model.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Model.
        The compartment OCID for fine-tuned models. For pretrained models, this value is null.


        :param compartment_id: The compartment_id of this Model.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def capabilities(self):
        """
        **[Required]** Gets the capabilities of this Model.
        Describes what this model can be used for.

        Allowed values for items in this list are: "TEXT_GENERATION", "TEXT_SUMMARIZATION", "TEXT_EMBEDDINGS", "FINE_TUNE", "CHAT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The capabilities of this Model.
        :rtype: list[str]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """
        Sets the capabilities of this Model.
        Describes what this model can be used for.


        :param capabilities: The capabilities of this Model.
        :type: list[str]
        """
        allowed_values = ["TEXT_GENERATION", "TEXT_SUMMARIZATION", "TEXT_EMBEDDINGS", "FINE_TUNE", "CHAT"]
        if capabilities:
            capabilities[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in capabilities]
        self._capabilities = capabilities

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Model.
        The lifecycle state of the model.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Model.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Model.
        The lifecycle state of the model.


        :param lifecycle_state: The lifecycle_state of this Model.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Model.
        A message describing the current state of the model in more detail that can provide actionable information.


        :return: The lifecycle_details of this Model.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Model.
        A message describing the current state of the model in more detail that can provide actionable information.


        :param lifecycle_details: The lifecycle_details of this Model.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def vendor(self):
        """
        Gets the vendor of this Model.
        The provider of the base model.


        :return: The vendor of this Model.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this Model.
        The provider of the base model.


        :param vendor: The vendor of this Model.
        :type: str
        """
        self._vendor = vendor

    @property
    def version(self):
        """
        Gets the version of this Model.
        The version of the model.


        :return: The version of this Model.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Model.
        The version of the model.


        :param version: The version of this Model.
        :type: str
        """
        self._version = version

    @property
    def display_name(self):
        """
        Gets the display_name of this Model.
        A user-friendly name.


        :return: The display_name of this Model.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Model.
        A user-friendly name.


        :param display_name: The display_name of this Model.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Model.
        The date and time that the model was created in the format of an RFC3339 datetime string.


        :return: The time_created of this Model.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Model.
        The date and time that the model was created in the format of an RFC3339 datetime string.


        :param time_created: The time_created of this Model.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Model.
        The date and time that the model was updated in the format of an RFC3339 datetime string.


        :return: The time_updated of this Model.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Model.
        The date and time that the model was updated in the format of an RFC3339 datetime string.


        :param time_updated: The time_updated of this Model.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def base_model_id(self):
        """
        Gets the base_model_id of this Model.
        The OCID of the base model that's used for fine-tuning. For pretrained models, the value is null.


        :return: The base_model_id of this Model.
        :rtype: str
        """
        return self._base_model_id

    @base_model_id.setter
    def base_model_id(self, base_model_id):
        """
        Sets the base_model_id of this Model.
        The OCID of the base model that's used for fine-tuning. For pretrained models, the value is null.


        :param base_model_id: The base_model_id of this Model.
        :type: str
        """
        self._base_model_id = base_model_id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this Model.
        The model type indicating whether this is a pretrained/base model or a custom/fine-tuned model.

        Allowed values for this property are: "BASE", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this Model.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Model.
        The model type indicating whether this is a pretrained/base model or a custom/fine-tuned model.


        :param type: The type of this Model.
        :type: str
        """
        allowed_values = ["BASE", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def fine_tune_details(self):
        """
        Gets the fine_tune_details of this Model.

        :return: The fine_tune_details of this Model.
        :rtype: oci.generative_ai.models.FineTuneDetails
        """
        return self._fine_tune_details

    @fine_tune_details.setter
    def fine_tune_details(self, fine_tune_details):
        """
        Sets the fine_tune_details of this Model.

        :param fine_tune_details: The fine_tune_details of this Model.
        :type: oci.generative_ai.models.FineTuneDetails
        """
        self._fine_tune_details = fine_tune_details

    @property
    def model_metrics(self):
        """
        Gets the model_metrics of this Model.

        :return: The model_metrics of this Model.
        :rtype: oci.generative_ai.models.ModelMetrics
        """
        return self._model_metrics

    @model_metrics.setter
    def model_metrics(self, model_metrics):
        """
        Sets the model_metrics of this Model.

        :param model_metrics: The model_metrics of this Model.
        :type: oci.generative_ai.models.ModelMetrics
        """
        self._model_metrics = model_metrics

    @property
    def is_long_term_supported(self):
        """
        Gets the is_long_term_supported of this Model.
        Whether a model is supported long-term. Only applicable to base models.


        :return: The is_long_term_supported of this Model.
        :rtype: bool
        """
        return self._is_long_term_supported

    @is_long_term_supported.setter
    def is_long_term_supported(self, is_long_term_supported):
        """
        Sets the is_long_term_supported of this Model.
        Whether a model is supported long-term. Only applicable to base models.


        :param is_long_term_supported: The is_long_term_supported of this Model.
        :type: bool
        """
        self._is_long_term_supported = is_long_term_supported

    @property
    def time_deprecated(self):
        """
        Gets the time_deprecated of this Model.
        Corresponds to the time when the custom model and its associated foundation model will be deprecated.


        :return: The time_deprecated of this Model.
        :rtype: datetime
        """
        return self._time_deprecated

    @time_deprecated.setter
    def time_deprecated(self, time_deprecated):
        """
        Sets the time_deprecated of this Model.
        Corresponds to the time when the custom model and its associated foundation model will be deprecated.


        :param time_deprecated: The time_deprecated of this Model.
        :type: datetime
        """
        self._time_deprecated = time_deprecated

    @property
    def previous_state(self):
        """
        Gets the previous_state of this Model.

        :return: The previous_state of this Model.
        :rtype: oci.generative_ai.models.Model
        """
        return self._previous_state

    @previous_state.setter
    def previous_state(self, previous_state):
        """
        Sets the previous_state of this Model.

        :param previous_state: The previous_state of this Model.
        :type: oci.generative_ai.models.Model
        """
        self._previous_state = previous_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Model.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Model.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Model.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Model.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Model.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Model.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Model.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Model.
        System tags for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Model.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
