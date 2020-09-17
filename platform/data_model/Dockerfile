FROM python:3

COPY / /

RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install requests

CMD [ "python","-u", "./setup.py" ]