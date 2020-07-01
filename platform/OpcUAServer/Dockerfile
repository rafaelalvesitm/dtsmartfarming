FROM python:3

ADD server.py /

RUN pip install requests && \
pip install opcua

CMD [ "python", "./server.py" ]