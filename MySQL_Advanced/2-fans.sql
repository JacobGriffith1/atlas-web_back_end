-- 2. Best Band Ever!
-- Ranks country origins of bands, ordered by the number od (non-unique) fans
-- Column names: origin, nb_fans

SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
