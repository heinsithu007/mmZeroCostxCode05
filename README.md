# Enhanced CodeAgent03 + DeepSeek R1 + vLLM Integration

This project creates a powerful, locally-running AI coding assistant by integrating CodeAgent03 with DeepSeek R1 through vLLM, building upon OpenHands integration work.

## System Configuration
- **Platform**: Linux 5.15.0-1078-gke
- **CPU Cores**: 4
- **Total RAM**: 15 GB
- **Configuration**: CPU-optimized deployment (no GPU detected)
- **Python**: 3.12.10

## Project Structure
```
enhanced-codeagent-integration/
├── repositories/          # Cloned repositories
├── src/                  # Integration source code
├── config/               # Configuration files
├── scripts/              # Deployment and utility scripts
├── docker/               # Docker configurations
├── tests/                # Test suites
├── docs/                 # Documentation
├── frontend/             # Web frontend
└── backend/              # Backend services
```

## Quick Start
1. Run system detection: `./scripts/detect_system.py`
2. Install dependencies: `./scripts/auto_install.sh`
3. Start services: `./scripts/start.sh`
4. Access web interface: http://localhost:8080

## Features
- Local DeepSeek R1 deployment via vLLM
- CodeAgent03 full integration
- OpenHands compatibility
- Multi-user support
- Real-time collaboration
- Automated testing and validation
- CPU/GPU adaptive configuration