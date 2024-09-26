import os
os.environ["SPARK_HOME"] = r"C:\spark\spark-3.2.0-bin-hadoop3.2"
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,' \
                                    'org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,' \
                                    'org.apache.kafka:kafka-clients:2.7.0'
# import findspark
# findspark.init(r"C:\spark\spark-3.2.0-bin-hadoop3.2")

spark_version = '3.2.0'
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import Normalizer, StandardScaler
import random
import time
import numpy



"""
Currently unable to run this file as it will not allow for the file to be run. spark-submit issue. 
"""

if __name__ == "__main__":
    kafka_bootstrap_servers = 'localhost:9092'
    kafka_topic_name = "songTopic"


    #Initialize the spark sessions
    spark = SparkSession.builder.appName("Spotify Streaming Recommendation System")\
        .master("local[*]").getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    #Retrieve from the kafka topic
    songs_df = spark.readStream.format("kafka")\
        .option("kafka.bootstrap.servers", kafka_bootstrap_servers)\
        .option("subscribe",kafka_topic_name)\
        .option("startingOffsets","latest")\
        .load()

    songs_df1 = songs_df.selectExpr("CAST(value as STRING","timestamp")

    songs_schema_string = "order_id INT,id STRING, name STRING,duration_ms DOUBLE, explicit INT, " \
                               + "artists STRING, artist_ids STRING, release_date STRING, " \
                               + "danceability DOUBLE," \
                               + "energy DOUBLE, key INT, loudness DOUBLE, " \
                               + "mode INT," \
                               + "speechiness DOUBLE," \
                               + "acousticness DOUBLE, instrumentalness DOUBLE, liveness DOUBLE, " \
                               + "valence DOUBLE, tempo DOUBLE, time_signature DOUBLE"

    songs_df2 = songs_df1\
        .select(from_csv(col("value"),songs_schema_string)\
                .alias("song"),"timestamp")
    songs_df3 = songs_df2.select("song.*", "timestamp")

    #Create a schema that matches producer. Add timestamp as data arrives.
    #Create a view with processign time 5 seconds in append mode to get all data from producer
    songs_df3.createOrReplaceTempView("song_find")
    song_find_text = spark.sql("SELECT * FROM song_find")
    songs_agg_write_stream = song_find_text.writeStream\
        .trigger(processingTime="5 seconds")\
        .outputMode("append").option("truncate","false")\
        .queryName("testedTable5").start()

    songs_agg_write_stream.awaitTermination(1)


