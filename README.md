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
````


## Set your Shodan API key:

#### Linux / WSL / macOS
```bash
export SHODAN_API_KEY='YOUR_API_KEY'
```
#### Windows CMD
```bash
setx SHODAN_API_KEY "YOUR_API_KEY"
```
#### Or add to .env
```bash
SHODAN_API_KEY=YOUR_API_KEY
```

### Usage
Interactive mode
```bash
python main.py
```

CLI mode
```bash
python main.py --country BR --limit 100 --output_dir reports/20250829_103015
```


Reports are saved in reports/YYYYMMDD_HHMMSS/ with CSV and PNG files.
