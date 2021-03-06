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


class SignalRKeys(Model):
    """A class represents the access keys of SignalR service.

    :param primary_key: The primary access key.
    :type primary_key: str
    :param secondary_key: The secondary access key.
    :type secondary_key: str
    :param primary_connection_string: SignalR connection string constructed
     via the primaryKey
    :type primary_connection_string: str
    :param secondary_connection_string: SignalR connection string constructed
     via the secondaryKey
    :type secondary_connection_string: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(self, *, primary_key: str=None, secondary_key: str=None, primary_connection_string: str=None, secondary_connection_string: str=None, **kwargs) -> None:
        super(SignalRKeys, self).__init__(**kwargs)
        self.primary_key = primary_key
        self.secondary_key = secondary_key
        self.primary_connection_string = primary_connection_string
        self.secondary_connection_string = secondary_connection_string
