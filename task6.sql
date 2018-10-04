ALTER TABLE profiles
ADD random int;

UPDATE profiles
SET random = rand()*1000
WHERE random IS NULL ;
