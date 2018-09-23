import enigma

from flask import Flask
from pyspark import SparkContext

app = Flask(__name__)

sc = SparkContext(appName="smoketest")

POPULATION_DATASET_ID = '17ec2829-32f7-4f69-882f-4cb83505706d'
PRISON_DATASET_ID = '7ecea525-23f0-4c16-be92-b9e0d15b357f'

@app.route('/incarcerations')
def get_incarceration_data():
    return "Hello World!"

@app.route('/smoketest')
def smoke_test():
    try:
        doc = [
            'one fish two fish',
            'red fish blue fish'
        ]

        rdd = sc.parallelize(doc).flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

        expected_word_count = set([('fish', 4), ('blue', 1), ('two', 1), ('one', 1), ('red', 1)])
        actual_word_count = set(rdd.collect())

        if expected_word_count == actual_word_count:
            public = enigma.Public()

            if len(public.collections.list()) > 0:
                return 'Smoke Test PASS'
            else:
                return 'Smoke Test Fail - Issue connecting to Enigma Public'
        else:
            return 'Smoke Test Fail - pyspark not running as expected'

    except Exception as e:
        print(str(e))
        return f'Smoke Test FAIL - {str(e)}'
    