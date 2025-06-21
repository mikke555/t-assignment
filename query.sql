SELECT 
    customer_id,
    value_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id, TO_CHAR(value_date, 'YYYY-MM')
        ORDER BY value_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_sum,
    SUM(amount) OVER (PARTITION BY customer_id) AS total_amount
FROM 
    transaction
ORDER BY 
    customer_id, value_date;