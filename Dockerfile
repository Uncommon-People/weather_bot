FROM python:3
LABEL authors="dimas"
RUN apt-get update && apt-get upgrade -y
RUN mkdir /project
COPY . /project
WORKDIR /project
EXPOSE 8080
RUN pip install --upgrade pip
RUN pip install aiogram
RUN pip install requests
RUN python3 main.py
CMD ["py", "main"]