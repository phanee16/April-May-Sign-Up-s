SELECT signup_id, transaction_start_date
FROM transactions
WHERE MONTH(transaction_start_date) IN (4, 5);
