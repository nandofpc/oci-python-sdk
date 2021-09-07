# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .access_request import AccessRequest
from .access_request_collection import AccessRequestCollection
from .access_request_history_collection import AccessRequestHistoryCollection
from .access_request_history_summary import AccessRequestHistorySummary
from .access_request_summary import AccessRequestSummary
from .approve_access_request_details import ApproveAccessRequestDetails
from .change_operator_control_assignment_compartment_details import ChangeOperatorControlAssignmentCompartmentDetails
from .change_operator_control_compartment_details import ChangeOperatorControlCompartmentDetails
from .create_operator_control_assignment_details import CreateOperatorControlAssignmentDetails
from .create_operator_control_details import CreateOperatorControlDetails
from .operator_action import OperatorAction
from .operator_action_collection import OperatorActionCollection
from .operator_action_properties import OperatorActionProperties
from .operator_action_summary import OperatorActionSummary
from .operator_control import OperatorControl
from .operator_control_assignment import OperatorControlAssignment
from .operator_control_assignment_collection import OperatorControlAssignmentCollection
from .operator_control_assignment_summary import OperatorControlAssignmentSummary
from .operator_control_collection import OperatorControlCollection
from .operator_control_summary import OperatorControlSummary
from .reject_access_request_details import RejectAccessRequestDetails
from .revoke_access_request_details import RevokeAccessRequestDetails
from .update_operator_control_assignment_details import UpdateOperatorControlAssignmentDetails
from .update_operator_control_details import UpdateOperatorControlDetails

# Maps type names to classes for operator_access_control services.
operator_access_control_type_mapping = {
    "AccessRequest": AccessRequest,
    "AccessRequestCollection": AccessRequestCollection,
    "AccessRequestHistoryCollection": AccessRequestHistoryCollection,
    "AccessRequestHistorySummary": AccessRequestHistorySummary,
    "AccessRequestSummary": AccessRequestSummary,
    "ApproveAccessRequestDetails": ApproveAccessRequestDetails,
    "ChangeOperatorControlAssignmentCompartmentDetails": ChangeOperatorControlAssignmentCompartmentDetails,
    "ChangeOperatorControlCompartmentDetails": ChangeOperatorControlCompartmentDetails,
    "CreateOperatorControlAssignmentDetails": CreateOperatorControlAssignmentDetails,
    "CreateOperatorControlDetails": CreateOperatorControlDetails,
    "OperatorAction": OperatorAction,
    "OperatorActionCollection": OperatorActionCollection,
    "OperatorActionProperties": OperatorActionProperties,
    "OperatorActionSummary": OperatorActionSummary,
    "OperatorControl": OperatorControl,
    "OperatorControlAssignment": OperatorControlAssignment,
    "OperatorControlAssignmentCollection": OperatorControlAssignmentCollection,
    "OperatorControlAssignmentSummary": OperatorControlAssignmentSummary,
    "OperatorControlCollection": OperatorControlCollection,
    "OperatorControlSummary": OperatorControlSummary,
    "RejectAccessRequestDetails": RejectAccessRequestDetails,
    "RevokeAccessRequestDetails": RevokeAccessRequestDetails,
    "UpdateOperatorControlAssignmentDetails": UpdateOperatorControlAssignmentDetails,
    "UpdateOperatorControlDetails": UpdateOperatorControlDetails
}