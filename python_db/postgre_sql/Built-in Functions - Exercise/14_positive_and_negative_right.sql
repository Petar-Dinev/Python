SELECT
	peak_name,
	right(peak_name, 4) AS positive_right,
	right(peak_name, -4) AS negative_right
FROM peaks