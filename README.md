# Shodan Mapper

A Python tool to map exposed services on the internet using the Shodan API.  
Generates CSV reports and simple graphs, organized in timestamped folders for each execution.

## Features

- Search by country, city, organization, netblock, or custom Shodan query
- Generates CSV + PNG reports
- Timestamped output folders to avoid overwriting
- Interactive or CLI mode
- Cross-platform setup with virtual environment

## Requirements

- Python 3.10+
- Shodan API key
- Dependencies listed in `requirements.txt`

## Setup

Run the setup script to create a virtual environment, install dependencies, and create a reports folder:

```bash
python setup.py
