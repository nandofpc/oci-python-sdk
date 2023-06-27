# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LoadSqlPlanBaselinesFromCursorCacheDetails(object):
    """
    The details of SQL statements and plans to be loaded from cursor cache. You can specify
    the plans to load using SQL ID, plan identifier, or filterName and filterValue pair.
    You can also control the SQL plan baseline into which the plans are loaded using either
    SQL text or SQL handle.
    """

    #: A constant which can be used with the filter_name property of a LoadSqlPlanBaselinesFromCursorCacheDetails.
    #: This constant has a value of "SQL_TEXT"
    FILTER_NAME_SQL_TEXT = "SQL_TEXT"

    #: A constant which can be used with the filter_name property of a LoadSqlPlanBaselinesFromCursorCacheDetails.
    #: This constant has a value of "PARSING_SCHEMA_NAME"
    FILTER_NAME_PARSING_SCHEMA_NAME = "PARSING_SCHEMA_NAME"

    #: A constant which can be used with the filter_name property of a LoadSqlPlanBaselinesFromCursorCacheDetails.
    #: This constant has a value of "MODULE"
    FILTER_NAME_MODULE = "MODULE"

    #: A constant which can be used with the filter_name property of a LoadSqlPlanBaselinesFromCursorCacheDetails.
    #: This constant has a value of "ACTION"
    FILTER_NAME_ACTION = "ACTION"

    def __init__(self, **kwargs):
        """
        Initializes a new LoadSqlPlanBaselinesFromCursorCacheDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param job_name:
            The value to assign to the job_name property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type job_name: str

        :param job_description:
            The value to assign to the job_description property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type job_description: str

        :param sql_id:
            The value to assign to the sql_id property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type sql_id: str

        :param plan_hash:
            The value to assign to the plan_hash property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type plan_hash: float

        :param sql_text:
            The value to assign to the sql_text property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type sql_text: str

        :param sql_handle:
            The value to assign to the sql_handle property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type sql_handle: str

        :param filter_name:
            The value to assign to the filter_name property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
            Allowed values for this property are: "SQL_TEXT", "PARSING_SCHEMA_NAME", "MODULE", "ACTION"
        :type filter_name: str

        :param filter_value:
            The value to assign to the filter_value property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type filter_value: str

        :param is_fixed:
            The value to assign to the is_fixed property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type is_fixed: bool

        :param is_enabled:
            The value to assign to the is_enabled property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type is_enabled: bool

        :param credentials:
            The value to assign to the credentials property of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type credentials: oci.database_management.models.ManagedDatabaseCredential

        """
        self.swagger_types = {
            'job_name': 'str',
            'job_description': 'str',
            'sql_id': 'str',
            'plan_hash': 'float',
            'sql_text': 'str',
            'sql_handle': 'str',
            'filter_name': 'str',
            'filter_value': 'str',
            'is_fixed': 'bool',
            'is_enabled': 'bool',
            'credentials': 'ManagedDatabaseCredential'
        }

        self.attribute_map = {
            'job_name': 'jobName',
            'job_description': 'jobDescription',
            'sql_id': 'sqlId',
            'plan_hash': 'planHash',
            'sql_text': 'sqlText',
            'sql_handle': 'sqlHandle',
            'filter_name': 'filterName',
            'filter_value': 'filterValue',
            'is_fixed': 'isFixed',
            'is_enabled': 'isEnabled',
            'credentials': 'credentials'
        }

        self._job_name = None
        self._job_description = None
        self._sql_id = None
        self._plan_hash = None
        self._sql_text = None
        self._sql_handle = None
        self._filter_name = None
        self._filter_value = None
        self._is_fixed = None
        self._is_enabled = None
        self._credentials = None

    @property
    def job_name(self):
        """
        **[Required]** Gets the job_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The name of the database job used for loading SQL plan baselines.


        :return: The job_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """
        Sets the job_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The name of the database job used for loading SQL plan baselines.


        :param job_name: The job_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._job_name = job_name

    @property
    def job_description(self):
        """
        Gets the job_description of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The description of the job.


        :return: The job_description of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._job_description

    @job_description.setter
    def job_description(self, job_description):
        """
        Sets the job_description of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The description of the job.


        :param job_description: The job_description of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._job_description = job_description

    @property
    def sql_id(self):
        """
        Gets the sql_id of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL statement identifier. Identifies a SQL statement in the cursor cache.


        :return: The sql_id of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._sql_id

    @sql_id.setter
    def sql_id(self, sql_id):
        """
        Sets the sql_id of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL statement identifier. Identifies a SQL statement in the cursor cache.


        :param sql_id: The sql_id of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._sql_id = sql_id

    @property
    def plan_hash(self):
        """
        Gets the plan_hash of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The plan identifier. By default, all plans present in the cursor cache
        for the SQL statement identified by `sqlId` are captured.


        :return: The plan_hash of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: float
        """
        return self._plan_hash

    @plan_hash.setter
    def plan_hash(self, plan_hash):
        """
        Sets the plan_hash of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The plan identifier. By default, all plans present in the cursor cache
        for the SQL statement identified by `sqlId` are captured.


        :param plan_hash: The plan_hash of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: float
        """
        self._plan_hash = plan_hash

    @property
    def sql_text(self):
        """
        Gets the sql_text of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL text to use in identifying the SQL plan baseline into which the plans
        are loaded. If the SQL plan baseline does not exist, it is created.


        :return: The sql_text of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """
        Sets the sql_text of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL text to use in identifying the SQL plan baseline into which the plans
        are loaded. If the SQL plan baseline does not exist, it is created.


        :param sql_text: The sql_text of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._sql_text = sql_text

    @property
    def sql_handle(self):
        """
        Gets the sql_handle of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL handle to use in identifying the SQL plan baseline into which
        the plans are loaded.


        :return: The sql_handle of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._sql_handle

    @sql_handle.setter
    def sql_handle(self, sql_handle):
        """
        Sets the sql_handle of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The SQL handle to use in identifying the SQL plan baseline into which
        the plans are loaded.


        :param sql_handle: The sql_handle of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._sql_handle = sql_handle

    @property
    def filter_name(self):
        """
        Gets the filter_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The name of the filter.

        - SQL_TEXT: Search pattern to apply to SQL text.
        - PARSING_SCHEMA_NAME: Name of the parsing schema.
        - MODULE: Name of the module.
        - ACTION: Name of the action.

        Allowed values for this property are: "SQL_TEXT", "PARSING_SCHEMA_NAME", "MODULE", "ACTION"


        :return: The filter_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._filter_name

    @filter_name.setter
    def filter_name(self, filter_name):
        """
        Sets the filter_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The name of the filter.

        - SQL_TEXT: Search pattern to apply to SQL text.
        - PARSING_SCHEMA_NAME: Name of the parsing schema.
        - MODULE: Name of the module.
        - ACTION: Name of the action.


        :param filter_name: The filter_name of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        allowed_values = ["SQL_TEXT", "PARSING_SCHEMA_NAME", "MODULE", "ACTION"]
        if not value_allowed_none_or_none_sentinel(filter_name, allowed_values):
            raise ValueError(
                "Invalid value for `filter_name`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._filter_name = filter_name

    @property
    def filter_value(self):
        """
        Gets the filter_value of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The filter value. It is upper-cased except when it is enclosed in
        double quotes or filter name is `SQL_TEXT`.


        :return: The filter_value of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: str
        """
        return self._filter_value

    @filter_value.setter
    def filter_value(self, filter_value):
        """
        Sets the filter_value of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        The filter value. It is upper-cased except when it is enclosed in
        double quotes or filter name is `SQL_TEXT`.


        :param filter_value: The filter_value of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: str
        """
        self._filter_value = filter_value

    @property
    def is_fixed(self):
        """
        Gets the is_fixed of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        Indicates whether the plans are loaded as fixed plans (`true`) or non-fixed plans (`false`).
        By default, they are loaded as non-fixed plans.


        :return: The is_fixed of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: bool
        """
        return self._is_fixed

    @is_fixed.setter
    def is_fixed(self, is_fixed):
        """
        Sets the is_fixed of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        Indicates whether the plans are loaded as fixed plans (`true`) or non-fixed plans (`false`).
        By default, they are loaded as non-fixed plans.


        :param is_fixed: The is_fixed of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: bool
        """
        self._is_fixed = is_fixed

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        Indicates whether the loaded plans are enabled (`true`) or not (`false`).
        By default, they are enabled.


        :return: The is_enabled of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        Indicates whether the loaded plans are enabled (`true`) or not (`false`).
        By default, they are enabled.


        :param is_enabled: The is_enabled of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def credentials(self):
        """
        **[Required]** Gets the credentials of this LoadSqlPlanBaselinesFromCursorCacheDetails.

        :return: The credentials of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :rtype: oci.database_management.models.ManagedDatabaseCredential
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this LoadSqlPlanBaselinesFromCursorCacheDetails.

        :param credentials: The credentials of this LoadSqlPlanBaselinesFromCursorCacheDetails.
        :type: oci.database_management.models.ManagedDatabaseCredential
        """
        self._credentials = credentials

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other