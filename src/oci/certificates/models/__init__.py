# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .ca_bundle import CaBundle
from .certificate_authority_bundle import CertificateAuthorityBundle
from .certificate_authority_bundle_version_collection import CertificateAuthorityBundleVersionCollection
from .certificate_authority_bundle_version_summary import CertificateAuthorityBundleVersionSummary
from .certificate_bundle import CertificateBundle
from .certificate_bundle_public_only import CertificateBundlePublicOnly
from .certificate_bundle_version_collection import CertificateBundleVersionCollection
from .certificate_bundle_version_summary import CertificateBundleVersionSummary
from .certificate_bundle_with_private_key import CertificateBundleWithPrivateKey
from .revocation_status import RevocationStatus
from .validity import Validity

# Maps type names to classes for certificates services.
certificates_type_mapping = {
    "CaBundle": CaBundle,
    "CertificateAuthorityBundle": CertificateAuthorityBundle,
    "CertificateAuthorityBundleVersionCollection": CertificateAuthorityBundleVersionCollection,
    "CertificateAuthorityBundleVersionSummary": CertificateAuthorityBundleVersionSummary,
    "CertificateBundle": CertificateBundle,
    "CertificateBundlePublicOnly": CertificateBundlePublicOnly,
    "CertificateBundleVersionCollection": CertificateBundleVersionCollection,
    "CertificateBundleVersionSummary": CertificateBundleVersionSummary,
    "CertificateBundleWithPrivateKey": CertificateBundleWithPrivateKey,
    "RevocationStatus": RevocationStatus,
    "Validity": Validity
}