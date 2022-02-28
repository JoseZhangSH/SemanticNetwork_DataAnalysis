from flask import Flask
from flask import request
import pandas as pd

app = Flask(__name__)

df_complete = pd.read_csv('01_Processed Data/Complete-Data.csv')

@app.route("/<concept>",methods=['GET','POST'])
def List_Semantic_Feature(concept):
    feature_list = list(df_complete[df_complete['Concept']==str(concept)].sort_values(by=['cue_validity'],ascending=False)['Feature'])
    if request.method == 'GET':
        return feature_list[0]
    else:
        return 'POST'