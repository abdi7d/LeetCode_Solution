# Write your MySQL query statement below
SELECT 
    machine_id,
    ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT 
        a1.machine_id,
        a1.process_id,
        a2.timestamp AS end_time,
        a1.timestamp AS start_time
    FROM Activity a1
    JOIN Activity a2
        ON a1.machine_id = a2.machine_id
       AND a1.process_id = a2.process_id
    WHERE a1.activity_type = 'start'
      AND a2.activity_type = 'end'
) t
GROUP BY machine_id;