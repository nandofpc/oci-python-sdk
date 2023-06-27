# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LeafCertificateDetails(object):
    """
    The details of leaf certificate
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LeafCertificateDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param certificate_id:
            The value to assign to the certificate_id property of this LeafCertificateDetails.
        :type certificate_id: str

        :param certificate_pem:
            The value to assign to the certificate_pem property of this LeafCertificateDetails.
        :type certificate_pem: str

        """
        self.swagger_types = {
            'certificate_id': 'str',
            'certificate_pem': 'str'
        }

        self.attribute_map = {
            'certificate_id': 'certificateId',
            'certificate_pem': 'certificatePem'
        }

        self._certificate_id = None
        self._certificate_pem = None

    @property
    def certificate_id(self):
        """
        Gets the certificate_id of this LeafCertificateDetails.
        The id of the certificate


        :return: The certificate_id of this LeafCertificateDetails.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """
        Sets the certificate_id of this LeafCertificateDetails.
        The id of the certificate


        :param certificate_id: The certificate_id of this LeafCertificateDetails.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def certificate_pem(self):
        """
        Gets the certificate_pem of this LeafCertificateDetails.
        The certificate content in PEM format


        :return: The certificate_pem of this LeafCertificateDetails.
        :rtype: str
        """
        return self._certificate_pem

    @certificate_pem.setter
    def certificate_pem(self, certificate_pem):
        """
        Sets the certificate_pem of this LeafCertificateDetails.
        The certificate content in PEM format


        :param certificate_pem: The certificate_pem of this LeafCertificateDetails.
        :type: str
        """
        self._certificate_pem = certificate_pem

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other