from pyspark.sql import functions as F

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder, TrainValidationSplit
from pyspark.ml.linalg import VectorUDT,Vectors
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.sql import Window
from pyspark.ml import Pipeline
from pyspark.ml.regression import GeneralizedLinearRegression
from IPython.display import display, Markdown, HTML
import pandas as pd
import re
from tabulate import tabulate
import random
import sys
import matplotlib.pyplot as plt
import numpy as np

sc.addPyFile("/home/svanhmic/workspace/DABAI/Workflows/shared/ConvertAllToVecToMl.py")
from ConvertAllToVecToMl import ConvertAllToVecToMl as convert

def save_as_html(dummy):
    import uuid
    with open('img/'+uuid.uuid4().hex+".html",'w') as html_file:
        html_file.write(dummy.to_html())


#import data and rename bad name rank into vaerdiSlope
#RAW DATA!!! 

PATH = '/home/svanhmic/workspace/data/DABAI/sparkdata/parquet'
#PIC_PATH = '/home/svanhmic/workspace/results/DABAI/tabel-pics'
#exclude some of the variables, and cast all variables to double

