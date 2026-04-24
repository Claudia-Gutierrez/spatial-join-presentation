# Spatial Join slides

This repository contains an overview of the **spatial joins**, developed using R Markdown and xaringan.

The presentation demonstrates how spatial joins can be used to answer planning questions using tram stop data from Greater Manchester.

---

## Objectives

- Explain what a spatial join is  
- Demonstrate the spatial join process
- - Apply the method to a real-world example  
- Show equivalent workflows in **R (sf)** and **Python (GeoPandas)**  

---

## Data
- **GM Metrolink stops** (points)  
- **Local Authority District boundaries** (polygons)  
Sources:
- data.gov.uk  
- ONS Geography  

---

## Repository structure

```text
Spatial_join.Rmd      # Source slide deck
Spatial_join.html     # Rendered presentation
style.css             # Custom styling
images/               # Figures used in slides
geodata/              # spatial data used in the example
