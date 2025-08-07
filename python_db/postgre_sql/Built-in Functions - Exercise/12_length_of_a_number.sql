SELECT
	population,
	LENGTH(CAST(population AS TEXT)) AS "length"
FROM
	countries
;