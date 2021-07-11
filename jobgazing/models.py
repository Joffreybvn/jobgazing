
import json
from enum import Enum


class Job(str, Enum):
    AI = 'ai',
    WEB = 'web'


class Enterprise:
    """Enterprise data model."""

    # Prevent any other attributes from being created.
    __slots__ = ('name', 'locations', 'website')

    def __init__(self, **kwargs):
        """
        Create a class to store enterprise data.

        Parameters
        ----------
        name : str
            Name of the enterprise.
        locations : list
            List of the locations where the enterprise is situated at.
        website : str
            Website's URL of the enterprise.
        """

        # Use super to set around __setattr__ definition.
        for parameter, value in kwargs.items():
            if parameter in self.__slots__:
                super(Enterprise, self).__setattr__(parameter, value)

    def __setattr__(self, obj, value):
        """Override setattr. Prevent user from modifying this class' attributes"""
        raise AttributeError('Enterprise is an immutable object.')

    def __str__(self) -> str:
        """Customize stdout when called with print()."""
        locations: str = ','.join(self.locations)
        return f'Enterprise: {self.name}, locations: {locations} - {self.website}'

    def __dict__(self) -> dict:
        """
        Implement the dictionary representation of this class.
        """
        # By default, all classes implement the __dict__ class variable, but
        # the custom declared __slot__ class variable remove it. Thus, we
        # re-implement a custom __dict__() class method.
        return {key: getattr(self, key) for key in self.__slots__}

    def __iter__(self):
        """
        Return this object's content as Iterator of tuple(key, value).
        Allow this object to be called with dict() and list().
        """
        for key in self.dict():
            yield key, getattr(self, key)

    def __getitem__(self, key: str):
        """
        Implement the behavior of a dictionary to this object.
        Return the attribute's value corresponding to the given key.
        """
        if isinstance(key, str):
            if key in self.__slots__:
                return getattr(self, key)

            # Raise KeyError when a missing attributes is passed.
            raise KeyError(f'Key must be one of {self.__slots__}, not {key}')

        # Raise a TypeError if the given key is not a string.
        else:
            raise TypeError(f'Key must be str, not {type(key).__name__}')

    def __len__(self) -> int:
        """Return the amount of this object's attributes."""
        return len(self.__slots__)

    def dict(self) -> dict:
        """Return a dictionary representation of this object."""
        return self.__dict__()

    def json(self, indent: int = 4) -> str:
        """Return a JSON-formatted representation of this object."""
        return json.dumps(self.dict(), indent=indent)

    def resume(self) -> dict:
        """Return a dictionary of this object's name, locations and website."""
        content = self.dict()
        keys_to_filter = ('name', 'locations', 'website')
        return {key: content[key] for key in keys_to_filter if key in content}
