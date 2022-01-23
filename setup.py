import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notion_orm",
    version="0.0.1",
    author="Bobby Christopher",
    author_email="rec3college@gmail.com",
    description="A base model for interacting with the Notion API'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/potofpie/notion-orm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'notion-database==20210816.4',
        'python-dotenv==0.17.1'
    ]
)