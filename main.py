"""Main Tester Script"""
#  GPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import time
from typing import Callable

from icecream import ic
from vistutils.text import stringList

from zshpy import FilePath


def tester00() -> int:
  """Hello world"""
  stuff = [os, sys, ic, 'hello world!', ]
  for item in stuff:
    print(item)
  return 0


def tester01() -> int:
  """Main Tester Script"""
  kill = FilePath(
    '/home/AsgerJon/PycharmProjects/ezside/src/ezside/widgets/charts'
    '/__pycache__/')
  print(kill)
  return 0


def main(callMeMaybe: Callable) -> None:
  """Main Tester Script"""
  tic = time.time()
  print('Running python script located at: \n%s' % sys.argv[0])
  print('Started at: %s' % time.ctime())
  print(77 * '-')
  retCode = 0
  try:
    retCode = callMeMaybe()
  except Exception as exception:
    print('Exception: %s' % exception)
    raise exception
  retCode = 0 if retCode is None else retCode
  print(77 * '-')
  print('Return Code: %s' % retCode)
  print('Runtime: %.3f seconds' % (time.time() - tic))


if __name__ == '__main__':
  main(tester01)
