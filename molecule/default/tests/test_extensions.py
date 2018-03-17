import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vscode_installed(host):
    assert host.package("code").is_installed


@pytest.mark.parametrize("ext", ['gitlens', 'ms-python', 'vscodevim'])
def test_vscode_extensions(host, ext):
    EXT_DIR = "/home/reguser/.vscode/extensions"
    ext_list = host.check_output("ls %s" % EXT_DIR)
    assert ext in ext_list
