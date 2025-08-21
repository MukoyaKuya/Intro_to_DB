-- File: task_4.sql
-- Print full description of the table 'Books' in alx_book_store

SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_DEFAULT AS 'Default',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Books'
  AND TABLE_SCHEMA = 'alx_book_store'
ORDER BY ORDINAL_POSITION;
