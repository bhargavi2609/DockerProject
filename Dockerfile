FROM alpine

RUN apk add --no-cache python3

ADD /Limerick.txt /home/data/Limerick.txt
ADD /IF.txt /home/data/IF.txt
ADD /main.py /home/main.py
RUN mkdir -p /home/output/
CMD ["/home/main.py"]
ENTRYPOINT ["python3"]