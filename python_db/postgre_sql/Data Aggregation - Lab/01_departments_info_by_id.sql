SELECT
	department_id,
	COUNT(department_id)
FROM employees
GROUP BY department_id
ORDER BY department_id;