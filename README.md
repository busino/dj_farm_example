# dj_farm_example
Simple Farm Application in Django to be used to evaluate docker


# Update MySQL

```sql
CREATE USER 'farm'@'%' IDENTIFIED BY 'farm';
GRANT ALL PRIVILEGES ON farm.* TO 'farm'@'%';
FLUSH PRIVILEGES;
```
