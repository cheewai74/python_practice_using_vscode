import pytest
from stuff.accum import Accumulator

#------------------------------------------------------------------------
# Fixtures
#------------------------------------------------------------------------

@pytest.fixture
def accum():
    return Accumulator()