from photos.tests.fixtures import get_fixture
from mock import Mock

def fake_results(api, fixture_name):
    api.make_request = Mock(return_value=api)
    api._call_api = Mock()
    api._call_api.return_value = get_fixture("api_list.json")
