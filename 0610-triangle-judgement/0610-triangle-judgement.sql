# Write your MySQL query statement below
# sum of two side lengths of a triangle is always greater than the third side. 

SELECT *, IF(x+y>z and y+z>x and z+x>y, "Yes", "No") as triangle FROM Triangle;