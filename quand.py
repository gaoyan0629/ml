import quandl
mydata = quandl.get("YAHOO/INDEX_DJI", 
        start_date="2005-12-01", end_date="2005-12-05")
