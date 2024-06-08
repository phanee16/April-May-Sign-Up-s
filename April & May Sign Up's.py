# Import your libraries
import pyspark
from pyspark.sql.functions import month,col

# Start writing code
transactions.filter(
    (month(col('transaction_start_date')).isin([4,5])) 
    ).select('signup_id').distinct().toPandas()
