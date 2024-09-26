import pandas as pd
from kafka import KafkaProducer
from datetime import datetime
from json import dumps
import time
import random
import numpy as np
import os
os.chdir("d:")

## start kafka server (go to C:/kafka/bin/windows/cmd ->runzoo and then run)
KAFKA_TOPIC_NAMES_CONS = "songTopic"
KAFKA_BOOTSTRAP_SERVERS_CONS = "localhost:9092"

if __name__ == "__main__":
    print("Kafka Producer Application Started ...")

    kafka_producer_obj = KafkaProducer(bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS_CONS,
                                       api_version=(0, 10, 2), # lowest api value safest
                                       value_serializer = lambda x: dumps(x).encode('utf-8'),
                                       batch_size = 1, acks = "all", max_block_ms = 1000) # this last line might be
    # optional


    filepath = r'D:\Forecasting\Epiconik NG\Data\spotify_1_2Msongs\tracks_features.csv'

    songs_df = pd.read_csv(filepath, nrows=100)
    print(songs_df.head(5))
    #choose songs that are popular, threshold 50, tunable
    # songs_df = songs_df[songs_df['popularity']>50]

    songs_df['order_id'] = np.arange(len(songs_df))
    print("Done aranging ids")
    songs_df['artists']= songs_df['artists'].str.replace('[^a-zA-Z]','')
    print("Done replacing chars in artists name")
    songs_df['artist_ids'] = songs_df['artist_ids'].str.replace('[^a-zA-Z]','')
    print("Done replacing chars in artists ids")

    song_list = songs_df.to_dict(orient="records")

    message_list = []
    message = None

    for message in song_list:
        message_fields_value_list = []

        message_fields_value_list.append(message["order_id"])
        message_fields_value_list.append(message["id"])
        message_fields_value_list.append(message["name"])
        # message_fields_value_list.append(message["popularity"])
        message_fields_value_list.append(message["duration_ms"])
        message_fields_value_list.append(message["explicit"])
        message_fields_value_list.append(message["artists"])
        message_fields_value_list.append(message["artist_ids"])
        message_fields_value_list.append(message["release_date"])
        message_fields_value_list.append(message["danceability"])
        message_fields_value_list.append(message["energy"])
        message_fields_value_list.append(message["key"])
        message_fields_value_list.append(message["loudness"])
        message_fields_value_list.append(message["mode"])
        message_fields_value_list.append(message["speechiness"])
        message_fields_value_list.append(message["acousticness"])
        message_fields_value_list.append(message["instrumentalness"])
        message_fields_value_list.append(message["liveness"])
        message_fields_value_list.append(message["valence"])
        message_fields_value_list.append(message["tempo"])
        message_fields_value_list.append(message["time_signature"])


        message = ",".join(str(v) for v in message_fields_value_list)
        print("Message Type: ", type(message))
        print("message: ",message)
        kafka_producer_obj.send(KAFKA_TOPIC_NAMES_CONS,message)
        time.sleep(1)

    print("Kafka Producer Application Completed.")














