CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INTEGER
AS
$$
DECLARE
		employees_count INT;
BEGIN
	SELECT
		COUNT(*)
	FROM
		addresses AS a
	JOIN
		employees AS e
	ON
		a.address_id = e.address_id
	WHERE
		a.town_id = (SELECT town_id FROM towns WHERE name = town_name)
	INTO employees_count;
	RETURN employees_count;
END;
$$
LANGUAGE plpgsql;