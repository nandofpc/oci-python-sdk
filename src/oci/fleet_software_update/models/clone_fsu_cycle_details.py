# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220528


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CloneFsuCycleDetails(object):
    """
    Details for cloning an existing Exadata Fleet Update Cycle resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CloneFsuCycleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CloneFsuCycleDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CloneFsuCycleDetails.
        :type compartment_id: str

        :param fsu_collection_id:
            The value to assign to the fsu_collection_id property of this CloneFsuCycleDetails.
        :type fsu_collection_id: str

        :param goal_version_details:
            The value to assign to the goal_version_details property of this CloneFsuCycleDetails.
        :type goal_version_details: oci.fleet_software_update.models.FsuGoalVersionDetails

        :param batching_strategy:
            The value to assign to the batching_strategy property of this CloneFsuCycleDetails.
        :type batching_strategy: oci.fleet_software_update.models.CreateBatchingStrategyDetails

        :param stage_action_schedule:
            The value to assign to the stage_action_schedule property of this CloneFsuCycleDetails.
        :type stage_action_schedule: oci.fleet_software_update.models.CreateScheduleDetails

        :param apply_action_schedule:
            The value to assign to the apply_action_schedule property of this CloneFsuCycleDetails.
        :type apply_action_schedule: oci.fleet_software_update.models.CreateScheduleDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'fsu_collection_id': 'str',
            'goal_version_details': 'FsuGoalVersionDetails',
            'batching_strategy': 'CreateBatchingStrategyDetails',
            'stage_action_schedule': 'CreateScheduleDetails',
            'apply_action_schedule': 'CreateScheduleDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'fsu_collection_id': 'fsuCollectionId',
            'goal_version_details': 'goalVersionDetails',
            'batching_strategy': 'batchingStrategy',
            'stage_action_schedule': 'stageActionSchedule',
            'apply_action_schedule': 'applyActionSchedule'
        }

        self._display_name = None
        self._compartment_id = None
        self._fsu_collection_id = None
        self._goal_version_details = None
        self._batching_strategy = None
        self._stage_action_schedule = None
        self._apply_action_schedule = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CloneFsuCycleDetails.
        Exadata Fleet Update Cycle display name.


        :return: The display_name of this CloneFsuCycleDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CloneFsuCycleDetails.
        Exadata Fleet Update Cycle display name.


        :param display_name: The display_name of this CloneFsuCycleDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CloneFsuCycleDetails.
        Compartment Identifier.


        :return: The compartment_id of this CloneFsuCycleDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CloneFsuCycleDetails.
        Compartment Identifier.


        :param compartment_id: The compartment_id of this CloneFsuCycleDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def fsu_collection_id(self):
        """
        Gets the fsu_collection_id of this CloneFsuCycleDetails.
        OCID identifier for the Collection ID the Exadata Fleet Update Cycle will be assigned to.
        If not specified, it will be assigned to the same Collection as the source Exadata Fleet Update Cycle.


        :return: The fsu_collection_id of this CloneFsuCycleDetails.
        :rtype: str
        """
        return self._fsu_collection_id

    @fsu_collection_id.setter
    def fsu_collection_id(self, fsu_collection_id):
        """
        Sets the fsu_collection_id of this CloneFsuCycleDetails.
        OCID identifier for the Collection ID the Exadata Fleet Update Cycle will be assigned to.
        If not specified, it will be assigned to the same Collection as the source Exadata Fleet Update Cycle.


        :param fsu_collection_id: The fsu_collection_id of this CloneFsuCycleDetails.
        :type: str
        """
        self._fsu_collection_id = fsu_collection_id

    @property
    def goal_version_details(self):
        """
        **[Required]** Gets the goal_version_details of this CloneFsuCycleDetails.

        :return: The goal_version_details of this CloneFsuCycleDetails.
        :rtype: oci.fleet_software_update.models.FsuGoalVersionDetails
        """
        return self._goal_version_details

    @goal_version_details.setter
    def goal_version_details(self, goal_version_details):
        """
        Sets the goal_version_details of this CloneFsuCycleDetails.

        :param goal_version_details: The goal_version_details of this CloneFsuCycleDetails.
        :type: oci.fleet_software_update.models.FsuGoalVersionDetails
        """
        self._goal_version_details = goal_version_details

    @property
    def batching_strategy(self):
        """
        Gets the batching_strategy of this CloneFsuCycleDetails.

        :return: The batching_strategy of this CloneFsuCycleDetails.
        :rtype: oci.fleet_software_update.models.CreateBatchingStrategyDetails
        """
        return self._batching_strategy

    @batching_strategy.setter
    def batching_strategy(self, batching_strategy):
        """
        Sets the batching_strategy of this CloneFsuCycleDetails.

        :param batching_strategy: The batching_strategy of this CloneFsuCycleDetails.
        :type: oci.fleet_software_update.models.CreateBatchingStrategyDetails
        """
        self._batching_strategy = batching_strategy

    @property
    def stage_action_schedule(self):
        """
        Gets the stage_action_schedule of this CloneFsuCycleDetails.

        :return: The stage_action_schedule of this CloneFsuCycleDetails.
        :rtype: oci.fleet_software_update.models.CreateScheduleDetails
        """
        return self._stage_action_schedule

    @stage_action_schedule.setter
    def stage_action_schedule(self, stage_action_schedule):
        """
        Sets the stage_action_schedule of this CloneFsuCycleDetails.

        :param stage_action_schedule: The stage_action_schedule of this CloneFsuCycleDetails.
        :type: oci.fleet_software_update.models.CreateScheduleDetails
        """
        self._stage_action_schedule = stage_action_schedule

    @property
    def apply_action_schedule(self):
        """
        Gets the apply_action_schedule of this CloneFsuCycleDetails.

        :return: The apply_action_schedule of this CloneFsuCycleDetails.
        :rtype: oci.fleet_software_update.models.CreateScheduleDetails
        """
        return self._apply_action_schedule

    @apply_action_schedule.setter
    def apply_action_schedule(self, apply_action_schedule):
        """
        Sets the apply_action_schedule of this CloneFsuCycleDetails.

        :param apply_action_schedule: The apply_action_schedule of this CloneFsuCycleDetails.
        :type: oci.fleet_software_update.models.CreateScheduleDetails
        """
        self._apply_action_schedule = apply_action_schedule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other