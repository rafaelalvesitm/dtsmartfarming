FROM python:3

ADD weather.py /

RUN pip install requests && \
pip install opcua && \
pip install apscheduler

CMD [ "python", "./weather.py" ]