UPDATE countries
SET iso_code = UPPER(left(country_name, 3))
WHERE iso_code IS NULL;