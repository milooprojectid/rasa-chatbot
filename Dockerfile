FROM rasa/rasa:1.10.18-full
COPY . .

RUN ["rasa", "train"]

EXPOSE 5005
ENTRYPOINT [ "rasa", "run" ]
