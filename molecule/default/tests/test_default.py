def test_disable_ipv6(host):
    cmd = host.run('ip addr show')

    assert 'inet6' not in cmd.stdout
