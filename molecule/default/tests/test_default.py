import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_icinga2_installed(host):
    icinga2 = host.package("icinga2")
    assert icinga2.is_installed


def test_icinga2_running_and_enabled(host):
    icinga2 = host.service("icinga2")
    assert icinga2.is_running
    assert icinga2.is_enabled
