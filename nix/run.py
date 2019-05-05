from nexxera.nix.app import create_app

app = create_app()
app.run(port=9009, debug=True)
