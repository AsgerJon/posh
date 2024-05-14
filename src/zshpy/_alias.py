"""Alias uses descriptor protocol to create aliases in the shell."""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from zshpy import AbstractZshLine


class Alias(AbstractZshLine):
  """Alias uses descriptor protocol to create aliases in the shell."""

  def apply(self, ) -> str:
    """Apply the alias to the shell."""
    rhs = ' '.join([str(arg) for arg in self.getArgs()])
    lhs = 'alias %s' % self.__field_name__
    return '%s="%s"' % (lhs, rhs)
