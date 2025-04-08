# Vulhub Manager 🔧

A utility toolkit to automate, manage, and safely deploy multiple vulnerable environments from [Vulhub](https://github.com/vulhub/vulhub) for security testing and research.

## 📦 Included Tools

### 1. `compose-up-all.sh`
**Description:**  
Scans all subdirectories under the Vulhub project and automatically starts any environment containing a `docker-compose.yml` file.

**Features:**
- One-click mass deployment of vulnerable containers
- Runs `docker compose up -d` for each directory
- Logs output for clarity
- Easily extensible

### 2. `randomize_ports.py`
**Description:**  
Automatically modifies all `docker-compose.yml` files in Vulhub to assign **random host ports** (while preserving the internal container ports). Prevents port conflicts when deploying multiple environments.

**Features:**
- Random host port assignment (20000–65000 range)
- Recursively edits all `docker-compose.yml` files
- Safe and idempotent YAML parsing with `PyYAML`
- Compatible with most Vulhub modules

## 🚀 Quick Start

```bash
git clone https://github.com/yourname/vulhub-manager.git
cd vulhub-manager
python3 randomize_ports.py    # Optional: avoid port conflicts
./compose-up-all.sh           # Launch all Vulhub environments
