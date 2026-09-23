"""Civilian-mention counts on CNN + MSNBC via the GDELT TV API — reproducible.

Replicates Johnson & Ali (The Nation, 14 Oct 2024; dataset github.com/nationmag/Gaza-Media-Bias):
a "mention" = a 15-second Internet Archive TV clip containing any of the people-terms below.
Run: python3 gdelt_civilian_mentions.py
"""
import json, time, urllib.parse, urllib.request

def ukraine_style(country, adj, bare):
    return [bare, f"civilians in {country}", f"{adj} civilians", f"civilians of {country}", f"{adj} people",
            f"people of {country}", f"people in {country}", f"{adj} refugees", f"refugees of {country}",
            f"refugees in {country}", f"refugees from {country}"]

GAZA = ["palestinian people", "people of gaza", "people in gaza", "civilians in gaza", "palestinian civilians",
        "gazan civilians", "civilians of gaza", "palestinians", "gazans", "palestinian refugees",
        "gazan refugees", "refugees in gaza"]

RUNS = [
    ("Ukraine (The Nation: 29,534)", ukraine_style("ukraine", "ukrainian", "ukrainians"), "20220224000000", "20220603235959"),
    ("Gaza (The Nation: 15,062)", GAZA, "20231007000000", "20240114235959"),
    ("Sudan, same query shape", ukraine_style("sudan", "sudanese", "sudanese"), "20230415000000", "20230723235959"),
    ("Sudan, strict (no bare 'sudanese')", ukraine_style("sudan", "sudanese", "sudanese")[1:], "20230415000000", "20230723235959"),
]

def count(terms, start, end):
    q = "(" + " OR ".join(f'"{t}"' for t in terms) + ") (station:CNN OR station:MSNBC)"
    url = "https://api.gdeltproject.org/api/v2/tv/tv?" + urllib.parse.urlencode(
        {"query": q, "mode": "timelinevol", "format": "json", "datanorm": "raw", "startdatetime": start, "enddatetime": end})
    for _ in range(4):
        try:
            data = json.load(urllib.request.urlopen(url, timeout=90))
            return {s["series"]: int(sum(p["value"] for p in s["data"])) for s in data["timeline"]}
        except Exception:
            time.sleep(6)
    raise RuntimeError("GDELT unreachable")

if __name__ == "__main__":
    for label, terms, s, e in RUNS:
        per = count(terms, s, e)
        print(f"{label}: {per} total {sum(per.values())}")
        time.sleep(6)
