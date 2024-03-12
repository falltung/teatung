from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="falltung",
    version="0.1.0",
    keywords=["falltung","canopen"],
    description="Tea is a simple and easy-to-use python package for parsing and analyzing CANopen network data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="falltung",
    author_email="falltung@gmail.com",
    url="https://github.com/falltung/teatung", # github项目连接
    license="MIT License", # 
    packages=[],
    install_requires=[ # 依赖包
        "canopen",
        "pandas", # panda包存在即可
        "numpy >= 1.0", # numpy包要求版本 >1.0
        "Django >= 1.11, != 1.11.1, <= 2", # 要求Django包版本在1.11至2之间，同时不等于1.11.1
        ],
    classifiers=[ # 其他配置项
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    package_data={ # 配置除了python代码外的其他数据、文件，会一起打包
        'data': ['data.csv','*.pkl'],
    }
)
