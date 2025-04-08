import os
import random
import yaml

VULHUB_DIR = "vulhub"

def get_random_port(start=20000, end=65000):
    return random.randint(start, end)

def randomize_ports_in_compose(file_path):
    with open(file_path, 'r') as f:
        try:
            compose = yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Failed to parse {file_path}: {e}")
            return

    updated = False

    for service in compose.get('services', {}).values():
        ports = service.get('ports', [])
        new_ports = []

        for port in ports:
            if isinstance(port, str) and ':' in port:
                host_port, container_port = port.split(':')
                new_host_port = str(get_random_port())
                new_ports.append(f"{new_host_port}:{container_port}")
                print(f"🔄 {host_port}->{new_host_port} for {container_port} in {file_path}")
                updated = True
            else:
                new_ports.append(port)

        service['ports'] = new_ports

    if updated:
        with open(file_path, 'w') as f:
            yaml.dump(compose, f, default_flow_style=False)
        print(f"✅ Updated {file_path}")

def walk_and_randomize(root_dir):
    for root, dirs, files in os.walk(root_dir):
        if 'docker-compose.yml' in files:
            file_path = os.path.join(root, 'docker-compose.yml')
            randomize_ports_in_compose(file_path)

if __name__ == "__main__":
    walk_and_randomize(VULHUB_DIR)
