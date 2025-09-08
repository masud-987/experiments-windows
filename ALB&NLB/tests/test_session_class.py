import pytest

# The Session class was removed when consolidating into backend/main.py.
# Keeping a minimal stand-in here or skip tests; for now we skip.
import pytest

pytest.skip("Session class removed; using Flask session now.", allow_module_level=True)



def test_session_set_and_get_value():
    s = Session(user_id="user-1")
    s.set("token", "abc123")
    assert s.get("token") == "abc123"


def test_session_get_default_when_missing():
    s = Session()
    assert s.get("missing") is None
    assert s.get("missing", default="fallback") == "fallback"


