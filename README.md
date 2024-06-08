# April-May-Sign-Up-s

You have been asked to get a list of all the sign up IDs with transaction start dates in either April or May.


Since a sign up ID can be used for multiple transactions only output the unique ID.


Your output should contain a list of non duplicated sign-up IDs.


## Table: transactions
transaction_id:  int
signup_id:  int
transaction_start_date:  datetime
amt: float

## Sample data
transaction_id	signup_id	transaction_start_date	amt
1	                  100	      2020-04-30	        24.9
2	                  101	      2020-04-16	        24.9
3	                  102	      2020-04-28	        9.9
4	                  102	      2020-05-28	        9.9
