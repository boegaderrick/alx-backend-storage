-- This script calculates the lifespan of bands with glam rock as their main style
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;
