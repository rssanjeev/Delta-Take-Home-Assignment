-- Assumption: Based on the email response, I'm assuming that the flightkey is duplicated and unique for every flight.

/*
In the following qeury I will be creating a common table expression (CTE) including a rank based on the 'lastopdt' datetime in descending 
order per 'flightkey'. 
*/

with cte as 
(
	select *, 
	RANK() over(partition by flightkey order by lastupdt desc) Ranky 
	from Flight
)
select 
	"Carrier Code", 
	flight_dt, 
	flightnum, 
	orig_arpt, 
	dest_arpt, 
	flightstatus, 
	lastupdt, 
	flightkey 
from cte 
where Ranky = 1;
