FROM python:3.11

WORKDIR /jupyter

COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

COPY ./startup /jupyter/config/ipython/profile_default/startup

COPY ./notebooks .

RUN useradd -ms /bin/bash jupyter
RUN chown -R jupyter:jupyter .

USER jupyter
ENTRYPOINT [ "jupyter-lab", "--ip=0.0.0.0", "--NotebookApp.token=''", "--NotebookApp.password=''" ]
