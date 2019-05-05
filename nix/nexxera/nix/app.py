def create_app():
    import connexion

    result = connexion.App(
        __name__,
        specification_dir='openapi',
        arguments={}
    )
    result.add_api('nix.yaml', arguments={})

    return result
