# Public research repository roadmap

The profile becomes substantially stronger when visitors can inspect two to six focused, reproducible repositories. Build depth before quantity.

| Priority | Suggested repository | Public value | Minimum first release |
|---:|---|---|---|
| 1 | <code>wrfchem-india-toolkit</code> | Demonstrates your strongest modelling and Python skills | Evaluation notebook, configuration guide, sample NetCDF subset, maps and tests |
| 2 | <code>compound-heat-pm25</code> | Connects directly to the ERL paper | Reproducible indicator calculation, synthetic example, key figure workflow |
| 3 | <code>aerosol-climate-diagnostics</code> | Shows radiative-forcing and heat-extreme expertise | ΔERF, ΔT, efficiency and regional-mask utilities with examples |
| 4 | <code>pm25-health-equity</code> | Demonstrates policy and environmental-justice impact | District aggregation, rural–urban comparisons and health-function interface |
| 5 | <code>india-inmap-support</code> | Shows reduced-complexity modelling collaboration | Input-preparation notes, model-evaluation utilities and reproducible plots |
| 6 | <code>earth-data-visualization</code> | Provides an accessible code portfolio | Publication-quality Cartopy, Xarray and geospatial plotting recipes |

## Release standard

Every public repository should have:

1. one-sentence scientific purpose at the top;
2. a visual result within the first screen;
3. a <code>CITATION.cff</code>;
4. an explicit license;
5. a reproducible environment;
6. a five-minute quick start;
7. documented input and output schemas;
8. a small test or validation dataset;
9. limitations and data-governance notes; and
10. a versioned release linked to Zenodo when mature.

## Suggested profile repository topics

<code>atmospheric-science</code>, <code>air-quality</code>, <code>climate-extremes</code>, <code>wrf-chem</code>, <code>environmental-health</code>, <code>geospatial-analysis</code>, <code>earth-system-science</code>, <code>research-profile</code>

## After publishing

Replace the username placeholder by running:

    python scripts/configure_profile.py --username Dewashishtiwari

Then pin the most mature repositories on the GitHub profile, ordered by scientific narrative rather than chronology.

