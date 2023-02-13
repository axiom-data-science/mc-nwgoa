from setuptools import setup


setup(
    use_scm_version={
        "write_to": "mc_nwgoa/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    },
    entry_points={
        'intake.catalogs': [
            # 'hc_ciofs_cat = mc_nwgoa:ciofs_cat',
            # 'hc_ciofs = mc_nwgoa:ciofs',
            'mc_nwgoa_cat = mc_nwgoa:nwgoa_cat',
            'mc_nwgoa = mc_nwgoa:nwgoa',
        ]
    },
)
