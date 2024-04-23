# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220926


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SubmitEmailDetails(object):
    """
    Details that are required by the sender to submit a request to send email.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SubmitEmailDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param message_id:
            The value to assign to the message_id property of this SubmitEmailDetails.
        :type message_id: str

        :param sender:
            The value to assign to the sender property of this SubmitEmailDetails.
        :type sender: oci.email_data_plane.models.Sender

        :param recipients:
            The value to assign to the recipients property of this SubmitEmailDetails.
        :type recipients: oci.email_data_plane.models.Recipients

        :param subject:
            The value to assign to the subject property of this SubmitEmailDetails.
        :type subject: str

        :param body_html:
            The value to assign to the body_html property of this SubmitEmailDetails.
        :type body_html: str

        :param body_text:
            The value to assign to the body_text property of this SubmitEmailDetails.
        :type body_text: str

        :param reply_to:
            The value to assign to the reply_to property of this SubmitEmailDetails.
        :type reply_to: list[oci.email_data_plane.models.EmailAddress]

        :param header_fields:
            The value to assign to the header_fields property of this SubmitEmailDetails.
        :type header_fields: dict(str, str)

        """
        self.swagger_types = {
            'message_id': 'str',
            'sender': 'Sender',
            'recipients': 'Recipients',
            'subject': 'str',
            'body_html': 'str',
            'body_text': 'str',
            'reply_to': 'list[EmailAddress]',
            'header_fields': 'dict(str, str)'
        }

        self.attribute_map = {
            'message_id': 'messageId',
            'sender': 'sender',
            'recipients': 'recipients',
            'subject': 'subject',
            'body_html': 'bodyHtml',
            'body_text': 'bodyText',
            'reply_to': 'replyTo',
            'header_fields': 'headerFields'
        }

        self._message_id = None
        self._sender = None
        self._recipients = None
        self._subject = None
        self._body_html = None
        self._body_text = None
        self._reply_to = None
        self._header_fields = None

    @property
    def message_id(self):
        """
        Gets the message_id of this SubmitEmailDetails.
        The unique ID for the email's Message-ID header used for service log correlation. The submission will return an error if the syntax is not a valid `RFC 5322`__ Message-ID. This will be generated if not provided.
        Example: sdiofu234qwermls24fd@mail.example.com

        __ https://www.rfc-editor.org/rfc/rfc5322


        :return: The message_id of this SubmitEmailDetails.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """
        Sets the message_id of this SubmitEmailDetails.
        The unique ID for the email's Message-ID header used for service log correlation. The submission will return an error if the syntax is not a valid `RFC 5322`__ Message-ID. This will be generated if not provided.
        Example: sdiofu234qwermls24fd@mail.example.com

        __ https://www.rfc-editor.org/rfc/rfc5322


        :param message_id: The message_id of this SubmitEmailDetails.
        :type: str
        """
        self._message_id = message_id

    @property
    def sender(self):
        """
        **[Required]** Gets the sender of this SubmitEmailDetails.

        :return: The sender of this SubmitEmailDetails.
        :rtype: oci.email_data_plane.models.Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """
        Sets the sender of this SubmitEmailDetails.

        :param sender: The sender of this SubmitEmailDetails.
        :type: oci.email_data_plane.models.Sender
        """
        self._sender = sender

    @property
    def recipients(self):
        """
        **[Required]** Gets the recipients of this SubmitEmailDetails.

        :return: The recipients of this SubmitEmailDetails.
        :rtype: oci.email_data_plane.models.Recipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """
        Sets the recipients of this SubmitEmailDetails.

        :param recipients: The recipients of this SubmitEmailDetails.
        :type: oci.email_data_plane.models.Recipients
        """
        self._recipients = recipients

    @property
    def subject(self):
        """
        **[Required]** Gets the subject of this SubmitEmailDetails.
        A short summary of the content, which will appear in the recipient's inbox. UTF-8 supported `RFC 2047`__.

        __ https://www.rfc-editor.org/rfc/rfc2047


        :return: The subject of this SubmitEmailDetails.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this SubmitEmailDetails.
        A short summary of the content, which will appear in the recipient's inbox. UTF-8 supported `RFC 2047`__.

        __ https://www.rfc-editor.org/rfc/rfc2047


        :param subject: The subject of this SubmitEmailDetails.
        :type: str
        """
        self._subject = subject

    @property
    def body_html(self):
        """
        Gets the body_html of this SubmitEmailDetails.
        HTML body content in UTF-8.
        NOTE: Even though bodytext and bodyhtml are both optional, at least one of them must be provided.


        :return: The body_html of this SubmitEmailDetails.
        :rtype: str
        """
        return self._body_html

    @body_html.setter
    def body_html(self, body_html):
        """
        Sets the body_html of this SubmitEmailDetails.
        HTML body content in UTF-8.
        NOTE: Even though bodytext and bodyhtml are both optional, at least one of them must be provided.


        :param body_html: The body_html of this SubmitEmailDetails.
        :type: str
        """
        self._body_html = body_html

    @property
    def body_text(self):
        """
        Gets the body_text of this SubmitEmailDetails.
        Text body content.
        NOTE: Even though bodytext and bodyhtml are both optional, at least one of them must be provided.


        :return: The body_text of this SubmitEmailDetails.
        :rtype: str
        """
        return self._body_text

    @body_text.setter
    def body_text(self, body_text):
        """
        Sets the body_text of this SubmitEmailDetails.
        Text body content.
        NOTE: Even though bodytext and bodyhtml are both optional, at least one of them must be provided.


        :param body_text: The body_text of this SubmitEmailDetails.
        :type: str
        """
        self._body_text = body_text

    @property
    def reply_to(self):
        """
        Gets the reply_to of this SubmitEmailDetails.
        The email address for the recipient to reply to. If left blank, defaults to the sender address.


        :return: The reply_to of this SubmitEmailDetails.
        :rtype: list[oci.email_data_plane.models.EmailAddress]
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """
        Sets the reply_to of this SubmitEmailDetails.
        The email address for the recipient to reply to. If left blank, defaults to the sender address.


        :param reply_to: The reply_to of this SubmitEmailDetails.
        :type: list[oci.email_data_plane.models.EmailAddress]
        """
        self._reply_to = reply_to

    @property
    def header_fields(self):
        """
        Gets the header_fields of this SubmitEmailDetails.
        The header used by the customer for the email sent. Reserved headers are not allowed e.g \"subject\", \"from\", and \"to\" etc.
        Example: `{\"bar-key\": \"value\"}`


        :return: The header_fields of this SubmitEmailDetails.
        :rtype: dict(str, str)
        """
        return self._header_fields

    @header_fields.setter
    def header_fields(self, header_fields):
        """
        Sets the header_fields of this SubmitEmailDetails.
        The header used by the customer for the email sent. Reserved headers are not allowed e.g \"subject\", \"from\", and \"to\" etc.
        Example: `{\"bar-key\": \"value\"}`


        :param header_fields: The header_fields of this SubmitEmailDetails.
        :type: dict(str, str)
        """
        self._header_fields = header_fields

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other