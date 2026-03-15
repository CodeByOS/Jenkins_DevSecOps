from app import get_data

def test_api():
    assert get_data() == 200