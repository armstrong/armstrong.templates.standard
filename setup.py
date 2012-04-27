from distutils.core import setup

setup(
    name="armstrong.templates.standard",
    version="0.1alpha.0",
    packages=[
        "armstrong.templates.standand",
    ],
    package_dir={
        "armstrong.templates.standard": "project_template",
    },
    namespace_packages=[
        "armstrong",
        "armstrong.templates",
        "armstrong.templates.standard",
    ],
)
