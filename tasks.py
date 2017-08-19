from invoke import run, task


@task
def test(ctx):
    run('py.test --pep8 --cov=flask_modus test_flask_modus.py', pty=True)


@task
def travisci(ctx):
    run('py.test --pep8 test_flask_modus.py')
