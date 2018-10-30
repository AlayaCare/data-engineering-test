SELECT * FROM clients 
LEFT JOIN profiles ON clients.idprofile = profiles.contact_id 
UNION ALL
SELECT * FROM clients  
RIGHT JOIN profiles ON clients.idprofile = profiles.contact_id 
WHERE clients.idprofile IS NULL

-- Using UNION ALL because MySQL does not support FULL OUTER JOIN
