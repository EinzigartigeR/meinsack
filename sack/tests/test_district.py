import os.path
import pytest
from main.utils import get_districts_stuttgart, add_district_to_database, extract_data_from_tr


@pytest.fixture
def stuttgart_districts():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'fixtures/',
                        'stuttgart_districts.html')


@pytest.mark.django_db
class TestDistrict():

    def test_district_import(self, stuttgart_districts):
        x = get_districts_stuttgart(stuttgart_districts)
        assert len(list(x)) == 57

    def test_extract_data_from_tr(self, stuttgart_districts):
        for index, tr in enumerate(get_districts_stuttgart(stuttgart_districts)):
            if index == 0:
                # ignore head
                continue
            x = extract_data_from_tr(tr)
            assert isinstance(x, dict)
            assert 'name' in x
            break  # one is enough

    def test_add_district_to_database(self, stuttgart_districts):
        for index, tr in enumerate(get_districts_stuttgart(stuttgart_districts)):
            if index == 0:
                # ignore head
                continue
            x = extract_data_from_tr(tr)
            district = add_district_to_database(x)
            assert district.name == x['name']
            print(district.__dict__)
            break  # one is enough
