FROM python

LABEL mantainer="crispedrani@gmail.com"

COPY src ./src

COPY requirements.txt .

RUN pip3 install update 

RUN cd src & ls src

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000