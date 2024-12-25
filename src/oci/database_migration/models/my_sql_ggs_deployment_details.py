# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MySqlGgsDeploymentDetails(object):
    """
    Optional settings for Oracle GoldenGate processes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MySqlGgsDeploymentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ggs_deployment:
            The value to assign to the ggs_deployment property of this MySqlGgsDeploymentDetails.
        :type ggs_deployment: oci.database_migration.models.GgsDeployment

        :param replicat:
            The value to assign to the replicat property of this MySqlGgsDeploymentDetails.
        :type replicat: oci.database_migration.models.Replicat

        :param acceptable_lag:
            The value to assign to the acceptable_lag property of this MySqlGgsDeploymentDetails.
        :type acceptable_lag: int

        """
        self.swagger_types = {
            'ggs_deployment': 'GgsDeployment',
            'replicat': 'Replicat',
            'acceptable_lag': 'int'
        }

        self.attribute_map = {
            'ggs_deployment': 'ggsDeployment',
            'replicat': 'replicat',
            'acceptable_lag': 'acceptableLag'
        }

        self._ggs_deployment = None
        self._replicat = None
        self._acceptable_lag = None

    @property
    def ggs_deployment(self):
        """
        Gets the ggs_deployment of this MySqlGgsDeploymentDetails.

        :return: The ggs_deployment of this MySqlGgsDeploymentDetails.
        :rtype: oci.database_migration.models.GgsDeployment
        """
        return self._ggs_deployment

    @ggs_deployment.setter
    def ggs_deployment(self, ggs_deployment):
        """
        Sets the ggs_deployment of this MySqlGgsDeploymentDetails.

        :param ggs_deployment: The ggs_deployment of this MySqlGgsDeploymentDetails.
        :type: oci.database_migration.models.GgsDeployment
        """
        self._ggs_deployment = ggs_deployment

    @property
    def replicat(self):
        """
        Gets the replicat of this MySqlGgsDeploymentDetails.

        :return: The replicat of this MySqlGgsDeploymentDetails.
        :rtype: oci.database_migration.models.Replicat
        """
        return self._replicat

    @replicat.setter
    def replicat(self, replicat):
        """
        Sets the replicat of this MySqlGgsDeploymentDetails.

        :param replicat: The replicat of this MySqlGgsDeploymentDetails.
        :type: oci.database_migration.models.Replicat
        """
        self._replicat = replicat

    @property
    def acceptable_lag(self):
        """
        Gets the acceptable_lag of this MySqlGgsDeploymentDetails.
        ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.


        :return: The acceptable_lag of this MySqlGgsDeploymentDetails.
        :rtype: int
        """
        return self._acceptable_lag

    @acceptable_lag.setter
    def acceptable_lag(self, acceptable_lag):
        """
        Sets the acceptable_lag of this MySqlGgsDeploymentDetails.
        ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.


        :param acceptable_lag: The acceptable_lag of this MySqlGgsDeploymentDetails.
        :type: int
        """
        self._acceptable_lag = acceptable_lag

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other