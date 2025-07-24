SELECT name,
       start_date
FROM projects
WHERE left(name, 5) = 'MOUNT'
ORDER BY id;