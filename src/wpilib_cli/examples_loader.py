import requests

# TODO: Instead of using their repo, we need to put this in our repo
URL = ("https://raw.githubusercontent.com/wpilibsuite/allwpilib/refs/heads/main/wpilibjExamples/src/main/java/edu/wpi"
       "/first/wpilibj/examples/examples.json")

def fetch_examples_from_github():
    """Fetches WPILib examples from GitHub"""
    res = requests.get(URL)
    res.raise_for_status()
    return res.json()
