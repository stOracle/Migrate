--RETURNS INVOICES HIGHER THAN THE VENDOR'S AVG INVOICE
SELECT vendor_id, invoice_number, invoice_total
FROM invoices inv_main
WHERE invoice_total >
    (
    SELECT AVG(invoice_total)
    FROM invoices inv_sub
    WHERE inv_sub.vendor_id = inv_main.vendor_id
    )
ORDER BY vendor_id, invoice_total;

--FACTORING
WITH summary AS
  (
  SELECT vendor_state, vendor_name, SUM(invoice_total) AS sum_of_invoices
  FROM invoices
    JOIN vendors ON invoices.vendor_id = vendors.vendor_id
  GROUP BY vendor_state, vendor_name
  ),
top_in_state AS
  (
  SELECT vendor_state, MAX(sum_of_invoices) AS sum_of_invoices
  FROM summary
  GROUP BY vendor_state
  )
SELECT summary.vendor_state, summary.vendor_name,
  top_in_state.sum_of_invoices
FROM summary JOIN top_in_state
  ON summary.vendor_state = top_in_state.vendor_state AND
    summary.sum_of_invoices = top_in_state.sum_of_invoices
ORDER BY summary.vendor_state;

--HIERARCHICAL
SELECT empno,ename, LEVEL
FROM emp
START WITH ename = 'KING'
CONNECT BY PRIOR empno = mgr
ORDER BY LEVEL, empno;

/*************************CHAPTER 6 EXERCISES***********************
1.  Write a SELECT statement that returns this but use subquery in the 
    where clause
      SELECT DISTINCT vendor_name
      FROM vendors v JOIN invoices i ON v.vendor_id = i.vendor_id
      ORDER BY vendor_name*/
      
SELECT DISTINCT vendor_name
FROM vendors v JOIN invoices i ON v.vendor_id = i.vendor_id
ORDER BY vendor_name;

SELECT vendor_name
FROM vendors
WHERE vendor_id IN
  (SELECT vendor_id FROM invoices)
ORDER BY vendor_name;
      
/*
2.  which invoices have a payment_total that's greater than the avg 
    payment_total for all paid invoices? return invoice_number and 
    invoice_total*/
    
SELECT invoice_number, invoice_total 
FROM invoices
WHERE payment_total >
  (
  SELECT AVG(payment_total) 
  FROM invoices
  WHERE payment_total > 0
  )
ORDER BY invoice_number;
    
/*
3.  Write a query returning two columns from the General_Ledger_Accounts:
    account_number and account_description. The result should have one row
    for each account num that has nvr been used
    use a subquery introduced with NOT EXISTS
    sort by account_number*/
    
SELECT account_number, account_description
FROM general_ledger_accounts
WHERE NOT EXISTS
  (
  SELECT *
  FROM invoice_line_items
  WHERE invoice_line_items.account_number = 
    general_ledger_accounts.account_number
  )
ORDER BY account_number;
    
/*
4.  returns 4 columns: vendor_name, invoice_id, invoice_sequence, 
    line_item_amt for each invoice that has > 1 line item in the 
    invoice_line_items table 
    (use subquery that tests for invoice_sequence>1)*/
    
SELECT vendor_name, i.invoice_id, invoice_sequence, line_item_amt 
FROM
    (
    vendors v 
    JOIN
    invoices i
    ON v.vendor_id = i.vendor_id
    )
    JOIN
    invoice_line_items li
    ON i.invoice_id = li.invoice_id
WHERE i.invoice_id IN
  (
  SELECT invoice_id
  FROM invoice_line_items
  WHERE invoice_sequence > 1
  )
ORDER BY vendor_name, i.invoice_id, invoice_sequence;    
    
/*
5.  returns single value representing the sum of the largest unpaid invoices
    for each vendor. Use an inline view that returns MAX(invoice_total)
    grouped by vendor_id, filtering for invoices with a balance due*/
    
SELECT SUM(invoice_max) AS sum_of_maximums
FROM 
  (
  SELECT vendor_id, MAX(invoice_total) AS invoice_max
  FROM invoices
  WHERE invoice_total - credit_total - payment_total > 0
  GROUP BY vendor_id
  );
  
WITH invoice_max AS
  (
  SELECT vendor_id, MAX(invoice_total) AS invoice_max
  FROM invoices
  WHERE invoice_total - credit_total - payment_total > 0
  GROUP BY vendor_id
  )
SELECT SUM(invoice_max) AS sum_of_maximums
FROM invoice_max;
    
/*
7.  returns the name, city and state of each vendor that's located in a 
    unique city and state. don't include vendors that have a city and state 
    in common with another vendor*/
    
SELECT vendor_name, vendor_city, vendor_state
FROM vendors
WHERE vendor_state || vendor_city NOT IN
  (
  SELECT vendor_state || vendor_city
  FROM vendors
  GROUP BY vendor_state || vendor_city
  HAVING COUNT(*) > 1
  )
ORDER BY vendor_state, vendor_city; 


/*
8.  Use a correlated subquery to return one row per vendor, representing the
    vendor's oldest invoice (earliest date). Each row should include 
    these 4 columns: vendor_name, invoice_number, invoice_date, invoice_total*/

SELECT vendor_name, invoice_number AS oldest_invoice,
    invoice_date, invoice_total
FROM invoices i_main JOIN vendors v
    ON i_main.vendor_id = v.vendor_id
WHERE invoice_date =
  (
  SELECT MIN(invoice_date)
  FROM invoices i_sub
  WHERE i_sub.vendor_id = i_main.vendor_id
  )
ORDER BY vendor_name;

/*
9.  do that^ without correlated subquery /*/

SELECT vendor_name, invoice_number AS oldest_invoice,
  oi.oldest_invoice_date, invoice_total
FROM invoices i JOIN
  (
  SELECT vendor_id, MIN(invoice_date) AS oldest_invoice_date
  FROM invoices
  GROUP BY vendor_id
  ) oi
  ON (i.vendor_id = oi.vendor_id)
      AND (i.invoice_date = oi.oldest_invoice_date)
  JOIN vendors v on i.vendor_id = v.vendor_id
ORDER BY vendor_name;

/*-----------------------------------CHAPTER 11*/

CREATE OR REPLACE VIEW open_items 
AS
  SELECT vendor_name, invoice_number, invoice_total, 
    (invoice_total - payment_total - credit_total) as balance_due
  FROM vendors join invoices 
    ON vendors.vendor_id = invoices.vendor_id
  WHERE (invoice_total - payment_total - credit_total) > 0
  ORDER BY vendor_name;
  
SELECT * 
FROM open_items
WHERE balance_due >= 1000;

CREATE OR REPLACE VIEW open_items_summary
AS
SELECT vendor_name, COUNT(*) AS open_item_count,
  SUM(invoice_total - (payment_total + credit_total)) AS open_item_total
FROM vendors JOIN invoices 
  ON vendors.vendor_id = invoices.vendor_id
WHERE (invoice_total -(credit_total + payment_total)) > 0
GROUP BY vendor_name
ORDER BY open_item_total DESC;

SELECT * 
FROM open_items_summary
WHERE ROWNUM <= 5;

CREATE OR REPLACE VIEW vendor_address 
AS
SELECT vendor_id, vendor_address1, vendor_address2, vendor_city,
  vendor_state, vendor_zip_code
FROM vendors;

UPDATE vendor_address
SET vendor_address1 = '1990 Westwood Blvd.',
    vendor_address2 = 'Ste 260'
WHERE vendor_id = 4;