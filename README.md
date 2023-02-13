mc-nwgoa
==============================
[![Build Status](https://github.com/axiom-data-science/mc-nwgoa/workflows/Tests/badge.svg)](https://github.com/axiom-data-science/mc-nwgoa/actions)
[![codecov](https://codecov.io/gh/axiom-data-science/mc-nwgoa/branch/main/graph/badge.svg)](https://codecov.io/gh/axiom-data-science/mc-nwgoa)
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python Package Index](https://img.shields.io/pypi/v/mc-nwgoa.svg?style=for-the-badge)](https://pypi.org/project/mc-nwgoa)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/mc-nwgoa.svg?style=for-the-badge)](https://anaconda.org/conda-forge/mc-nwgoa)

A `model_catalogs` catalog for NWGOA.

Metadata from catalog file is applied to model dataset on the fly.

--------

<p><small>Project based on the <a target="_blank" href="https://github.com/jbusecke/cookiecutter-science-project">cookiecutter science project template</a>.</small></p>


# Installation

If you need to install these yourself, you can with PyPI:

```
pip install mc-goods
```

or with conda-forge:

```
conda install -c conda-forge mc-goods
```


# How to Use

Install [`model_catalogs`](https://github.com/NOAA-ORR-ERD/model_catalogs) and install this package to get access to these catalogs through the default `intake` catalog.

```
import intake
import model_catalogs as mc

# see the catalog and dataset this way
intake.cat.mc_nwgoa_cat  # catalog
intake.cat.mc_nwgoa      # source

# Use model_catalogs to apply metadata to model output
source = mc.open_catalog(intake.cat.mc_nwgoa_cat)["nwgoa"]
# access model output
ds = source.to_dask()

# if you want to deal with just one source, a shortcut to ds:
ds = mc.transform_source(intake.cat.mc_nwgoa).to_dask()
```