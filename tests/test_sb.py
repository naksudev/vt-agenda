import pytest
from ../modules import sb

def test_openAgenda():
    result = sb.openAgenda()
    assert isinstance(result, str)
