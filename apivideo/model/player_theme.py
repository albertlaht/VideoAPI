"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""


import re  # noqa: F401
import sys  # noqa: F401

from apivideo.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from apivideo.model.player_theme_assets import PlayerThemeAssets
    globals()['PlayerThemeAssets'] = PlayerThemeAssets


class PlayerTheme(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'player_id': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'text': (str,),  # noqa: E501
            'link': (str,),  # noqa: E501
            'link_hover': (str,),  # noqa: E501
            'link_active': (str,),  # noqa: E501
            'track_played': (str,),  # noqa: E501
            'track_unplayed': (str,),  # noqa: E501
            'track_background': (str,),  # noqa: E501
            'background_top': (str,),  # noqa: E501
            'background_bottom': (str,),  # noqa: E501
            'background_text': (str,),  # noqa: E501
            'enable_api': (bool,),  # noqa: E501
            'enable_controls': (bool,),  # noqa: E501
            'force_autoplay': (bool,),  # noqa: E501
            'hide_title': (bool,),  # noqa: E501
            'force_loop': (bool,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'assets': (PlayerThemeAssets,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'player_id': 'playerId',  # noqa: E501
        'name': 'name',  # noqa: E501
        'text': 'text',  # noqa: E501
        'link': 'link',  # noqa: E501
        'link_hover': 'linkHover',  # noqa: E501
        'link_active': 'linkActive',  # noqa: E501
        'track_played': 'trackPlayed',  # noqa: E501
        'track_unplayed': 'trackUnplayed',  # noqa: E501
        'track_background': 'trackBackground',  # noqa: E501
        'background_top': 'backgroundTop',  # noqa: E501
        'background_bottom': 'backgroundBottom',  # noqa: E501
        'background_text': 'backgroundText',  # noqa: E501
        'enable_api': 'enableApi',  # noqa: E501
        'enable_controls': 'enableControls',  # noqa: E501
        'force_autoplay': 'forceAutoplay',  # noqa: E501
        'hide_title': 'hideTitle',  # noqa: E501
        'force_loop': 'forceLoop',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'assets': 'assets',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, player_id, *args, **kwargs):  # noqa: E501
        """PlayerTheme - a model defined in OpenAPI

        Args:
            player_id (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            name (str): The name of the player theme. [optional]  # noqa: E501
            text (str): RGBA color for timer text. Default: rgba(255, 255, 255, 1). [optional]  # noqa: E501
            link (str): RGBA color for all controls. Default: rgba(255, 255, 255, 1). [optional]  # noqa: E501
            link_hover (str): RGBA color for all controls when hovered. Default: rgba(255, 255, 255, 1). [optional]  # noqa: E501
            link_active (str): RGBA color for the play button when hovered.. [optional]  # noqa: E501
            track_played (str): RGBA color playback bar: played content. Default: rgba(88, 131, 255, .95). [optional]  # noqa: E501
            track_unplayed (str): RGBA color playback bar: downloaded but unplayed (buffered) content. Default: rgba(255, 255, 255, .35). [optional]  # noqa: E501
            track_background (str): RGBA color playback bar: background. Default: rgba(255, 255, 255, .2). [optional]  # noqa: E501
            background_top (str): RGBA color: top 50% of background. Default: rgba(0, 0, 0, .7). [optional]  # noqa: E501
            background_bottom (str): RGBA color: bottom 50% of background. Default: rgba(0, 0, 0, .7). [optional]  # noqa: E501
            background_text (str): RGBA color for title text. Default: rgba(255, 255, 255, 1). [optional]  # noqa: E501
            enable_api (bool): enable/disable player SDK access. Default: true. [optional]  # noqa: E501
            enable_controls (bool): enable/disable player controls. Default: true. [optional]  # noqa: E501
            force_autoplay (bool): enable/disable player autoplay. Default: false. [optional]  # noqa: E501
            hide_title (bool): enable/disable title. Default: false. [optional]  # noqa: E501
            force_loop (bool): enable/disable looping. Default: false. [optional]  # noqa: E501
            created_at (datetime): When the player was created, presented in ISO-8601 format.. [optional]  # noqa: E501
            updated_at (datetime): When the player was last updated, presented in ISO-8601 format.. [optional]  # noqa: E501
            assets (PlayerThemeAssets): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.player_id = player_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
