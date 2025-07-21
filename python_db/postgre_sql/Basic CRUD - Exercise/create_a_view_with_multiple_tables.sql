CREATE VIEW view_addresses AS
SELECT CONCAT(
               e.first_name,
               ' ',
               e.last_name
       ) AS full_name,
       e.department_id,
       CONCAT(
               number,
               ' ',
               street
       ) AS address
FROM employees AS e,
     addresses AS a
Where e.address_id = a.id;