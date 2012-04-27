from distutils.core import setup

setup(
    name="armstrong.templates.standard",
    version="1.0.0",
    description="Provides a basic project template for an Armstrong project",
    long_description=open("README.rst").read(),
    author='Texas Tribune & Bay Citizen',
    author_email='dev@armstrongcms.org',
    packages=[
        "armstrong.templates.standard",
    ],
    package_dir={
        "armstrong.templates.standard": "project_template",
    },
    namespace_packages=[
        "armstrong",
        "armstrong.templates",
        "armstrong.templates.standard",
    ],
    entry_points={
        "armstrong.templates": [
            "standard = armstrong.templates.standard",
        ],
    },
)
