-- 1. Top 10 Restaurant Categories
SELECT category, COUNT(*) AS total_restaurants
FROM ubereats_restaurants
GROUP BY category
ORDER BY total_restaurants DESC
LIMIT 10;

-- 2. Price Range Distribution for High-Rated Restaurants
SELECT 
  CASE price_range
    WHEN '$' THEN 'Affordable ($)'
    WHEN '$$' THEN 'Moderate ($$)'
    WHEN '$$$' THEN 'Expensive ($$$)'
    WHEN '$$$$' THEN 'Luxury ($$$$)'
    ELSE 'Unknown'
  END AS price_category,
  COUNT(*) AS count
FROM ubereats_restaurants
WHERE score >= 4.5
  AND price_range IS NOT NULL
  AND price_range != ''
GROUP BY price_range
ORDER BY count DESC;

-- 3. Most Popular Dishes from Highly Rated Restaurants
SELECT m.name AS dish_name, COUNT(*) AS popularity
FROM ubereats_menus m
JOIN ubereats_restaurants r ON m.restaurant_id = r.id
WHERE r.score >= 4.5
GROUP BY m.name
ORDER BY popularity DESC
LIMIT 10;

-- 4. Traits of Low-Rated Restaurants (3.0 ≤ score ≤ 4.0)
SELECT category, price_range, COUNT(*) AS low_rated_count
FROM ubereats_restaurants
WHERE score BETWEEN 3.0 AND 4.0
  AND price_range IN ('$', '$$', '$$$', '$$$$')
GROUP BY category, price_range
ORDER BY low_rated_count DESC
LIMIT 10;

-- 5. Highest Average Rated Categories (with 50+ restaurants)
SELECT category, ROUND(AVG(score), 2) AS avg_rating, COUNT(*) AS total_restaurants
FROM ubereats_restaurants
WHERE score IS NOT NULL
GROUP BY category
HAVING COUNT(*) > 50
ORDER BY avg_rating DESC
LIMIT 10;
