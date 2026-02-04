# Multi-Recon-Integrated-Subdomain-Discovery-Tool
A powerful Python-based wrapper that aggregates results from industry-standard subdomain enumeration tools. This script automates the reconnaissance phase by combining passive and active discovery methods into a single, deduplicated output.
## 🚀 Features
* **Multi-Tool Integration:** Combines `Subfinder`, `Assetfinder`, `Chaos`, and `Sublist3r`.
* **Deduplication:** Automatically merges results and removes duplicate entries.
* **Automatic Cleaning:** Filters out "garbage" data and focuses only on the target domain.
* **API Support:** Native integration for ProjectDiscovery's Chaos API.
* **Fast Execution:** Leverages the speed of Go-based tools alongside Python's flexibility.

---

## 🛠️ Prerequisites
This script requires the following tools to be installed and available in your system `$PATH`:

1. **Subfinder** (`sudo apt install subfinder`)
2. **Assetfinder** (`sudo apt install assetfinder`)
3. **Chaos-Client** (`go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest`)
4. **Sublist3r** (Included in this repo)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AthulCys/multi-recon.git](https://github.com/YOUR_USERNAME/multi-recon.git)
   cd multi-recon
Set up a Virtual Environment:

Bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
Configure API Keys: The script uses a hardcoded key or environment variable for Chaos. To use it globally:

Bash
export PDCP_API_KEY="your_chaos_api_key_here"
💻 Usage
Run the scanner by providing a target domain:

Bash
python3 hunt.py domainname
