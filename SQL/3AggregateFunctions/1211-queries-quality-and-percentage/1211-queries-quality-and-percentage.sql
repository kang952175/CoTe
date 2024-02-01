select
query_name,
round(avg(cast(rating as decimal) / position), 2) as quality,
round(avg(if(rating<3,1,0))*100, 2) as poor_query_percentage
from Queries
WHERE query_name is not null
group by query_name;

