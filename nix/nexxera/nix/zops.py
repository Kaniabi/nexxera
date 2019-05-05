import click


@click.group('nix')
def main():
    pass


@main.command()
def create_db():
    from nexxera.nix.models import Base
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///nix.db', echo=True)
    Base.metadata.create_all(engine)
