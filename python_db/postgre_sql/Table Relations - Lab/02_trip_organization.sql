SELECT
	v.driver_id,
	v.vehicle_type,
	CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles AS v
	JOIN campers AS c
		ON c.id = driver_id;