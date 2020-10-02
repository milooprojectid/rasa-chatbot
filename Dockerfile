FROM rasa/rasa
COPY . .

RUN ["rasa", "train"]

EXPOSE 5005
ENTRYPOINT [ "rasa", "run" ]
