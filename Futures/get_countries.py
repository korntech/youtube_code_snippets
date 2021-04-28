
from concurrent import futures
import random
import time

import pandas as pd
import requests

BASE_URL = "https://restcountries.eu/rest/v2"


country_list = pd.read_csv("country_list.csv")
country_list = country_list["name"].to_list()
country_list = random.sample(country_list, 10)


def get_country(name: str) -> str:
    url = f"{BASE_URL}/name/{name}"
    try:
        resp = requests.get(url, timeout=2)
    except Exception as e:
        return f"Failed for: {name} due to {e}."
    else:
        with open(f"{name}.txt", "w") as fout:
            fout.write(resp.text)
    return name


def get_all_countries(country_list: list[str]) -> int:

    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(get_country, name): name for name in country_list}
        print(future_to_url)
        for count, future in enumerate(futures.as_completed(future_to_url), 1):
            res = future.result()
            print(res)

    return count


if __name__ == "__main__":
    t0 = time.perf_counter()
    get_all_countries(country_list)
    elapsed = time.perf_counter() - t0
    print(f"Execution took {elapsed:.2f} seconds.")
