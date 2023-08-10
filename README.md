# ansible-template-ui
Ansible Template UI provides a web-based interface for testing ansible templates. It offers a streamlined user experience for developers and users alike, making it easier than ever to validate your ansible templates.

## Preview
### New UI
![NEW UI](./media/new_ui.png)

## Features
- Intuitive Web UI
- Docker support for easy deployment
- Compatibility with PEX and traditional Python environments

## Technologies Used
- Ansible
- Python
- Docker
- Gunicorn
- PEX


## Getting Started
### Using Docker
Pull the Docker Container

```
docker pull sivel/ansible-template-ui:devel
```

Build the Docker Image

```
docker build -t ansible-template-ui:devel docker/devel
```

### Running the Web App
Development Environment

```
python -m ansible_template_ui
```

## Deployment
### Using PEX
PEX provides a way to produce a self-contained Python executable, making it easier to distribute and deploy.

1. Install PEX:
```
pip install pex
```

2. Build the PEX:
```
./build_pex.sh
```

3. Run with Gunicorn:
```
ansible_template_ui.pex -k gevent ansible_template_ui:app
```

### Without PEX
1. Install the required packages:
```
pip install -r requirements.txt -r deploy-requirements.txt
```

2. Run with Gunicorn:
```
gunicorn -k gevent ansible_template_ui:app
```

## License

This project is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for details.