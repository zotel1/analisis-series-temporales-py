#Import pandas
import pandas as pd

#Convert the stock index and bond index into sets
set_stock_dates = set(stocks.index)
set_bond_dates = set(bonds.index)

#Take the difference between the sets and print
print(set_stock_dates - set_bond_dates)

# Merge stocks ad bonds DataFrames using .join()
stocks_and_bonds = stocks.join(bonds, how='inner')

"""
<script.py> output:
    {'2009-10-12', '2010-10-11', '2013-11-11', '2015-10-12', '2007-11-12', '2013-10-14', '2011-10-10', '2007-10-08', '2008-11-11', '2014-11-11', '2008-10-13', '2016-10-10', '2017-06-09', '2012-10-08', '2009-11-11', '2012-11-12', '2015-11-11', '2016-11-11', '2011-11-11', '2010-11-11', '2014-10-13'}
"""