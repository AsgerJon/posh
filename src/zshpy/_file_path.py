"""FilePath represents a file path in the file system. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os


class FilePath:
  """FilePath represents a file path in the file system. """

  def parseStrings(self, *args: str, **kwargs) -> list[str]:
    """Parse the strings into a file path. """
    out = []
    for arg in args:
      if isinstance(arg, (tuple, list)):
        out = [*out, *self.parseStrings(*arg)]
      elif isinstance(arg, str):
        if '/' in arg:
          out = [*out, *self.parseStrings(*arg.split('/'), )]
        else:
          out.append(arg)
      else:
        out.append(str(arg))
    return out

  def __init__(self, *args: str) -> None:
    leadingChar = '~'
    strArgs = self.parseStrings(*args)
    first = [*strArgs, None][0]
    if first is None:
      self.__inner_path__ = os.path.join('~')
    elif first:
      self.__inner_path__ = os.path.join('~', *strArgs)
    else:
      self.__inner_path__ = os.path.join('/', *strArgs)

  def __str__(self, ) -> str:
    return self.__inner_path__
