import pytest

from datetime import datetime

from apps.tvazteca.cabs.coding.util import *


def test_getDateBoorlandActual():
   assert getDateBoorlandActual(datetime.now()) == 42975

def test_subString():
   data = subString('hola', 'o')
   assert data == 'la'