-- Task: Rank country origins of bands, ordered by the number of (non-unique) fans.

DROP 
  TABLE IF EXISTS temp_country_fans;
CREATE TEMPORARY TABLE temp_country_fans AS 
SELECT 
  origin, 
  SUM(nb_fans) AS nb_fans 
FROM 
  metal_bands 
GROUP BY 
  origin;
SELECT 
  origin, 
  nb_fans 
FROM 
  temp_country_fans 
ORDER BY 
  nb_fans DESC;
