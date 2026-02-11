
import pytest

from stuff.accum import Accumulator

# A funtion that handles setup and clean up operations for a test case
@pytest.fixture
def accum2():
    return Accumulator()


@pytest.fixture
def accum3():
    yield Accumulator()
    print("DONE-ZO!")


@pytest.fixture  # Fixture only 1 time when set to session
def accum4(scope="session"):
    return Accumulator()


# def test_accumulator_init():
#    accum = Accumulator()
#    assert accum.count == 0
@pytest.mark.accumulator
def test_accumulator_init(accum):  # Example of how fixture works
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    # accum = Accumulator()
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    # accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    # accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    # accum = Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


