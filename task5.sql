-- Better way of doing this with unique indices, can't quite get it to work here though
SELECT max(id) FROM profiles;
SELECT max(id), max(guid) FROM profiles;

INSERT INTO clients (id, description, guid, update_time, create_time, idmasteraccount, geofence, phone, display_id, idstatus, idaccounttype, idprofile) VALUES (2525, 'Task5 client', 591530, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP , 1000, '','','','active',0, 9315);


INSERT INTO profiles (id, contact_id, attribute_id, value, crypted)
VALUES (117514, 9305, 3, 'Task5', 0),
(117515, 9315, 4, 'client', 0),
(117516, 9315, 5, 'Montreal', 0),
(117517, 9315, 6, 'Mrs.', 0),
(117518, 9315, 9, 'QC', 0),
(117519, 9315, 11, 'F', 0),
(117520, 9315, 26, 'task5@client.com', 0),
(117521, 9315, 18, '555-555-5555', 0),
(117522, 9315, 30, '123 Sherbrooke St', 0),
(117523, 9315, 31, 'QC', 0),
(117524, 9315, 32, 'A1B 2C3', 0),
(117525, 9315, 2034, '1900-00-00', 0),
(117526, 9315, 2138, 'En', 0);



