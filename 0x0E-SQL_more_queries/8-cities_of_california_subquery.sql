-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id`=`1`
 ORDER BY `id`;
