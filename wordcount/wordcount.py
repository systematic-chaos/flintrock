from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("DemoDeploy").setMaster("spark://ec2-3-249-190-116.eu-west-1.compute.amazonaws.com:7077")
sc = SparkContext(conf=conf)

print('==== DEMO DEPLOY ====')

text = ['Hadoop MapReduce, a disk-based big data processing engine, is being replaced by a new generation of memory-based processing frameworks, the most popular of which is Spark.', 'Spark supports Scala, Java, Python, and R.']
rdd = sc.parallelize(text)

counts = rdd.flatMap(lambda line: line.split(' ')) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .collect()

[print(c) for c in counts]

sc.stop()
