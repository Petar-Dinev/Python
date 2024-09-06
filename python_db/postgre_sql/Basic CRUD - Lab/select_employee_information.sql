SELECT
	"id",
	first_name || ' ' ||
	last_name as "Full Name",
	job_title as "Job Title"
from employees;