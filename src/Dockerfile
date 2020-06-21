FROM python:3.7-slim
MAINTAINER "Jayant Mishra"
COPY . /check_out_system_git
WORKDIR /check_out_system_git
ENV PYTHONPATH /check_out_system_git
RUN pip install -r src/requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "src/app.py" ]
