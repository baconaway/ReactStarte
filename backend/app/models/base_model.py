from pydantic import BaseModel
from typing import TypeVar, Type, List, Tuple

T = TypeVar('T', bound='BaseAPIModel')

class BaseAPIModel(BaseModel):
    """
    A foundational API model class that provides utility methods for converting tuples to model instances.

    This class is designed to be inherited by other Pydantic models that wish to utilize the 
    provided utility functions for creating model instances from tuple data. This is particularly useful 
    when working with database rows returned as tuples.

    Methods:
    - from_tuple: Create an instance of the model from a tuple.
    - list_from_tuples: Create a list of model instances from a list of tuples.
    """

    @classmethod
    def from_tuple(
        cls: Type[T],
        data: Tuple
    ) -> T:
        """
        Convert a tuple to an instance of the model.

        This method attempts to map the fields of the tuple to the model's fields based on the order 
        in which they are defined. If the tuple has `_fields` and `_data` attributes (like namedtuples), 
        those are used for conversion. Otherwise, it will use the model's field keys.

        Args:
            - data (Tuple): The tuple containing the data.

        Returns:
            - T: An instance of the model.
        """
        if hasattr(data, '_fields') and hasattr(data, '_data'):
            return cls(**{field: value for field, value in zip(data._fields, data._data)})
        else:
            return cls(**dict(zip(cls.__config__.fields.keys(), data)))
    
    @classmethod
    def list_from_tuples(
        cls: Type[T],
        tuple_list: List[Tuple]
    ) -> List[T]:
        """
        Convert a list of tuples to a list of model instances.

        This method utilizes the `from_tuple` method to transform each tuple in the list into a 
        corresponding model instance.

        Args:
            - tuple_list (List[Tuple]): A list of tuples to be converted.

        Returns:
            - List[T]: A list of model instances.
        """
        return [cls.from_tuple(data) for data in tuple_list]