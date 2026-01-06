# Data Properties Overview

## Leveling Data (NAP Benchmarks)

**Description**  
Historic height time series of NAP benchmarks from classical precise leveling campaigns.

**Temporal and Spatial Resolution**  
- Irregular point-based

**Accuracy / Variance**  
- Variance: 

**Reference Frame**  
- Vertical: NAP (meters)  
- Horizontal: RD coordinates (meters)  
- Latitude/longitude available (degrees)

**Data Notes**  
- Some height values are NaN due to missing redefinition coverage or duplicate entries

---

## InSAR Data (Sentinel-1)

**Description**  
InSAR displacement time series derived from Sentinel-1 SAR data for Limburg, provided as radar line-of-sight (LOS) measurements. Two datasets are included: ascending and descending orbits.

**Datasets**  
- `sentinel1_asc_t088_limburg.csv` — Ascending orbit (Midden-2 layer)  
- `sentinel1_dsc_t037_limburg.csv` — Descending orbit (Midden-1 layer)

**Temporal and Spatial Resolution**  
- Irregular point-based, satellite revisit–based 12-day interval 

**Observed Variable**  
- LOS displacement time series (`d_YYYYMMDD`, meters)
- Find correct offset:
  - pnt_height            - Height of scatterer [m] (WGS84)
  - pnt_demheight         - Height of DEM [m] (WGS84), approximately local terrain height
  - pnt_demheight_highres - Height of high-resolution DEM (if available) [m] (WGS84), approximately local terrain height
  - pnt_geoid             - Height of geoid [m] (WGS84)

**Accuracy / Variance**  
- Variance: $\sigma$ 1.2 mm

**Reference Frame**  
- Coordinate system: WGS84 (latitude/longitude in degrees)  
- Heights: Ellipsoidal heights and DEM-based terrain heights (meters)

**Data Notes**  
- Displacements are given in **radar LOS direction**  
- Linear, quadratic, and seasonal displacement model parameters are included per point

---

## GNSS Data

**Description**  
GNSS displacement time series for multiple stations in the Abandoned Mines Limburg case study.

**Temporal and Spatial Resolution**  
- Irregular point-based, typically daily observations

**Observed Variables**  
- North, East, Up coordinates (`n`, `e`, `u`, mm)

**Accuracy / Variance**  
- Station-specific precision provided as standard deviations:
  - `sn`, `se`, `su` (mm)
  - standard deviation horizontal coordinates $\sigma \approx$ 1-2mm
  - standard deviation vertical coordinate $\sigma \approx$ 2-4mm
- Accuracy varies per station and time period

**Reference Frame**  
- Horizontal coordinates:
  - WGS84 latitude/longitude (degrees)
  - RD coordinates (meters)
- Displacements expressed in local topocentric frame (N, E, U)

**Data Notes**  
- Station locations visualized in `GPS_CORS_ZL.png`  
- Time series plots and summaries provided in accompanying files
