#!/usr/bin/env python3
# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import json
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).parent.resolve()


def generate_matrix() -> list[dict[str, Any]]:
    dockerfiles = sorted(THIS_DIR.glob("*.dockerfile"))
    runs_on = ["ubuntu-24.04", "ubuntu-22.04-arm"]

    matrix = []
    for dockerfile in dockerfiles:
        dockerfile_name = dockerfile.name
        for run in runs_on:
            if dockerfile_name == "oracledb.dockerfile" and run == "ubuntu-22.04-arm":
                continue
            dockerfile_lines = dockerfile.read_text().splitlines()
            base_image = [
                line for line in dockerfile_lines if line.startswith("ARG BASE_IMAGE=")
            ][0][15:]
            base_image_short = base_image[base_image.rfind("/") + 1 :]
            # Handling a case of `docker.io/jupyter/base-notebook:notebook-6.5.4` image
            if ":" in base_image_short:
                base_image_short = ""
            matrix.append(
                {
                    "dockerfile": dockerfile_name,
                    "runs-on": run,
                    "platform": "x86_64" if run == "ubuntu-24.04" else "aarch64",
                    "parent-image": base_image_short,
                }
            )
    return matrix


if __name__ == "__main__":
    print("matrix=" + json.dumps(generate_matrix()))
