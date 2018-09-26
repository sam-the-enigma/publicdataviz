import enigma
import os

from flask import Flask, jsonify
from pyspark import SparkContext, SQLContext
from pprint import pprint

app = Flask(__name__)

sc = SparkContext(appName="smoketest")
sqlContext = SQLContext(sparkContext=sc)


POPULATION_DATASET_ID = '17ec2829-32f7-4f69-882f-4cb83505706d'
PRISON_DATASET_ID = '7ecea525-23f0-4c16-be92-b9e0d15b357f'

@app.route('/data')
def get_data():
    return "Hello World!"

    # population_data = get_data_from_enigma(POPULATION_DATASET_ID)
    # prison_data = get_data_from_enigma(PRISON_DATASET_ID)


    # population_dataframe = sqlContext.createDataFrame(population_data).withColumnRenamed('b01003001', 'population')
    # prison_dataframe = sqlContext.createDataFrame(prison_data)

    # population_dataframe.show()
    # prison_dataframe.show()

    # df = population_dataframe.join(prison_dataframe, on=population_dataframe.place_name == prison_dataframe.state, how='inner')

    # df.show()

    # all_columns = df.schema.names
    # punishment_columns = ['prison', 'parole', 'jail', 'felony_probation']
    # columns_we_want = ['population', 'state'] + punishment_columns
    
    # columns_to_drop = set(all_columns) - set(columns_we_want)
    # df = df.drop(*columns_to_drop)

    # df.show()

    # df = df.na.fill(0)

    # df.show()
    # rows_as_dicts = df.rdd.map(lambda row: row.asDict()).collect()

    # pprint(rows_as_dicts)

    # response = jsonify(rows_as_dicts)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    # return response

    # return f"Rows in Population Data: {len(population_data)}, Rows in Prison Data: {len(prison_data)}"


# def get_data_from_enigma(dataset_id):
#     public = enigma.Public()
#     public.set_auth(apikey=os.getenv('ENIGMA_PUBLIC_KEY', None))
#     dataset = public.datasets.get(dataset_id)
#     current_snapshot = dataset.current_snapshot
#     return current_snapshot.export_dataframe()


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
    