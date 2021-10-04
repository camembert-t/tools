import paramiko
import socket
import subprocess
import threading

class Cmd_Tool:
    _ssh_config = None

    def __init__(self, path_ssh_config):
        if path_ssh_config:
            _ssh_config = paramiko.SSHConfig().from_path(path_ssh_config)

    def _exec_local_cmd(cmd):
        p = subprocess.Popen(
            cmd.split(),
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )

        stdout, stderr = p.communicate()

        stdout = stdout.decode('utf-8').strip()
        stderr = stderr.decode('utf-8').strip()

    def exec_local_cmd(cmd):
        cmd_thread = threading.Thread(
            target = _exec_local_cmd,
            args = (cmd, )
        )

        cmd_thread.start()
        cmd_thread.join()

    def _exec_remote_cmd(hostname, cmd):
        if not _ssh_config:
            return

        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()

        host_config = _ssh_config.lookup(hostname)
        ssh.connect(
            host_config['hostname'],
            username = host_config['user'],
            key_filename = host_config['identityfile']
        )

        stdin, stdout, stderr = ssh.exec_command(cmd)

        try:
            stdout = stdout.read().decode('utf-8').strip()
            stderr = stderr.read().decode('utf-8').strip()
        except socket.timeout:

        ssh.close()

    def exec_remote_cmd(hostname, cmd):
        cmd_thread = threading.Thread(
            target = _exec_remote_cmd,
            args = (hostname, cmd, )
        )

        cmd_thread.start()
        cmd_thread.join()

    def _get_user_at_host(hostname):
        if not _ssh_config:
            return None

        host_config = SSH_CONFIG.lookup(hostname)
        return '{}@{}'.format(host_config['user'], hostname)

    def fetch_file(hostname, src, dst):
        cmd = 'scp {}:{} {}' \
              ''.format(_get_user_at_host(hostname), src, dst)
        exec_local_cmd(cmd)

    def post_file(hostname, src, dst):
        cmd = 'scp {} {}:{}' \
              ''.format(src, _get_user_at_host(hostname), dst)
        exec_local_cmd(cmd)
