#base
FROM python:3.14.6

#working directory
WORKDIR /metflix

#copy requirements file
COPY . /metflix

#run pip install
RUN pip install -r requirements.txt

#port 
EXPOSE 8000

#run server
CMD ["python", "./manage.py", "runserver", "0.0.0.0:8000"]

