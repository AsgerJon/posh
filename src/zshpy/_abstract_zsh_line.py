"""The zshpy module intends to provide a pythonic way of augmenting the
zsh shell as is done in the .zshrc file. AbstractZshLine provides an
abstract baseclass for entries that suitable for zsh configuration. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from abc import abstractmethod
from typing import Never


class AbstractZshLine:
  """The zshpy module intends to provide a pythonic way of augmenting the
  zsh shell as is done in the .zshrc file. AbstractZshLine provides an
  abstract baseclass for entries that suitable for zsh configuration. """

  __pos_args__ = None
  __key_args__ = None
  __field_name__ = None
  __field_owner__ = None

  def __init__(self, *args, **kwargs) -> None:
    self.__pos_args__ = [*args, ]
    self.__key_args__ = {**kwargs, }

  def __set_name__(self, owner: type, name: str) -> None:
    self.__field_name__ = name
    self.__field_owner__ = owner

  def __set__(self, *_) -> Never:
    """Illegal accessor"""
    e = """%s does not support setting!"""
    raise TypeError(e % self.__class__.__name__)

  def __delete__(self, *_) -> Never:
    """Illegal accessor"""
    e = """%s does not support deletion!"""
    raise TypeError(e % self.__class__.__name__)

  def getArgs(self) -> list:
    """Return the arguments of the alias."""
    return self.__pos_args__

  def getKwargs(self) -> dict:
    """Return the keyword arguments of the alias."""
    return {**self.__key_args__, }

  @abstractmethod
  def apply(self, ) -> None:
    """Subclasses should implement this method to define how this
    entry should be applied to the zsh shell. """
