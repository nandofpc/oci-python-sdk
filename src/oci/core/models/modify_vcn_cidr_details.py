# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ModifyVcnCidrDetails(object):
    """
    Details for updating a CIDR block.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ModifyVcnCidrDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param original_cidr_block:
            The value to assign to the original_cidr_block property of this ModifyVcnCidrDetails.
        :type original_cidr_block: str

        :param new_cidr_block:
            The value to assign to the new_cidr_block property of this ModifyVcnCidrDetails.
        :type new_cidr_block: str

        """
        self.swagger_types = {
            'original_cidr_block': 'str',
            'new_cidr_block': 'str'
        }

        self.attribute_map = {
            'original_cidr_block': 'originalCidrBlock',
            'new_cidr_block': 'newCidrBlock'
        }

        self._original_cidr_block = None
        self._new_cidr_block = None

    @property
    def original_cidr_block(self):
        """
        **[Required]** Gets the original_cidr_block of this ModifyVcnCidrDetails.
        The CIDR IP address to update.


        :return: The original_cidr_block of this ModifyVcnCidrDetails.
        :rtype: str
        """
        return self._original_cidr_block

    @original_cidr_block.setter
    def original_cidr_block(self, original_cidr_block):
        """
        Sets the original_cidr_block of this ModifyVcnCidrDetails.
        The CIDR IP address to update.


        :param original_cidr_block: The original_cidr_block of this ModifyVcnCidrDetails.
        :type: str
        """
        self._original_cidr_block = original_cidr_block

    @property
    def new_cidr_block(self):
        """
        **[Required]** Gets the new_cidr_block of this ModifyVcnCidrDetails.
        The new CIDR IP address.


        :return: The new_cidr_block of this ModifyVcnCidrDetails.
        :rtype: str
        """
        return self._new_cidr_block

    @new_cidr_block.setter
    def new_cidr_block(self, new_cidr_block):
        """
        Sets the new_cidr_block of this ModifyVcnCidrDetails.
        The new CIDR IP address.


        :param new_cidr_block: The new_cidr_block of this ModifyVcnCidrDetails.
        :type: str
        """
        self._new_cidr_block = new_cidr_block

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
