from setuptools import setup


dependencies = [
    "beautifulsoup4==4.9.3",
    "marshmallow==3.13.0",
    "requests==2.25.0",
    "urllib3==1.26.2",
]

package_data = {
    "scrap.resources": ["config.ini"],
}

packages = [
    "controller",
    "functions",
    "log",
    "model",
    "schemas",
    "scrap",
    "scrap.resources",
    "view",
]

platform = ["any"]

long_description = "Web Scraping dollar values of Argentine Banks"

manifest = dict(
    name="dollar-exchange-rate-argentine-banks",
    version="1.0.0",
    author="DobleRR - Rodrigo Quispe",
    author_email="rrquispezabala@gmail.com",
    description="Dollar Exchange Rate Argentine Banks",
    url="https://github.com/RRodriQZ",
    license="MIT",
    python_requires=">=3.6, <4",
    keywords="dollar scraping argentine banks",
    install_requires=dependencies,
    package_data=package_data,
    packages=packages,
    platforms=platform,
    long_description=long_description,
    long_description_content_type="text/markdown",
)


if __name__ == "__main__":
    setup(**manifest)
