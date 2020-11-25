def test_swarm_service_rc(host):
    cmd = host.run("docker service ls")
    assert cmd.rc == 0
