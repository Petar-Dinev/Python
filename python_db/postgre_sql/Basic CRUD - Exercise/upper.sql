UPDATE projects
SET name = upper(name)
returning *;