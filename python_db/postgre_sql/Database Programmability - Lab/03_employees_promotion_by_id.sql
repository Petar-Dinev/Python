CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
	BEGIN
		IF (SELECT COUNT(*) FROM employees AS e WHERE employee_id = id ) IS NULL THEN
			RETURN;
		END IF;
		UPDATE employees AS e
		SET salary = salary * 1.05
		WHERE employee_id = id;
	END;
$$
LANGUAGE plpgsql;