# Spatial Join slides

This repository contains short presentationan on **Spatial joins**, developed using R Markdown and xaringan.

The slides give an overview on how spatial joins can be used to answer spatial planning questions. Here it is demonstrated using tram stop data from Greater Manchester.

---

## Objectives

- Explain what a spatial join is  
- Demonstrate the spatial join process
- Apply the method to a real-world example  
- Show equivalent workflows in **R (sf)** and **Python (GeoPandas)**  

---

## Data
- **GM Metrolink stops** (points)  
- **Local Authority District boundaries** (polygons)

Sources:
- [data.gov.uk](https://www.data.gov.uk/dataset/55576216-cd1d-4e2b-adcf-c87c07473373/gm-metrolink-network)
- [ONS Geography](https://geoportal.statistics.gov.uk/documents/ons::local-authority-districts-counties-and-unitary-authorities-december-2022-map-in-the-uk/about?path=)

Raw geospatial data is not included in this repository. Please refer to the sources above to download the original datasets.

---

## Relevant files

```text
Spatial_join.Rmd      # Source slide deck
Spatial_join.html     # Rendered presentation
style.css             # Custom styling
images/               # Figures used in slides
geodata/              # spatial data used in the example
```
## License
This work is licensed under a Creative Commons Attribution 4.0 International (CC BY 4.0) License.
https://creativecommons.org/licenses/by/4.0/
