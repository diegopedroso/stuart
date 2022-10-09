from stuart.core import get_event_source, add_event_source

def test_add_event_source():
    assert add_event_source("45", "10")

def test_get_event_source():
    add_event_source("45", "10")
    results = get_event_source()
    assert len(results) > 0