FROM python:latest
 
WORKDIR /alpha
COPY . /alpha
 
RUN pip install -r requirements.txt
 
CMD ["bash", "run.sh"]
