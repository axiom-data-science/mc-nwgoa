from setuptools import setup


setup(
    use_scm_version={
        "write_to": "mc_nwgoa/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    },
    entry_points={
        'intake.catalogs': [
            'nwgoa_cat = mc_nwgoa:cat',
            'nwgoa_data = mc_nwgoa:data'
        ]
    },
)
