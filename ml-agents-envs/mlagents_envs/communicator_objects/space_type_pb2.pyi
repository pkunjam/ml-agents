# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


builtin___int = int
builtin___str = str


class SpaceTypeProto(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'SpaceTypeProto': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['SpaceTypeProto']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SpaceTypeProto']]: ...
    discrete = typing___cast('SpaceTypeProto', 0)
    continuous = typing___cast('SpaceTypeProto', 1)
discrete = typing___cast('SpaceTypeProto', 0)
continuous = typing___cast('SpaceTypeProto', 1)