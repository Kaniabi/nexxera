def create_app(name, config_updates=None):
    import flask
    import flask_sqlalchemy
    import flask_restless
    from .models import create_models, ValidationError

    result = flask.Flask(name)
    result.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nix.db"
    result.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    result.config.update(config_updates or {})
    result.db = flask_sqlalchemy.SQLAlchemy(result)

    result.models = create_models(result.db)
    result.db.create_all()

    manager = flask_restless.APIManager(result, flask_sqlalchemy_db=result.db)
    manager.create_api(
        result.models.NixUser,
        methods=["GET", "POST", "DELETE"],
        validation_exceptions=[ValidationError]
    )
    manager.create_api(
        result.models.NixTransaction,
        methods=["GET", "POST", "DELETE"],
        validation_exceptions=[ValidationError],
        postprocessors={
            'GET_MANY': [result.models.NixTransaction.get_many_postprocessor]
        }
    )

    return result
