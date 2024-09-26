from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import StandardScaler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.feature import VectorAssembler
import numpy as np, pandas as pd
import matplotlib.pyplot as plt, seaborn as sns
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

# Feature Engineering
df = spark.sql("SELECT * FROM TestedTable5")
df = df.sort(df.release_date.desc())
df_stream = df
df = df.drop('order_id','id',
 'explicit',
  'mode',
 'release_date',
 'id_artists',
 'time_signature',
 'duration_ms',
 'timestamp')

assembler = VectorAssembler(inputCols=['danceability',
 'energy', 'loudness', 'speechiness', 'acousticness',
 'instrumentalness', 'liveness', 'valence', 'tempo'], outputCol='features')
assembled_data = assembler.setHandleInvalid("skip").transform(df)

#Scaling
scale = StandardScaler(inputCol='features',outputCol='standardized')
data_scale = scale.fit(assembled_data)
df = data_scale.transform(assembled_data)

#K-Means Clustering
sihouette_score = []
evaluator = ClusteringEvaluator(predictionCol='prediction',featuresCol='standardized',
                                metricName='silhouette',distanceMeasure='squaredEuclidean')
KMeans_algo = KMeans(featuresCol='standardized',k=3)
KMeans_fit = KMeans_algo.fit(df)
output_df = KMeans_fit.transform(df)

###Recommendation System
































