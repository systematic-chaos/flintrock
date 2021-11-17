from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Demo Deploy").setMaster("spark://ec2-34-255-97-216.eu-west-1.compute.amazonaws.com:7077")
sc = SparkContext(conf=conf)

print('==== DEMO DEPLOY ====')

rdd = sc.textFile('s3a://simple-pyspark-deploy-bucket/rock-and-roll-wiki.txt')

counts = rdd.flatMap(lambda line: line.split(' ')) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .collect()

[print(c) for c in counts]

sc.stop()
