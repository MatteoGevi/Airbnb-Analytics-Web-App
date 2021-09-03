# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import system, os
import numpy as np
import pandas as pd
from fastapi import FastAPI
from pymongo import MongoClient

# +

# Server Security for HTTPS
server = flask.Flask('app')

def export_excel():
    # Convert House Prices into an exportable file
    strIO = io.BytesIO()
    excel_writer = pd.ExcelWriter(strIO, engine='xlsxwrite')
    df.to_excel(excel_writer, sheet_name='sheet1')
    excel_writer.save()
    excel_data =strIO.get_value()
    strIO.seek(0)
    return flask.send_file(strIO, attachment_filename="Housing Price.xlsx", as_attachment=True, cache_timeout=0)
