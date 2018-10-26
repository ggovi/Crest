# coding: utf-8

"""
    CrestDB REST API

    Crest Rest Api to manage data for calibration files.

    OpenAPI spec version: 2.0
    Contact: andrea.formica@cern.ch
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RuninfoApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_run_lumi_info(self, body, **kwargs):
        """
        Create an entry for run information.
        Run informations go into a separate table.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_run_lumi_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RunLumiInfoDto body: A json string that is used to construct a runlumiinfodto object: { run: xxx, ... } (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_run_lumi_info_with_http_info(body, **kwargs)
        else:
            (data) = self.create_run_lumi_info_with_http_info(body, **kwargs)
            return data

    def create_run_lumi_info_with_http_info(self, body, **kwargs):
        """
        Create an entry for run information.
        Run informations go into a separate table.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_run_lumi_info_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RunLumiInfoDto body: A json string that is used to construct a runlumiinfodto object: { run: xxx, ... } (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_run_lumi_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_run_lumi_info`")


        collection_formats = {}

        resource_path = '/runinfo'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/plain'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def find_run_lumi_info(self, **kwargs):
        """
        Finds a RunLumiInfoDto lists using parameters.
        This method allows to perform search.Arguments: from=<someformat>,to=<someformat>, format=<describe previous types>, page={ipage}, size={isize}, sort=<sortpattern>. The pattern <pattern> is in the form <param-name><operation><param-value>       <param-name> is the name of one of the fields in the dto       <operation> can be [< : >] ; for string use only [:]        <param-value> depends on the chosen parameter. A list of this criteria can be provided       using comma separated strings for <pattern>.      The pattern <sortpattern> is <field>:[DESC|ASC]
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_run_lumi_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str _from: from: the starting time or run-lumi
        :param str to: to: the ending time or run-lumi
        :param str format: format: the format to digest previous arguments [time] or [run-lumi]. Time = yyyymmddhhmiss, Run-lumi = run-lumi
        :param int page: page: the page number {0}
        :param int size: size: the page size {1000}
        :param str sort: sort: the sort pattern {since:ASC}
        :return: list[RunLumiInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.find_run_lumi_info_with_http_info(**kwargs)
        else:
            (data) = self.find_run_lumi_info_with_http_info(**kwargs)
            return data

    def find_run_lumi_info_with_http_info(self, **kwargs):
        """
        Finds a RunLumiInfoDto lists using parameters.
        This method allows to perform search.Arguments: from=<someformat>,to=<someformat>, format=<describe previous types>, page={ipage}, size={isize}, sort=<sortpattern>. The pattern <pattern> is in the form <param-name><operation><param-value>       <param-name> is the name of one of the fields in the dto       <operation> can be [< : >] ; for string use only [:]        <param-value> depends on the chosen parameter. A list of this criteria can be provided       using comma separated strings for <pattern>.      The pattern <sortpattern> is <field>:[DESC|ASC]
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.find_run_lumi_info_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str _from: from: the starting time or run-lumi
        :param str to: to: the ending time or run-lumi
        :param str format: format: the format to digest previous arguments [time] or [run-lumi]. Time = yyyymmddhhmiss, Run-lumi = run-lumi
        :param int page: page: the page number {0}
        :param int size: size: the page size {1000}
        :param str sort: sort: the sort pattern {since:ASC}
        :return: list[RunLumiInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to', 'format', 'page', 'size', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_run_lumi_info" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/runinfo/list'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if '_from' in params:
            query_params['from'] = params['_from']
        if 'to' in params:
            query_params['to'] = params['to']
        if 'format' in params:
            query_params['format'] = params['format']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'size' in params:
            query_params['size'] = params['size']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[RunLumiInfoDto]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_run_lumi_info(self, **kwargs):
        """
        Finds a RunLumiInfoDto lists.
        This method allows to perform search and sorting.Arguments: by=<pattern>, page={ipage}, size={isize}, sort=<sortpattern>. The pattern <pattern> is in the form <param-name><operation><param-value>       <param-name> is the name of one of the fields in the dto       <operation> can be [< : >] ; for string use only [:]        <param-value> depends on the chosen parameter. A list of this criteria can be provided       using comma separated strings for <pattern>.      The pattern <sortpattern> is <field>:[DESC|ASC]
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_run_lumi_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str by: by: the search pattern {none}
        :param int page: page: the page number {0}
        :param int size: size: the page size {1000}
        :param str sort: sort: the sort pattern {since:ASC}
        :return: list[RunLumiInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_run_lumi_info_with_http_info(**kwargs)
        else:
            (data) = self.list_run_lumi_info_with_http_info(**kwargs)
            return data

    def list_run_lumi_info_with_http_info(self, **kwargs):
        """
        Finds a RunLumiInfoDto lists.
        This method allows to perform search and sorting.Arguments: by=<pattern>, page={ipage}, size={isize}, sort=<sortpattern>. The pattern <pattern> is in the form <param-name><operation><param-value>       <param-name> is the name of one of the fields in the dto       <operation> can be [< : >] ; for string use only [:]        <param-value> depends on the chosen parameter. A list of this criteria can be provided       using comma separated strings for <pattern>.      The pattern <sortpattern> is <field>:[DESC|ASC]
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_run_lumi_info_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str by: by: the search pattern {none}
        :param int page: page: the page number {0}
        :param int size: size: the page size {1000}
        :param str sort: sort: the sort pattern {since:ASC}
        :return: list[RunLumiInfoDto]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['by', 'page', 'size', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_run_lumi_info" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/runinfo'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'by' in params:
            query_params['by'] = params['by']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'size' in params:
            query_params['size'] = params['size']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[RunLumiInfoDto]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
