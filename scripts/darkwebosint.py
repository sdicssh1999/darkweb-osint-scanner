import argparse
from scripts.tor_control import start_tor_service
from scripts.runner import run_tool
from scripts.utils import print_banner, list_available_tools
import os


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Dark Web OSINT Tool by @Sumandas")
    parser.add_argument("-all", action="store_true", help="Run all tools")
    parser.add_argument("-s", "--select", nargs='+', help="Select specific tools to run")
    parser.add_argument("-o", "--output", default="data/", help="Output directory")

    args = parser.parse_args()

    if not os.path.exists(args.output):
        os.makedirs(args.output)

    start_tor_service()

    with open("config/keywords.txt") as f:
        keywords = [line.strip() for line in f if line.strip()]

    if args.all:
        for tool in list_available_tools():
            run_tool(tool, output_dir=args.output, keywords=keywords)
    elif args.select:
        for tool in args.select:
            run_tool(tool, output_dir=args.output, keywords=keywords)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

