# 1. Load CSVs and Create Temp Views
restaurantsDF = spark.read.option("header", "true").csv("/path/to/ubereats_restaurants.csv")
menusDF = spark.read.option("header", "true").csv("/path/to/ubereats_restaurant-menus.csv")

restaurantsDF.createOrReplaceTempView("ubereats_restaurants")
menusDF.createOrReplaceTempView("ubereats_menus")

# 2. State-wise High Rated Restaurants (requires address splitting)
from pyspark.sql.functions import split, size, col

split_address = split(restaurantsDF['full_address'], ', ')
popular_restaurant_with_state = restaurantsDF.filter((col('score') >= 4.5) & (size(split_address) == 4)) \
    .withColumn('state', split_address.getItem(2)) \
    .filter((col('state').isNotNull()) & (col('state') != ''))

state_with_popular_restaurant = popular_restaurant_with_state.groupBy("state") \
    .count().orderBy(col("count").desc())

state_with_popular_restaurant.show(10)
