import subprocess

ip = '192.168.1.13'

for node_num in range(1, 4):

    node_name = f"hazelcast-node-{node_num}"
    command = [
        "docker", "run", "-it", "--name", node_name, "--rm",
        "-e", f"HZ_NETWORK_PUBLICADDRESS={ip}:570{node_num}",
        "-e", "HZ_CLUSTERNAME=hazelcast-cluster-log",
        "-p", f"570{node_num}:5701",
        "hazelcast/hazelcast:5.3.6"
    ]
    subprocess.Popen(command)