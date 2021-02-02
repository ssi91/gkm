import os


class GitCLIClient:
    def __init__(self, _ssh_key_path=None, _path=os.curdir):
        self._working_path = _path
        # if _ssh_key_path is None, use default key (usually it's ~/.ssh/id_rsa) without the ssh-agent
        self._ssh_key_path = _ssh_key_path
        self._current_path = os.curdir

    def __enter__(self):
        os.chdir(self._working_path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self._current_path)

    def clone(self, origin_url):
        os.chdir(self._working_path)
        os.system("ssh-agent sh -c 'ssh-add %s; git clone %s'" % (self._ssh_key_path, origin_url))

    def push(self, origin_url, branch):
        os.system("ssh-agent sh -c 'ssh-add %s; git push %s %s'" % (self._ssh_key_path, origin_url, branch))

    def command(self, *args):
        print(args)
        c = self._build_command(*args)
        os.system(c)

    def _build_command(self, *args):
        c = 'git %s' % ' '.join(args)
        return c if self._ssh_key_path is None else self._wrap_ssh_agent(c)

    def _wrap_ssh_agent(self, command):
        ssh_agent_wrap_string = "ssh-agent sh -c 'ssh-add %s; %s'" % (self._ssh_key_path, command)
        return ssh_agent_wrap_string
