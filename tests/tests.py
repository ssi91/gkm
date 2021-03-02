import os

from git_cli.gkm import GitCLIClient


def test_context_manager():
    with GitCLIClient(None, '/') as git_client:
        assert '/' == os.getcwd()
