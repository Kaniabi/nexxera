import connexion


app = connexion.App(
    __name__,
    specification_dir='openapi',
    arguments={}
)
app.add_api('nix.yaml', arguments={})
app.run(port=9009, debug=True)
