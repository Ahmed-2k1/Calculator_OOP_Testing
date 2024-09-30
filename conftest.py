import pytest
from faker import Faker

fake = Faker()


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=1,
                     type=int, help="Number of records to generate")


@pytest.fixture
def generated_data(request):
    """Fixture to generate test data."""
    num_records = request.config.getoption("--num_records")
    test_data = []
    for _ in range(num_records):
        a = fake.random_int(1, 100)
        b = fake.random_int(1, 100)
        operation = fake.random_element(
            elements=('add', 'subtract', 'multiply', 'divide'))
        test_data.append((a, b, operation))
    return test_data


def test_generated_data(generated_data):
    """Test that the generated_data fixture provides valid data."""
    for a, b, operation in generated_data:
        assert isinstance(a, int)
        assert isinstance(b, int)
        assert operation in ['add', 'subtract', 'multiply', 'divide']


def test_pytest_addoption(pytestconfig):
    """Test if the --num_records option is properly configured."""
    assert pytestconfig.getoption("num_records") == 1  # Default value is 1