FROM python:3.6.8

ARG uid=1000
ARG user=developer

RUN useradd -G www-data,root -u $uid -d /home/$user $user
RUN mkdir -p /home/$user && chown -R $user:$user /home/$user

WORKDIR /app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

USER $user

CMD ["python3", "myapp/manage.py", "runserver", "0.0.0.0:8000"]