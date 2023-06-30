FROM python:3.10-slim-buster

LABEL maintainer="Alex"

ARG UID=10000
ARG GID=10000
ENV UID=${UID}
ENV GID=${GID}
# тут ми сворюємо користувача з ім'м docker_user, який не є рутом, і його UID за
# замовченням буде 1000 (раніше тут було ARG UID=1000 ENV UID=${UID}), він може бути
# замінений при старті контейнера передачою змінної або в файлі docker-compose.yaml
# або як аргумент команди docker
RUN useradd -m -u $UID docker_user
USER docker_user

WORKDIR /home/docker-user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3","-m", "bot.main" ]


