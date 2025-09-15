SELECT
	CONCAT_WS(' ', a.address, a.address_2) AS apartment_address,
	b.booked_for AS nights
FROM
	apartments AS a
JOIN
	bookings AS b
ON
	b.booking_id = a.booking_id
ORDER BY
	a.apartment_id
;