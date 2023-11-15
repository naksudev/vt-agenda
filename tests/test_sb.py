import pytest
from sb import *

def test_openAgenda():
    result = openAgenda()
    assert isinstance(result, str)
