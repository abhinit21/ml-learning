FROM ubuntu:latest
LABEL authors="surak"

ENTRYPOINT ["top", "-b"]