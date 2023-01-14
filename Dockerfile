FROM centos7_python3:v0.1
COPY . /git/distqcpbypython
WORKDIR /git/distqcpbypython
EXPOSE 8081
RUN yum install -y python-devel zlib-devel libjpeg-turbo-devel
RUN pip3 install -r requirements.txt -i https://pypi.douban.com/simple/
CMD ["python3","mainflask.py"]
