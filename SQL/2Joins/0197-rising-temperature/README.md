<h2><a href="https://leetcode.com/problems/rising-temperature">197. Rising Temperature</a></h2><h3>Easy</h3><hr><p>Table: <code>Weather</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
</pre>

<p>&nbsp;</p>

<p>Write a solution to find all dates&#39; <code>Id</code> with higher temperatures compared to its previous dates (yesterday).</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
<strong>Output:</strong> 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
<strong>Explanation:</strong> 
In 2015-01-02, the temperature was higher than the previous day (10 -&gt; 25).
In 2015-01-04, the temperature was higher than the previous day (20 -&gt; 30).
</pre>

### Notes
> window 을 비교하는 방법 (날짜 차이 아는 방법)

- 같은 테이블을 LEFT JOIN하고, ON <조건문>에서 날짜 간격이 차이나게 조인한다.
- 그리고 WHERE <조건문>을 이용하여 온도를 비교하면 된다.

> Example

```sql
SELECT *
FROM Weather AS w1
LEFT JOIN Weather AS w2
ON w1.recordDate=DATE_ADD(w2.recordDate, INTERVAL 1 DAY);
```
Output:
```text
| id | recordDate | temperature | id   | recordDate | temperature |
| -- | ---------- | ----------- | ---- | ---------- | ----------- |
| 1  | 2015-01-01 | 10          | null | null       | null        |
| 2  | 2015-01-02 | 25          | 1    | 2015-01-01 | 10          |
| 3  | 2015-01-03 | 20          | 2    | 2015-01-02 | 25          |
| 4  | 2015-01-04 | 30          | 3    | 2015-01-03 | 20          |
```
