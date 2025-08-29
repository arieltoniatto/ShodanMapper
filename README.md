# Shodan Mapper

A Python tool to map exposed services on the internet using the Shodan API.  
Generates CSV reports and simple graphs, organized in timestamped folders for each execution.

## Features

- Search by country, city, organization, netblock, or custom Shodan query
- Generates CSV + PNG reports
- Timestamped output folders to avoid overwriting
- Interactive or CLI mode
- Cross-platform (Linux, WSL, Windows, macOS)

## Requirements

- Python 3.10+
- Shodan API key
- Dependencies listed in `requirements.txt`

## Setup

1. **Create a virtual environment**:

```bash
python -m venv venv
````

2. **Activate the virtual environment**:

```bash
# Linux / WSL / macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Install project dependencies**:

```bash
pip install -r requirements.txt
```

4. **Set your Shodan API Key**:

```bash
# Linux / WSL / macOS
export SHODAN_API_KEY='YOUR_API_KEY'

# Windows CMD
setx SHODAN_API_KEY "YOUR_API_KEY"

# Or add to .env file in project root
SHODAN_API_KEY=YOUR_API_KEY
```

---

## Usage

### Interactive mode

```bash
python main.py
```

The script will prompt for search filters and automatically create a timestamped output folder in `reports/YYYYMMDD_HHMMSS/`.

### CLI mode

```bash
python main.py --country BR --limit 100 --output results --output_dir reports/20250829_103015
```

Reports (CSV + PNG) are saved in the specified folder.

---

## Project Structure

```
shodan-mapper/
├── main.py
├── requirements.txt
├── .env
├── reports/
│   └── 20250829_103015/
│       ├── results.csv
│       ├── results_ports.png
│       └── results_services.png
├── .vscode/
│   └── settings.json
└── shodan_mapper/
    ├── api.py
    ├── report.py
    ├── interactive.py
    ├── utils.py
    └── config.py
```

---

## License

MIT License
