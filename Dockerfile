FROM python:3

RUN useradd --user-group --create-home --shell /bin/false app

ARG APP_NAME
ENV HOME=/home/app

COPY . ${HOME}/${APP_NAME}

RUN pip install --no-cache-dir -r ${HOME}/${APP_NAME}/requirements.txt

USER app

WORKDIR ${HOME}/${APP_NAME}

CMD [ "python", "./beholder.py" ]
