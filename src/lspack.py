#!/usr/bin/env python3
import os
import sys
import shutil
import requests
import tarfile
import hashlib

packdir = os.path.expanduser("~/.lspack/packages")
cachedir = os.path.expanduser("~/.lspack/cache")
index_url = "https://lspack.com/lspack/index.json"

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
cyan = '\033[96m'
reset = '\033[0m'

def colored(text, color):
  return f"{color}{text}{reset}"

def download_package(package_name, version, url):
  print(f"Downloading{colored(package_name, yellow)}...")
  package_url = f"{url}/{package_name}/{version}.tar.gz"
  response = requests.get(package_url, stream=True)
  if response.status_code == 200:
    cache_file = os.path.join(cachedir, f"{package_name}_{version}.tar.gz")
    with open(cache_file, 'wb') as f:
      for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)
    print(f"{colored(package_name, yellow)}")