"""
mc-nwgoa: `model_catalogs` Catalog for NWGOA model.
"""


from importlib.metadata import PackageNotFoundError, version


try:
    __version__ = version("mc-nwgoa")
except PackageNotFoundError:
    # package is not installed
    pass



import intake
import os
here = os.path.abspath(os.path.dirname(__file__))

# # the catalog is a YAML file in the same directory as this init file
# cat = intake.open_catalog(os.path.join(here, 'nwgoa_cat.yaml'), ttl=None)
# data = cat.nwgoa()  # <- note the parentheses

# after installation, this will be available as intake.cat.nwgoa_cat, with one entry, nwgoa
# and intake.cat.nwgoa_data, which is a data source.
# intake.cat.nwgoa_cat.nwgoa and intake.cat.nwgoa_data are identical.


# # testing
# cbofs = intake.open_catalog(os.path.join(here, 'cbofs.yaml'), ttl=None)
# ciofs = intake.open_catalog(os.path.join(here, 'ciofs.yaml'), ttl=None)


# # the catalog is a YAML file in the same directory as this init file
# ciofs_cat = intake.open_catalog(os.path.join(here, 'ciofs.yaml'), ttl=None)
# ciofs = ciofs_cat.ciofs()  # <- note the parentheses

nwgoa_cat = intake.open_catalog(os.path.join(here, 'nwgoa.yaml'), ttl=None)
nwgoa = nwgoa_cat.nwgoa()  # <- note the parentheses

