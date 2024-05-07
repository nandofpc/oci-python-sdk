# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190531


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstallOsPatchDetails(object):
    """
    Os patch details for installing a os patches to a cluster.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstallOsPatchDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param os_patch_version:
            The value to assign to the os_patch_version property of this InstallOsPatchDetails.
        :type os_patch_version: str

        :param cluster_admin_password:
            The value to assign to the cluster_admin_password property of this InstallOsPatchDetails.
        :type cluster_admin_password: str

        :param patching_configs:
            The value to assign to the patching_configs property of this InstallOsPatchDetails.
        :type patching_configs: oci.bds.models.PatchingConfigs

        """
        self.swagger_types = {
            'os_patch_version': 'str',
            'cluster_admin_password': 'str',
            'patching_configs': 'PatchingConfigs'
        }

        self.attribute_map = {
            'os_patch_version': 'osPatchVersion',
            'cluster_admin_password': 'clusterAdminPassword',
            'patching_configs': 'patchingConfigs'
        }

        self._os_patch_version = None
        self._cluster_admin_password = None
        self._patching_configs = None

    @property
    def os_patch_version(self):
        """
        **[Required]** Gets the os_patch_version of this InstallOsPatchDetails.
        The target os patch version.


        :return: The os_patch_version of this InstallOsPatchDetails.
        :rtype: str
        """
        return self._os_patch_version

    @os_patch_version.setter
    def os_patch_version(self, os_patch_version):
        """
        Sets the os_patch_version of this InstallOsPatchDetails.
        The target os patch version.


        :param os_patch_version: The os_patch_version of this InstallOsPatchDetails.
        :type: str
        """
        self._os_patch_version = os_patch_version

    @property
    def cluster_admin_password(self):
        """
        **[Required]** Gets the cluster_admin_password of this InstallOsPatchDetails.
        Base-64 encoded password for the cluster admin user.


        :return: The cluster_admin_password of this InstallOsPatchDetails.
        :rtype: str
        """
        return self._cluster_admin_password

    @cluster_admin_password.setter
    def cluster_admin_password(self, cluster_admin_password):
        """
        Sets the cluster_admin_password of this InstallOsPatchDetails.
        Base-64 encoded password for the cluster admin user.


        :param cluster_admin_password: The cluster_admin_password of this InstallOsPatchDetails.
        :type: str
        """
        self._cluster_admin_password = cluster_admin_password

    @property
    def patching_configs(self):
        """
        Gets the patching_configs of this InstallOsPatchDetails.

        :return: The patching_configs of this InstallOsPatchDetails.
        :rtype: oci.bds.models.PatchingConfigs
        """
        return self._patching_configs

    @patching_configs.setter
    def patching_configs(self, patching_configs):
        """
        Sets the patching_configs of this InstallOsPatchDetails.

        :param patching_configs: The patching_configs of this InstallOsPatchDetails.
        :type: oci.bds.models.PatchingConfigs
        """
        self._patching_configs = patching_configs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
