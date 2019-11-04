description = """

Your first task as Chief Business Intelligence Officer at AckMe! Retail is to analyze the last few years' sales data for *UnbelievableAlien* plush dolls.

The given data will be an array of strings, each one representing the day's change in stock (the amount of purchases minus the amount of sales).

Each string begins with a `YYYY-MM-DD` date stamp, followed by a semicolon, and finally, the change in stock (computed at the end of the day), which begins with either a `+` or `-`. An integer will follow this sign.

The array will be sorted in ascending chronological order. Not all days will be given, say for holidays and when the change in stock is `0`.

The Director wishes to know how many **complete** days (including weekends and holidays) in total the stock was below `100` units, because during these days there may have been potential lost sales of larger amounts.

Because the recorded data is computed at the end of the business day, even if a client purchases the entire stock (at or above `100` units), that particular day should not be counted as having "low stock" in the total. A purchase takes some time to be processed, so there is a moment when the stock may have been `100` units or more. However, the following days should be counted as having "low stock".
"""
