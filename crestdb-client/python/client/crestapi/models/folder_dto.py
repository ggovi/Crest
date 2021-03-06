# coding: utf-8

"""
    CrestDB REST API

    Crest Rest Api to manage data for calibration files.

    OpenAPI spec version: 2.0
    Contact: andrea.formica@cern.ch
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FolderDto(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, node_fullpath=None, schema_name=None, node_name=None, node_description=None, tag_pattern=None, group_role=None):
        """
        FolderDto - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'node_fullpath': 'str',
            'schema_name': 'str',
            'node_name': 'str',
            'node_description': 'str',
            'tag_pattern': 'str',
            'group_role': 'str'
        }

        self.attribute_map = {
            'node_fullpath': 'nodeFullpath',
            'schema_name': 'schemaName',
            'node_name': 'nodeName',
            'node_description': 'nodeDescription',
            'tag_pattern': 'tagPattern',
            'group_role': 'groupRole'
        }

        self._node_fullpath = node_fullpath
        self._schema_name = schema_name
        self._node_name = node_name
        self._node_description = node_description
        self._tag_pattern = tag_pattern
        self._group_role = group_role

    @property
    def node_fullpath(self):
        """
        Gets the node_fullpath of this FolderDto.

        :return: The node_fullpath of this FolderDto.
        :rtype: str
        """
        return self._node_fullpath

    @node_fullpath.setter
    def node_fullpath(self, node_fullpath):
        """
        Sets the node_fullpath of this FolderDto.

        :param node_fullpath: The node_fullpath of this FolderDto.
        :type: str
        """

        self._node_fullpath = node_fullpath

    @property
    def schema_name(self):
        """
        Gets the schema_name of this FolderDto.

        :return: The schema_name of this FolderDto.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this FolderDto.

        :param schema_name: The schema_name of this FolderDto.
        :type: str
        """

        self._schema_name = schema_name

    @property
    def node_name(self):
        """
        Gets the node_name of this FolderDto.

        :return: The node_name of this FolderDto.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """
        Sets the node_name of this FolderDto.

        :param node_name: The node_name of this FolderDto.
        :type: str
        """

        self._node_name = node_name

    @property
    def node_description(self):
        """
        Gets the node_description of this FolderDto.

        :return: The node_description of this FolderDto.
        :rtype: str
        """
        return self._node_description

    @node_description.setter
    def node_description(self, node_description):
        """
        Sets the node_description of this FolderDto.

        :param node_description: The node_description of this FolderDto.
        :type: str
        """

        self._node_description = node_description

    @property
    def tag_pattern(self):
        """
        Gets the tag_pattern of this FolderDto.

        :return: The tag_pattern of this FolderDto.
        :rtype: str
        """
        return self._tag_pattern

    @tag_pattern.setter
    def tag_pattern(self, tag_pattern):
        """
        Sets the tag_pattern of this FolderDto.

        :param tag_pattern: The tag_pattern of this FolderDto.
        :type: str
        """

        self._tag_pattern = tag_pattern

    @property
    def group_role(self):
        """
        Gets the group_role of this FolderDto.

        :return: The group_role of this FolderDto.
        :rtype: str
        """
        return self._group_role

    @group_role.setter
    def group_role(self, group_role):
        """
        Sets the group_role of this FolderDto.

        :param group_role: The group_role of this FolderDto.
        :type: str
        """

        self._group_role = group_role

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FolderDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
