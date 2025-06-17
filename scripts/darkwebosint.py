import argparse
from utils import generate_keywords, update_keywords_file, print_banner
from runner import run_all_tools
from tor_control import start_tor_service

if __name__ == "__main__":
    start_tor_service()
    print_banner()
    parser = argparse.ArgumentParser(description="WODS - World of Dark Side OSINT Scanner")
    parser.add_argument("-org", "--organization", help="Organization name to generate OSINT keywords", required=False)
    args = parser.parse_args()

    if not args.organization:
        org = input("🔍 Enter your organization name for OSINT: ").strip()
    else:
        org = args.organization.strip()

    keywords = generate_keywords(org)
    update_keywords_file(keywords)
    run_all_tools()

