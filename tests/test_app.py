from app.version import get_version


class TestApp(object):
    def test_version(self):
        version = get_version()
        assert version
