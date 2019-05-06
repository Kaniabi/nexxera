import pytest


@pytest.fixture(name="flask_live_url")
def _flask_live_url(live_server):
    yield live_server.url()


@pytest.fixture()
def app():
    from nexxera.nix.app import create_app

    config_updates = {
        "FLASK_TEST": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    }

    return create_app("test_nix", config_updates)
