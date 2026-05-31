# Write your MySQL query statement below
SELECT
    p.product_id,
    ROUND(
        IFNULL(SUM(pr.price * u.units) / SUM(u.units), 0),
        2
    ) AS average_price
FROM Prices pr
LEFT JOIN UnitsSold u
    ON pr.product_id = u.product_id
   AND u.purchase_date BETWEEN pr.start_date AND pr.end_date
RIGHT JOIN Prices p
    ON pr.product_id = p.product_id
GROUP BY p.product_id;