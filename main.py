import argparse
from src.api import search_shodan
from src.report import generate_report
from src.utils import build_query
from src.interactive import interactive_query
from pathlib import Path
from datetime import datetime

# ----------------------------
# Default timestamped output folder
# ----------------------------
base_output_dir = Path("reports")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
default_output_dir = base_output_dir / timestamp
default_output_dir.mkdir(parents=True, exist_ok=True)

# ----------------------------
# CLI arguments
# ----------------------------
parser = argparse.ArgumentParser(description="Shodan service mapper")
parser.add_argument("--country")
parser.add_argument("--city")
parser.add_argument("--org")
parser.add_argument("--net")
parser.add_argument("--query")
parser.add_argument("--limit", type=int)
parser.add_argument("--output")
parser.add_argument("--output_dir", type=str, default=str(default_output_dir))
args = parser.parse_args()

# ----------------------------
# Decide interactive or CLI mode
# ----------------------------
if not any([args.country, args.city, args.org, args.net, args.query]):
    country, city, org, net, custom, limit, output, output_dir = interactive_query(default_output_dir=Path(args.output_dir))
    if not any([country, city, org, net, custom]):
        exit(1)
else:
    country = args.country
    city = args.city
    org = args.org
    net = args.net
    custom = args.query
    limit = args.limit or 100
    output = args.output or "results"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

# ----------------------------
# Build query and run search
# ----------------------------
query = build_query(country, city, org, net, custom)
print(f"🔍 Running query: {query}")

df = search_shodan(query, limit=limit)
print(df.head())

generate_report(df, output_prefix=output, output_dir=output_dir)
