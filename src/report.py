import pandas as pd
import matplotlib.pyplot as plt
import csv
import os

def generate_report(df, output_prefix="results", output_dir="."):
    if df.empty:
        print("⚠️ No data to generate report.")
        return

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Top ports
    top_ports = df['port'].value_counts().head(10)
    top_services = df['service'].value_counts().head(10)

    if not top_ports.empty:
        top_ports.plot(kind="bar", title="Top 10 Exposed Ports", ylabel="Count", xlabel="Port")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{output_prefix}_ports.png"))
        plt.clf()

    if not top_services.empty:
        top_services.plot(kind="bar", title="Top 10 Exposed Services", ylabel="Count", xlabel="Service")
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f"{output_prefix}_services.png"))
        plt.clf()

    # Save CSV with proper escaping
    df.to_csv(
        os.path.join(output_dir, f"{output_prefix}.csv"),
        index=False,
        sep=",",
        quoting=csv.QUOTE_ALL,
        escapechar="\\",
        encoding="utf-8"
    )

    print(f"✅ Report generated in folder '{output_dir}':")
    print(f"   {output_prefix}.csv")
    print(f"   {output_prefix}_ports.png")
    print(f"   {output_prefix}_services.png")
