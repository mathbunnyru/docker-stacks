ARG BASE_IMAGE=quay.io/jupyter/base-notebook
FROM $BASE_IMAGE

# Install the Dask dashboard
RUN mamba install --yes 'dask-labextension' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Dask Scheduler port
EXPOSE 8787
