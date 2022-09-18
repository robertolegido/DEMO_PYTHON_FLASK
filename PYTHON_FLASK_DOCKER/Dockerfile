# start by pulling the python image
FROM python:3.8.5-alpine
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
# switch working directory
WORKDIR /app
# install dependencies and packages defined in requirements
RUN pip install -r requirements.txt
# copy every content from local file to the image
COPY . /app
# run python in container and execute rest.py scritp 
ENTRYPOINT ["python"]
CMD ["rest.py"]
