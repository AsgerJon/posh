"""RunCommands instances define a collection of commands to be applied to
the zsh shell. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from typing import Any

from zshpy import AbstractZshLine

Bases = tuple[type, ...]


class RunCommands(type):
  """MetaRun is a metaclass for RunCommands. """

  __iter_contents__ = None

  def __new__(mcls,
              name: str,
              bases: Bases,
              namespace: dict,
              **kwargs) -> Any:
    """Create a new RunCommands class. """
    cls = type.__new__(mcls, name, bases, namespace, **kwargs)
    lines = []

    for (key, value) in namespace.items():
      if isinstance(value, AbstractZshLine):
        lines.append('%s' % value.apply())
    return '\n'.join(lines)
