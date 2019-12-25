FROM python:3.7.2-slim
COPY . /machinelearningpipeline

WORKDIR /machinelearningpipeline

RUN pip install -r requirements.txt

CMD echo "run any .py file for example python src/miners/imdb_miner.py"