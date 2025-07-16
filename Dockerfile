FROM ubuntu:latest
LABEL authors="ludod"

ENTRYPOINT ["top", "-b"]