# Data Properties Overview

## Leveling Data (NAP Benchmarks)

**Description**  
Historic height time series of NAP benchmarks from classical precise leveling campaigns.

**Temporal Resolution**  
- Irregular (campaign-based; not daily)

**Spatial Resolution**  
- Point-based benchmark locations

**Observed Variable**  
- Height relative to NAP (`hgt`, meters)

**Accuracy / Variance**  
- High accuracy typical of precise leveling  
- Variance not provided; assumed point- and time-dependent

**Reference Frame**  
- Vertical: NAP (meters)  
- Horizontal: RD coordinates (meters)  
- Latitude/longitude available (degrees)

**Noise Characteristics**  
- Low-noise measurements with possible correlated errors  
- Potential step changes due to NAP redefinitions and benchmark instability

**Data Notes**  
- Some height values are NaN due to missing redefinition coverage or duplicate entries

---

## InSAR Data (Sentinel-1)

**Description**  
InSAR displacement time series derived from Sentinel-1 SAR data for Limburg, provided as radar line-of-sight (LOS) measurements. Two datasets are included: ascending and descending orbits.

**Datasets**  
- `sentinel1_asc_t088_limburg.csv` — Ascending orbit (Midden-2 layer)  
- `sentinel1_dsc_t037_limburg.csv` — Descending orbit (Midden-1 layer)

**Temporal Resolution**  
- Irregular, satellite revisit–based (multi-day intervals)

**Spatial Resolution**  
- Point-based persistent and distributed scatterers

**Observed Variable**  
- LOS displacement time series (`d_YYYYMMDD`, meters)

**Accuracy / Variance**  
- Quality depends on:
  - Ensemble coherence (`pnt_enscoh`)
  - Amplitude consistency (`pnt_ampconsist`)
  - Number of averaged pixels (`pnt_ds_nr_neighbors`)
- Variance not explicitly provided

**Reference Frame**  
- Coordinate system: WGS84 (latitude/longitude in degrees)  
- Heights: Ellipsoidal heights and DEM-based terrain heights (meters)

**Noise Characteristics**  
- Mixed noise sources including:
  - Atmospheric phase delay
  - Temporal decorrelation
  - Orbit and DEM errors
- Noise level varies per point and can be assessed using coherence metrics

**Data Notes**  
- Displacements are given in **radar LOS direction**  
- Linear, quadratic, and seasonal displacement model parameters are included per point


---

## GNSS Data

**Description**  
GNSS displacement time series for multiple stations in the Abandoned Mines Limburg case study.

**Temporal Resolution**  
- Regular, typically daily observations

**Spatial Resolution**  
- Point-based GNSS station locations

**Observed Variables**  
- North, East, Up coordinates (`n`, `e`, `u`, mm)

**Accuracy / Variance**  
- Station-specific precision provided as standard deviations:
  - `sn`, `se`, `su` (mm)
- Accuracy varies per station and time period

**Reference Frame**  
- Horizontal coordinates:
  - WGS84 latitude/longitude (degrees)
  - RD coordinates (meters)
- Displacements expressed in local topocentric frame (N, E, U)

**Noise Characteristics**  
- Combination of:
  - White noise (measurement noise)
  - Temporally correlated noise (e.g. multipath, monument motion)
- Noise properties may be inferred from time series residuals

**Data Notes**  
- Station locations visualized in `GPS_CORS_ZL.png`  
- Time series plots and summaries provided in accompanying files
