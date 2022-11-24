import config

app = config.connexion_app

app.add_api(config.basedir / "openapi/swagger.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)