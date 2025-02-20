-- 3. Old School Band
-- Lists Glam Rock bands ranked by longevity

SELECT DISTINCT `band_name`, IFNULL(`split`, 2024) - `formed` as `lifespan`
    FROM `metal_bands` WHERE FIND_IN_SET('Glam rock', style)
    ORDER BY `lifespan` DESC;
