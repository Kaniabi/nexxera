import pytest


@pytest.fixture(name="flask_live_url")
def _flask_live_url(live_server):
    yield live_server.url()


@pytest.fixture()
def app():
    from nexxera.nix.app import create_app

    # TODO: The connexion application (returned by create_app()) is alive by coincidence.
    return create_app().app
