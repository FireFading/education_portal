import nox


@nox.session
def format(session: nox.Session) -> None:
    session.install("ufmt", "black", "ruff")
    session.run("ufmt", "format", ".")
    session.run("black", "--config=configs/.black.toml", "app")
    session.run(
        "ruff",
        "check",
        "--config=configs/.ruff.toml",
        "--fix",
        "app",
    )


@nox.session
def lint(session: nox.Session) -> None:
    session.install("flake8", "mypy")
    session.run("flake8", "--config=configs/.flake8", "app")
    # session.run(
    #     "mypy",
    #     "--config-file=configs/.mypy.ini",
    #     "app"
    # )


@nox.session
def run_tests(session: nox.Session) -> None:
    session.install("-r", "requirements_tests.txt")
    session.run("pytest", "./tests")
