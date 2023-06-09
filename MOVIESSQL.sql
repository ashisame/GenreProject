-- Removing duplicates
DELETE FROM moviesdataset
WHERE MOVIES IN (
  SELECT MOVIES
  FROM moviesdataset 
  GROUP BY MOVIES
  HAVING COUNT(*) > 1
);

-- Removing irrelevant columns
ALTER TABLE moviesdataset
DROP COLUMN `ONE-LINE`,
DROP COLUMN STARS;

-- Removing missing values
DELETE FROM moviesdataset
WHERE Gross='';

-- Adding a new column to store the numerical values
ALTER TABLE moviesdataset ADD COLUMN GROSS_NUMERIC DECIMAL(10, 2);

-- Updating the new column with the converted numerical values
UPDATE moviesdataset
SET GROSS_NUMERIC = REPLACE(REPLACE(GROSS, '$', ''), 'M', '');

-- Changing the column name and type
ALTER TABLE moviesdataset
CHANGE COLUMN GROSS_NUMERIC GROSSINMIL DECIMAL(10, 2);

-- Adding a new subgenre column
ALTER TABLE moviesdataset ADD COLUMN Subgenre VARCHAR(255);

-- Updating the genre and subgenre columns
UPDATE moviesdataset
SET Subgenre = SUBSTRING_INDEX(Genre, ',', -1),
    Genre = SUBSTRING_INDEX(Genre, ',', 1);
   
-- Updating the subgenre column name and position
ALTER TABLE moviesdataset
CHANGE COLUMN Subgenre SUBGENRE VARCHAR(255);

-- Replacing the subgenre column after the genre column
ALTER TABLE moviesdataset
MODIFY COLUMN SUBGENRE VARCHAR(255) AFTER GENRE;

SELECT * FROM moviesdataset;
