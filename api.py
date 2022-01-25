# load the libraries
from flask import Flask, jsonify
from flask_restful import Resource, Api
import numpy as np
import pandas as pd

app = Flask(__name__)
api = Api(app)

class get_sheet_names(Resource):    # to get the sheet names
    def get(self,fpname):
        xls = pd.ExcelFile(fpname)  # read the excel file
        wk_sheet_names = xls.sheet_names    # read all sheet names
        return {"Filenamepath":wk_sheet_names}

class get_headers(Resource):    # to get the headers from the sheet
    def get(self,fpname,shname):
        col_headers = []
        xls2 = pd.ExcelFile(fpname)
        df2 = xls2.parse(shname)
        col_headers = df2.columns.values
        col_headers = np.array(col_headers).tolist()
        return jsonify({"SheetColHeaders":col_headers})

# add the api resource 
api.add_resource(get_sheet_names, '/get_sheet_names/<path:fpname>')
api.add_resource(get_headers, '/get_headers/<path:fpname>/<string:shname>')

if __name__ == '__main__':
    app.run(debug=True)



