# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221208


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CccInfrastructureRoutingStaticDetails(object):
    """
    Static routing information for a rack.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CccInfrastructureRoutingStaticDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param uplink_vlan:
            The value to assign to the uplink_vlan property of this CccInfrastructureRoutingStaticDetails.
        :type uplink_vlan: int

        :param uplink_hsrp_group:
            The value to assign to the uplink_hsrp_group property of this CccInfrastructureRoutingStaticDetails.
        :type uplink_hsrp_group: int

        """
        self.swagger_types = {
            'uplink_vlan': 'int',
            'uplink_hsrp_group': 'int'
        }

        self.attribute_map = {
            'uplink_vlan': 'uplinkVlan',
            'uplink_hsrp_group': 'uplinkHsrpGroup'
        }

        self._uplink_vlan = None
        self._uplink_hsrp_group = None

    @property
    def uplink_vlan(self):
        """
        Gets the uplink_vlan of this CccInfrastructureRoutingStaticDetails.
        The virtual local area network (VLAN) identifier used to connect to the uplink
        (only access mode is supported).


        :return: The uplink_vlan of this CccInfrastructureRoutingStaticDetails.
        :rtype: int
        """
        return self._uplink_vlan

    @uplink_vlan.setter
    def uplink_vlan(self, uplink_vlan):
        """
        Sets the uplink_vlan of this CccInfrastructureRoutingStaticDetails.
        The virtual local area network (VLAN) identifier used to connect to the uplink
        (only access mode is supported).


        :param uplink_vlan: The uplink_vlan of this CccInfrastructureRoutingStaticDetails.
        :type: int
        """
        self._uplink_vlan = uplink_vlan

    @property
    def uplink_hsrp_group(self):
        """
        Gets the uplink_hsrp_group of this CccInfrastructureRoutingStaticDetails.
        The uplink Hot Standby Router Protocol (HSRP) group value for the switch in the
        Compute Cloud@Customer infrastructure.


        :return: The uplink_hsrp_group of this CccInfrastructureRoutingStaticDetails.
        :rtype: int
        """
        return self._uplink_hsrp_group

    @uplink_hsrp_group.setter
    def uplink_hsrp_group(self, uplink_hsrp_group):
        """
        Sets the uplink_hsrp_group of this CccInfrastructureRoutingStaticDetails.
        The uplink Hot Standby Router Protocol (HSRP) group value for the switch in the
        Compute Cloud@Customer infrastructure.


        :param uplink_hsrp_group: The uplink_hsrp_group of this CccInfrastructureRoutingStaticDetails.
        :type: int
        """
        self._uplink_hsrp_group = uplink_hsrp_group

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other