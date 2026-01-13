import os

# Set the root directory to scan (current directory or via param)
import sys

DEFAULT_ROOT = os.path.dirname(os.path.abspath(__file__))
OUTPUT_MD = "file_paths.md"
SCRIPT_NAME = os.path.basename(__file__)

# Set your GitHub raw base URL
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/ia-p16/p16_public/main/"

# Allow folder to be specified as a parameter
if len(sys.argv) > 1:
    ROOT_DIR = os.path.abspath(sys.argv[1])
else:
    ROOT_DIR = DEFAULT_ROOT

def should_ignore_dir(dirname):
    return dirname.startswith(".git")

def is_pdf(filename):
    return filename.lower().endswith(".pdf")

with open(OUTPUT_MD, "w") as md_file:
    md_file.write("# Raw PDF File URLs\n\n")
    for root, dirs, files in os.walk(ROOT_DIR):
        # Ignore dirs starting with 'git'
        dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

        # Only process files at the root or in the specified folder
        for file in files:
            if file == OUTPUT_MD or file == SCRIPT_NAME:
                continue  # Skip the generated file and the script itself
            if not is_pdf(file):
                continue  # Only .pdf files
            rel_path = os.path.relpath(os.path.join(root, file), DEFAULT_ROOT)
            rel_path_url = rel_path.replace(os.sep, "/")
            full_url = GITHUB_RAW_BASE + rel_path_url
            md_file.write(f"- {full_url}\n")

print(f"PDF file URLs written to {OUTPUT_MD}")
