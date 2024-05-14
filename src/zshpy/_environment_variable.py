"""Env provides for setting environment variables in the zsh shell. """
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from zshpy import AbstractZshLine


class Env(AbstractZshLine):
  """Env provides for setting environment variables in the zsh shell. """

  def apply(self, ) -> str:
    """Apply the environment variable to the shell. """
    rhs = ' '.join([str(arg) for arg in self.getArgs()])
    lhs = 'export %s' % self.__field_name__
    return '%s="%s"' % (lhs, rhs)
