 SELECT customer, SUM(ordervalue) FROM orders GROUP BY customer;
 
--  This pretty straight forward, since we need data for each customer, and customers are repeated,
--  we group their data using a group by clause.
--  The information we are interested in is the total value so we use the SUM aggregate function.
