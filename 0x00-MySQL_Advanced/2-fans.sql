-- This script queries a metal_band database

-- Queries the database for origin of bands ranked by number of fans in descending order
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
