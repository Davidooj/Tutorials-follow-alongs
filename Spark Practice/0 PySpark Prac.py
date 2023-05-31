import pyspark
import pandas as pd
from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("Agg").getOrCreate()

df = spark.read.csv("Test3.csv", header = True, inferSchema = True)

spark

# Starting a cluster and opening a df