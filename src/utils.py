def build_query(country=None, city=None, org=None, net=None, custom=None):
    """
    Build Shodan query from parameters.
    """
    parts = []
    if country:
        parts.append(f"country:{country}")
    if city:
        parts.append(f'city:"{city}"')
    if org:
        parts.append(f'org:"{org}"')
    if net:
        parts.append(f"net:{net}")
    if custom:
        parts.append(custom)

    if not parts:
        raise ValueError("At least one search parameter must be provided.")

    return " ".join(parts)
