FROM python:alpine3.7
MAINTAINER "Jayant Mishra"
COPY . /checkout_system
WORKDIR /checkout_system
ENV PYTHONPATH /checkout_system
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
