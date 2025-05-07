# Monitoring App with Load Balancer - Context

## Project Overview
This project implements a monitoring system with load balancing capabilities for a clinical handler application. The system is designed to ensure high availability and optimal performance through distributed architecture and health monitoring.

## Architecture Components

### 1. Load Balancer (Kong)
- Implements round-robin load balancing algorithm
- Health check configuration:
  - Active health checks every 5 seconds
  - Threshold of 66% for healthy instances
  - Endpoint: `/health/`
  - Timeout: 2 seconds per attempt
  - Requires 1 successful response for healthy status
  - 1 failure for unhealthy status

### 2. Backend Services
- Multiple instances running on different IPs (10.128.0.10, 10.128.0.11, 10.128.0.12)
- Port: 8080
- Built with Django 2.1.5
- PostgreSQL database integration (psycopg2-binary 2.8.6)

### 3. Project Structure
- `monitoring/`: Core monitoring application
- `alarms/`: Alarm system components
- `measurements/`: Data collection and metrics
- `variables/`: Configuration and environment variables
- `Jmeter-test/`: Performance testing suite
- `docs/`: Project documentation

### 4. Infrastructure
- Docker support (Dockerfile included)
- Virtual environment management (venv)
- Git version control

## Key Features
1. Distributed architecture with multiple service instances
2. Automated health monitoring
3. Load balancing for optimal resource utilization
4. Performance testing capabilities
5. Containerization support

## Technical Stack
- Backend: Django 2.1.5
- Database: PostgreSQL
- Load Balancer: Kong
- Container: Docker
- Testing: JMeter

## Development Environment
- Python virtual environment
- Docker for containerization
- Git for version control
- JMeter for performance testing

## Monitoring and Maintenance
- Health check endpoints for service monitoring
- Load balancer configuration for service distribution
- Performance testing suite for load testing
- Alarm system for issue detection and notification
