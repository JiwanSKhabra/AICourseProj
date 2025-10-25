import json, csv

with open("anemoculi.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

headers = raw["headers"]                    # ["id","type","mid","level","lng","lat","meta"]
rows = raw["data"]                          # list of lists

# Build dicts for easy access
records = [dict(zip(headers, r)) for r in rows]

# keep only Anemoculus type ("o5")
records = [r for r in records if str(r.get("type","")).lower() == "o5"]

out = []
for r in records:
    out.append({
        "id": r["id"],
        "name": "Anemoculus",
        "lon": float(r["lng"]),
        "lat": float(r["lat"]),
    })

with open("data/mondstadt_anemoculi.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id","name","lon","lat"])
    w.writeheader()
    w.writerows(out)

print(f"Wrote {len(out)} rows to data/mondstadt_anemoculi.csv")
