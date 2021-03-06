# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OutputDirectory(Model):
    """Output directory for the job.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The name for the output directory. The path of the
     output directory will be available as a value of an environment variable
     with AZ_BATCHAI_OUTPUT_<id> name, where <id> is the value of id attribute.
    :type id: str
    :param path_prefix: Required. The prefix path where the output directory
     will be created. NOTE: This is an absolute path to prefix. E.g.
     $AZ_BATCHAI_MOUNT_ROOT/MyNFS/MyLogs. You can find the full path to the
     output directory by combining pathPrefix, jobOutputDirectoryPathSegment
     (reported by get job) and pathSuffix.
    :type path_prefix: str
    :param path_suffix: The suffix path where the output directory will be
     created. The suffix path where the output directory will be created. E.g.
     models. You can find the full path to the output directory by combining
     pathPrefix, jobOutputDirectoryPathSegment (reported by get job) and
     pathSuffix.
    :type path_suffix: str
    """

    _validation = {
        'id': {'required': True},
        'path_prefix': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'path_prefix': {'key': 'pathPrefix', 'type': 'str'},
        'path_suffix': {'key': 'pathSuffix', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OutputDirectory, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.path_prefix = kwargs.get('path_prefix', None)
        self.path_suffix = kwargs.get('path_suffix', None)
