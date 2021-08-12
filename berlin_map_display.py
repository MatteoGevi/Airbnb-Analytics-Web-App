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

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from shapely.geometry import Polygon, Point





# +
'''Berlin Map'''

# Public token to access Mapbox layout style for Plotly
fig = px.scatter_mapbox()
