import csv
import time

import click
import requests
from requests.exceptions import RequestException, Timeout
from rich import print

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option("-i", "path", default="data/urls.csv", help="Input CSV file containing urls.", metavar="PATH")
def main(path):
    with open(path, "r") as f:
        csv_reader = csv.reader(f, delimiter="|")

        for name, url in csv_reader:
            start_time = time.time()
            try:
                resp = requests.get(url, timeout=3)
                print(f'"{name}", HTTP {resp.status_code}, time {time.time() - start_time:.2f} seconds')
            except Timeout:
                print(f"Skipping {url}")
            except RequestException as e:
                print(f'"{name}", Error: {e}')


if __name__ == "__main__":
    main()
