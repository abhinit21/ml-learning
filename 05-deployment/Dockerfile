FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["flask_app.py", "script.py", "model.bin", "dv.bin", "./"]

EXPOSE 9090

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9090", "flask_app:app"]

LABEL authors="abhint21"