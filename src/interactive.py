MAX_LIMIT = 1000
from pathlib import Path
from datetime import datetime

def interactive_query(default_output_dir=None):
    """
    Interactive prompt for selecting Shodan search parameters.
    default_output_dir: pre-created timestamped folder from setup.py
    """
    print("🔹 Shodan Mapper Interactive Mode 🔹")
    print("Choose a filter type:")
    print("1 - Country")
    print("2 - City")
    print("3 - Organization")
    print("4 - Netblock")
    print("5 - Custom query")
    choice = input("Enter your choice (1-5): ").strip()

    country = city = org = net = custom = None

    if choice == "1":
        country = input("Enter country code (e.g., BR, US): ").strip()
    elif choice == "2":
        city = input("Enter city name: ").strip()
    elif choice == "3":
        org = input("Enter organization name: ").strip()
    elif choice == "4":
        net = input("Enter netblock (e.g., 8.8.8.0/24): ").strip()
    elif choice == "5":
        custom = input("Enter custom Shodan query: ").strip()
    else:
        print("Invalid choice. Exiting.")
        return None, None, None, None, None, None, None

    limit = input(f"Enter result limit (default 100, max {MAX_LIMIT}): ").strip()
    if not limit.isdigit():
        limit = 100
    else:
        limit = min(int(limit), MAX_LIMIT)

    output = input("Enter output file prefix (default 'results'): ").strip() or "results"

    # Use timestamped folder if default provided
    if default_output_dir:
        output_dir = default_output_dir
    else:
        output_dir_input = input("Enter output folder (default current folder '.'): ").strip()
        if output_dir_input:
            output_dir = Path(output_dir_input)
        else:
            output_dir = Path(".")

    output_dir.mkdir(parents=True, exist_ok=True)

    return country, city, org, net, custom, limit, output, output_dir
