FROM python:3.7-slim

ENV PATH="/home/myuser/.local/bin:${PATH}"

RUN useradd -m myuser
USER myuser
WORKDIR /home/worker

RUN pip install --user --upgrade pip
COPY --chown=myuser:myuser requirements.txt requirements.txt
#COPY requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
#RUN pip install  -r requirements.txt


COPY --chown=myuser:myuser . .
#COPY  . .

CMD ["python3","my_ssh.py"]


