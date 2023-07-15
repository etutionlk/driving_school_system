# syntax=docker/dockerfile:1
FROM python:3.11.4-bullseye

ARG RUNTIME_USER="appuser"
RUN groupadd -g 1010 -r ${RUNTIME_USER} && useradd -rm -d $HOME -s /bin/bash -g ${RUNTIME_USER} -G sudo -u 1001 ${RUNTIME_USER}
USER ${RUNTIME_USER}

ARG HOME=/home/${RUNTIME_USER}
ENV PYTHONPATH ${HOME}/app:${HOME}/.local/bin:$HOME/.local/lib/python3.11/site-packages

ENV PATH ${HOME}/.local/bin:${PATH}
WORKDIR ${HOME}

RUN export  PYTHONPATH=$PYTHONPATH:$HOME/.local/lib/python3.11/site-packages
ENV PATH="${HOME}/.local/bin:${PATH}"

COPY --chown=${RUNTIME_USER}:${RUNTIME_USER} ./requirements.txt .

RUN python3 -m pip install -r requirements.txt

RUN mkdir -p ${HOME}/app
COPY --chown=${RUNTIME_USER}:${RUNTIME_USER} . ./app
WORKDIR ${HOME}/app

EXPOSE 5000
CMD [ "flask", "--app", "application", "run" ]

#ENTRYPOINT ["tail"]
#CMD ["-f", "/dev/null"]