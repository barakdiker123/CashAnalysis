setup(
    name="server-analysis",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/barakdiker123/CashAnalysis",
    author="Barak Diker",
    author_email="barakdiker@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    # install_requires=["feedparser", "html2text", "importlib_resources", "typing"],
    entry_points={
        "console_scripts": ["realpython=first_try_sidebar_demo.__main__:main"]
    },
)