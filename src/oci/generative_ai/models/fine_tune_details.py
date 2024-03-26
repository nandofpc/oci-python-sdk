# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20231130


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FineTuneDetails(object):
    """
    Details about fine-tuning a custom model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FineTuneDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param training_dataset:
            The value to assign to the training_dataset property of this FineTuneDetails.
        :type training_dataset: oci.generative_ai.models.Dataset

        :param dedicated_ai_cluster_id:
            The value to assign to the dedicated_ai_cluster_id property of this FineTuneDetails.
        :type dedicated_ai_cluster_id: str

        :param training_config:
            The value to assign to the training_config property of this FineTuneDetails.
        :type training_config: oci.generative_ai.models.TrainingConfig

        """
        self.swagger_types = {
            'training_dataset': 'Dataset',
            'dedicated_ai_cluster_id': 'str',
            'training_config': 'TrainingConfig'
        }

        self.attribute_map = {
            'training_dataset': 'trainingDataset',
            'dedicated_ai_cluster_id': 'dedicatedAiClusterId',
            'training_config': 'trainingConfig'
        }

        self._training_dataset = None
        self._dedicated_ai_cluster_id = None
        self._training_config = None

    @property
    def training_dataset(self):
        """
        **[Required]** Gets the training_dataset of this FineTuneDetails.

        :return: The training_dataset of this FineTuneDetails.
        :rtype: oci.generative_ai.models.Dataset
        """
        return self._training_dataset

    @training_dataset.setter
    def training_dataset(self, training_dataset):
        """
        Sets the training_dataset of this FineTuneDetails.

        :param training_dataset: The training_dataset of this FineTuneDetails.
        :type: oci.generative_ai.models.Dataset
        """
        self._training_dataset = training_dataset

    @property
    def dedicated_ai_cluster_id(self):
        """
        **[Required]** Gets the dedicated_ai_cluster_id of this FineTuneDetails.
        The OCID of the dedicated AI cluster this fine-tuning runs on.


        :return: The dedicated_ai_cluster_id of this FineTuneDetails.
        :rtype: str
        """
        return self._dedicated_ai_cluster_id

    @dedicated_ai_cluster_id.setter
    def dedicated_ai_cluster_id(self, dedicated_ai_cluster_id):
        """
        Sets the dedicated_ai_cluster_id of this FineTuneDetails.
        The OCID of the dedicated AI cluster this fine-tuning runs on.


        :param dedicated_ai_cluster_id: The dedicated_ai_cluster_id of this FineTuneDetails.
        :type: str
        """
        self._dedicated_ai_cluster_id = dedicated_ai_cluster_id

    @property
    def training_config(self):
        """
        Gets the training_config of this FineTuneDetails.

        :return: The training_config of this FineTuneDetails.
        :rtype: oci.generative_ai.models.TrainingConfig
        """
        return self._training_config

    @training_config.setter
    def training_config(self, training_config):
        """
        Sets the training_config of this FineTuneDetails.

        :param training_config: The training_config of this FineTuneDetails.
        :type: oci.generative_ai.models.TrainingConfig
        """
        self._training_config = training_config

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other