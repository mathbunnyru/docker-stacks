# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
from dataclasses import dataclass, field
from typing import Optional, List
from taggers import TaggerInterface, \
    SHATagger, \
    PythonVersionTagger, \
    JupyterNotebookVersionTagger, JupyterLabVersionTagger, JupyterHubVersionTagger, \
    RVersionTagger, TensorflowVersionTagger, JuliaVersionTagger, \
    SparkVersionTagger, HadoopVersionTagger, JavaVersionTagger


@dataclass
class ImageDescription:
    parent_image: Optional[str]
    taggers: List[TaggerInterface] = field(default_factory=list)


ALL_IMAGES = {
    "base-notebook": ImageDescription(
        parent_image=None,
        taggers=[
            SHATagger,
            PythonVersionTagger,
            JupyterNotebookVersionTagger, JupyterLabVersionTagger, JupyterHubVersionTagger
        ]
    ),
    "minimal-notebook": ImageDescription(
        parent_image="base-notebook"
    ),
    "scipy-notebook": ImageDescription(
        parent_image="minimal-notebook"
    ),
    "r-notebook": ImageDescription(
        parent_image="minimal-notebook",
        taggers=[RVersionTagger]
    ),
    "tensorflow-notebook": ImageDescription(
        parent_image="scipy-notebook",
        taggers=[TensorflowVersionTagger]
    ),
    "datascience-notebook": ImageDescription(
        parent_image="scipy-notebook",
        taggers=[JuliaVersionTagger]
    ),
    "pyspark-notebook": ImageDescription(
        parent_image="scipy-notebook",
        taggers=[SparkVersionTagger, HadoopVersionTagger, JavaVersionTagger]
    ),
    "allspark-notebook": ImageDescription(
        parent_image="pyspark-notebook",
        taggers=[RVersionTagger]
    )
}