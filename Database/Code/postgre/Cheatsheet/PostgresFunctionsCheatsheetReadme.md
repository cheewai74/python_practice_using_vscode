# PostgreSQL & PL/pgSQL Stored Functions Cheatsheet #

### Boiler-plate stored function ###

```
CREATE OR REPLACE FUNCTION public.sp_user_ins_status(status smallint)
  RETURNS integer
  LANGUAGE plpgsql
AS $function$

DECLARE
  sproc_utc_now TIMESTAMP;

BEGIN
    SELECT CAST(NOW() at time zone 'utc' AS TIMESTAMP) INTO sproc_utc_now;
  
END
$function$
```

### Get count of records and return value ###

```
BEGIN
   SELECT count(*) into total FROM COMPANY;
   RETURN total;
END;

```

### Get id of newly created INSERT record ###

```
DECLARE
myid INTEGER;

BEGIN
INSERT INTO contacts 
VALUES 
  (name,'bob') 
RETURNING id INTO myid;
END
```

### Basic if statement ###

```
BEGIN
 IF (SELECT COUNT(*) FROM pg_language WHERE lanname = 'plpgsql') > 0 THEN 
     RAISE NOTICE 'GOOD';
 ELSE
     RAISE NOTICE 'BAD';
 END IF;
END
```

### Raising an exception ###

```
CREATE OR REPLACE FUNCTION msgfailerror() 
RETURNS trigger AS 
$$
BEGIN 
  IF NEW.noces< new.first_column THEN 
    RAISE EXCEPTION 'cannot have a negative salary'; 
  END IF; 
  return new; 
END;
$$
LANGUAGE plpgsql;
```


### Returning multiple rows of data ###

```
RETURNS TABLE(...)

BEGIN
  RETURN QUERY SELECT ....; -- result is forwarded to output directly
  RETURN;   -- there will not be any next result, finish execution
END;
```
References:
* http://stackoverflow.com/questions/17244256/how-to-return-multiple-rows-from-pl-pgsql-function