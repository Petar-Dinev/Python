SELECT
	c.country_name,
	COALESCE(r.river_name, NULL) AS river_name
FROM
	countries AS c
LEFT JOIN
	countries_rivers AS cr
USING
	(country_code)
LEFT JOIN
	rivers AS r
ON
	r.id = cr.river_id
WHERE
	c.continent_code = (SELECT continent_code FROM continents WHERE continent_name = 'Africa')
ORDER BY
	country_name
LIMIT 5;