# Copyright 2023 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

import setuptools


_deps = [
    "transformers>=4.34.0",
    "datasets[audio]>=2.14.5",
    "jax>=0.4.13",
    "flax>=0.7.2",
    "optax",
    "evaluate",
    "jiwer",
    "torch",
    "torchdata",
    "tokenizers",
]

_extras_dev_deps = [
    "black~=23.1",
    "isort>=5.5.4",
    "ruff>=0.0.241,<=0.0.259",
]

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# read version
with open(os.path.join(here, "distil_whisper", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"')
            break
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="distil_whisper",
    version=version,
    description="Toolkit for distilling OpenAI's Whisper model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=_deps,
    extras_require={
        "dev": [_extras_dev_deps],
    },
)
