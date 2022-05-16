/*What are the top 5 most expensive items (on average) for Kenyan providers?*/
SELECT top 5 item_name,
           average_amount = round(avg(item_amount/item_quantity), 1)
FROM dbo.data_claims c
JOIN dbo.data_provider p ON c.provider_name = p.provider_name
AND p.provider_country = 'Kenya'
WHERE item_status not in ('DELETED')
  AND item_status IS NOT NULL
  AND cast(item_quantity AS decimal) > 0
  AND claim_status not in ('Deleted')
GROUP BY item_name
ORDER BY avg(item_amount) DESC

/*How many claims have been approved by 5-star rated Nigerian providers?*/
SELECT count(DISTINCT claim_id)
FROM dbo.data_claims c
JOIN dbo.data_provider p ON c.provider_name = p.provider_name
AND p.provider_country = 'Nigeria'
AND provider_star_rating = 5
WHERE claim_status = 'Approved'