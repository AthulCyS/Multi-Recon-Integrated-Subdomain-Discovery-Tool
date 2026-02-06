import subprocess
import os
import sys

# Your Specific Configuration
CHAOS_KEY = "type your cahsos api key"

def run_tool(name, cmd):
    print(f"[*] Running {name}...")
    # Chaos and Subfinder use this environment variable for their API keys
    env = os.environ.copy()
    env["PDCP_API_KEY"] = CHAOS_KEY 
    
    try:
        # Run the command and capture output
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True, env=env)
        results = process.stdout.splitlines()
        
        # Filter for only subdomains (removes banners/noise)
        clean_results = {line.strip().lower() for line in results if "." in line}
        print(f"[+] {name} found {len(clean_results)} subdomains.")
        return clean_results
    except Exception as e:
        print(f"[!] Error with {name}: {e}")
        return set()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 hunt.py <domain.com>")
        sys.exit(1)

    target = sys.argv[1]
    master_list = set()

    # Optimized Tool Commands
    tools = {
        "Subfinder": f"subfinder -d {target} -silent",
        "Assetfinder": f"assetfinder --subs-only {target}",
        "Chaos": f"chaos -d {target} -key {CHAOS_KEY} -silent",
        "Sublist3r": f"python3 sublist3r.py -d {target} -n"
    }

    for name, cmd in tools.items():
        master_list.update(run_tool(name, cmd))

    # Final cleanup: ensure only subdomains for the target are included
    final_output = {s for s in master_list if target in s}

    output_file = f"{target}_results.txt"
    with open(output_file, "w") as f:
        f.write("\n".join(sorted(final_output)))

    print("-" * 30)
    print(f"Total Unique Subdomains Found: {len(final_output)}")
    print(f"Results saved to: {output_file}")

if __name__ == "__main__":
    main()
