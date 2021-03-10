import os
import sys

from git_cli.gkm import GitCLIClient
from gkm import _parse_argv


def test_context_manager():
    with GitCLIClient(None, '/') as git_client:
        assert '/' == os.getcwd()


def test__parse_argv():
    input0 = "command -i /path/to/key some git command"
    input1 = "command some git command"
    argv0 = input0.split(' ')
    argv1 = input1.split(' ')

    sys.argv = argv0
    assert ('/path/to/key', ['some', 'git', 'command']) == _parse_argv()
    sys.argv = argv1
    assert (None, ['some', 'git', 'command']) == _parse_argv()
