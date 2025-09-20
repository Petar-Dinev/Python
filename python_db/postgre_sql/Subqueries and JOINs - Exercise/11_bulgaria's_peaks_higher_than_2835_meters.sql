SELECT
	c.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM
	countries AS c
JOIN
	mountains_countries AS mc
USING
	(country_code)
JOIN
	mountains AS m
ON
	mc.mountain_id = m.id
JOIN
	peaks AS p
ON
	m.id = p.mountain_id
WHERE
	p.elevation > 2835 AND c.country_code = 'BG'
ORDER BY
	p.elevation DESC
;