#!/usr/bin/env python
# coding: utf-8

# ## Spatial Join




import geopandas as gpd
import pandas as pd
from pathlib import Path





base = Path(r"C:/Your_path")

boroughs = gpd.read_file(base / "geodata/GM_lad.gpkg")
stops = gpd.read_file(base / "geodata/Metrolink_Stops_Functional.json")

print(boroughs.crs)
print(stops.crs)


# Set Coordinate Reference System to OSGB36 / British National Grid



boroughs = boroughs.to_crs(epsg=27700)
stops = stops.to_crs(epsg=27700)


# Spatial join: assign each stop to the borough it falls within




stops_in_borough = gpd.sjoin(
    stops,
    boroughs,
    how="inner",
    predicate="within"
)

stops_in_borough.head()


# Count tram stops per borough



borough_counts = (
    stops_in_borough
    .groupby("LAD22NM")
    .size()
    .reset_index(name="n_stops")
    .sort_values("n_stops", ascending=False)
)


# Boroughs not served by the tram network




not_served = (
    boroughs[["LAD22NM"]]
    .merge(
        stops_in_borough[["LAD22NM"]].drop_duplicates(),
        on="LAD22NM",
        how="left",
        indicator=True
    )
    .query('_merge == "left_only"')
    [["LAD22NM"]]
)


# Inspect outputs



print("\nStops joined to boroughs:")
print(stops_in_borough[["name", "stationCode", "LAD22NM"]].head())

print("\nStops per borough:")
print(borough_counts)

print("\nBoroughs not served:")
print(not_served)





