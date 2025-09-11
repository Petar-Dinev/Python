SELECT
	a.name,
	a_t.animal_type,
	TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM
	animals AS a
JOIN
	animal_types AS a_t
ON
	a.animal_type_id = a_t.id
ORDER BY
	a.name