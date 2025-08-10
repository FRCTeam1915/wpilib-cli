from typing import List, Dict

import requests


# TODO: Implement a function to fetch examples from GitHub
def fetch_examples_from_github() -> List[Dict]:
    examples_url = "None"
    res = requests.get(examples_url)
    res.raise_for_status()
    return res.json()
