#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import tempfile

def main():
    print("Building pandoc and pandoc-crossref from source...")
    
    # Build pandoc first
    build_pandoc()
    
    # Then build pandoc-crossref that matches the pandoc version
    build_pandoc_crossref()
    
    print("Both pandoc and pandoc-crossref have been built and installed successfully!")
    return 0

def build_pandoc():
    print("Building pandoc...")
    
    # Clone pandoc if it doesn't exist
    if not os.path.exists("pandoc"):
        subprocess.run(["git", "clone", "https://github.com/jgm/pandoc.git"], check=True)
    
    # Change to the pandoc directory
    os.chdir("pandoc")
    
    # Check if Stack is installed
    if shutil.which("stack") is None:
        print("Error: Stack is not installed. Please install it first.")
        print("Visit: https://docs.haskellstack.org/en/stable/install_and_upgrade/")
        sys.exit(1)
    
    # Build pandoc using Stack
    subprocess.run(["stack", "setup"], check=True)
    subprocess.run(["stack", "install"], check=True)
    
    # Get the installed pandoc version
    result = subprocess.run(["pandoc", "--version"], capture_output=True, text=True, check=True)
    version_line = result.stdout.splitlines()[0]
    pandoc_version = version_line.split()[1]
    print(f"Installed pandoc version: {pandoc_version}")
    
    # Return to the original directory
    os.chdir("..")
    
    return pandoc_version

def build_pandoc_crossref():
    print("Building pandoc-crossref...")
    
    # Clone pandoc-crossref if it doesn't exist
    if not os.path.exists("pandoc-crossref"):
        subprocess.run(["git", "clone", "https://github.com/lierdakil/pandoc-crossref.git"], check=True)
    
    # Change to the pandoc-crossref directory
    os.chdir("pandoc-crossref")
    
    # Build pandoc-crossref using Stack
    subprocess.run(["stack", "setup"], check=True)
    subprocess.run(["stack", "install"], check=True)
    
    # Return to the original directory
    os.chdir("..")
    
    print("pandoc-crossref has been built successfully!")

if __name__ == "__main__":
    sys.exit(main())
