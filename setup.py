from distutils.core import setup
import os

package_data = []
BASE_DIR = os.path.dirname(__file__)
walk_generator = os.walk(os.path.join(BASE_DIR, "project_template"))
paths_and_files = [(paths, files) for paths, dirs, files in walk_generator]
for path, files in paths_and_files:
    prefix = path[len("project_template/"):]
    if files:
        package_data.append(os.path.join(prefix, "*.*"))

setup(
    name="armstrong.templates.standard",
    version="1.0.1",
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
    package_data={
        "armstrong.templates.standard": package_data,
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
