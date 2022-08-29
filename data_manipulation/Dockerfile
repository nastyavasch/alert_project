FROM python:3.7




WORKDIR /home/anastasiya/Documents/GitHub/alert_project




COPY requirements.txt ./

COPY ./data .




RUN pip install --no-cache-dir -r requirements.txt




COPY . /home/anastasiya/Documents/GitHub/alert_project




CMD [ "python", "./main.py" ]