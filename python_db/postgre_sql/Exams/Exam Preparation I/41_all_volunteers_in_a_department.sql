CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(search_volunteers_department VARCHAR(30))
RETURNS INTEGER
AS
$$
	DECLARE
		volunteers_count INT;
	BEGIN
		SELECT
			COUNT(*) INTO volunteers_count
		FROM
			volunteers
		WHERE
			department_id = (SELECT id FROM volunteers_departments WHERE department_name = search_volunteers_department);
		RETURN volunteers_count;
	END;
$$
LANGUAGE plpgsql;