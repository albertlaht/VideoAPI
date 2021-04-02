"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from apivideo.api_client import ApiClient
from apivideo.endpoint import EndPoint as _EndPoint
from apivideo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from apivideo.exceptions import ApiTypeError, ApiValueError
from apivideo.model.account import Account
from apivideo.model.not_found import NotFound


class AccountApi(_EndPoint):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def get(
            self,
            **kwargs
        ):
            """Show account  # noqa: E501

            Deprecated. Authenticate and get a token, then you can use the bearer token here to retrieve details about your account.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Account
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')

            params_map = {
                'all': [
                    'async_req',
                    '_host_index',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only',
                    '_check_input_type',
                    '_check_return_type'
                ],
                'required': [],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
            }
            openapi_types = {
                'async_req': (bool,),
                '_host_index': (none_type, int),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,),
                '_check_input_type': (bool,),
                '_check_return_type': (bool,)
            }
            attribute_map = {
            }
            location_map = {
            }
            collection_format_map = {
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get`" %
                        (key, )
                    )
                # only throw this nullable ApiValueError if _check_input_type
                # is False, if _check_input_type==True we catch this case
                # in self.__validate_inputs
                if (key not in params_map['nullable'] and value is None
                        and kwargs['_check_input_type'] is False):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/account",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(Account,),
                async_req=kwargs['async_req'],
                _check_type=kwargs['_check_return_type'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

