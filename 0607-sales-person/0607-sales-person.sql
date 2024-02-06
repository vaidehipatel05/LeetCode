# Write your MySQL query statement below

SELECT s.name from SalesPerson s
where s.name NOT IN
(SELECT s.name from SalesPerson s
INNER JOIN Orders o ON s.sales_id = o.sales_id
INNER JOIN Company c ON c.com_id = o.com_id
WHERE c.name ='RED' );
