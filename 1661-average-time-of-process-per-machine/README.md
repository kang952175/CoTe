<h2><a href="https://leetcode.com/problems/average-time-of-process-per-machine">1661. Average Time of Process per Machine</a></h2><h3>Easy</h3><hr><p>Table: <code>Activity</code></p>

<pre>
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM (category) of type (&#39;start&#39;, &#39;end&#39;).
timestamp is a float representing the current time in seconds.
&#39;start&#39; means the machine starts the process at the given timestamp and &#39;end&#39; means the machine ends the process at the given timestamp.
The &#39;start&#39; timestamp will always be before the &#39;end&#39; timestamp for every (machine_id, process_id) pair.</pre>

<p>&nbsp;</p>

<p>There is a factory website that has several machines each running the <strong>same number of processes</strong>. Write a solution&nbsp;to find the <strong>average time</strong> each machine takes to complete a process.</p>

<p>The time to complete a process is the <code>&#39;end&#39; timestamp</code> minus the <code>&#39;start&#39; timestamp</code>. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.</p>

<p>The resulting table should have the <code>machine_id</code> along with the <strong>average time</strong> as <code>processing_time</code>, which should be <strong>rounded to 3 decimal places</strong>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+
<strong>Output:</strong> 
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+
<strong>Explanation:</strong> 
There are 3 machines running 2 processes each.
Machine 0&#39;s average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1&#39;s average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2&#39;s average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456
</pre>

### Notes

> 전후 차이 계산하는 방법
---

- left join으로 같은 테이블을 합친다.
- on <key>을 이용하여 and 논리연산자로 복합키를 이용하여 전후를 붙여준다.
- 특히, 마지막 조건으로 '전 < 후'를 넣어 컬럼이 전과 후로 분리되게 한다.
  
> Example
---

Code
```sql
select *
from Activity a1
join Activity a2
on a1.process_id=a2.process_id
and a1.machine_id=a2.machine_id
and a1.timestamp<a2.timestamp;
```
Output
```text
| machine_id | process_id | activity_type | timestamp | machine_id | process_id | activity_type | timestamp |
| ---------- | ---------- | ------------- | --------- | ---------- | ---------- | ------------- | --------- |
| 0          | 0          | start         | 0.712     | 0          | 0          | end           | 1.52      |
| 0          | 1          | start         | 3.14      | 0          | 1          | end           | 4.12      |
| 1          | 0          | start         | 0.55      | 1          | 0          | end           | 1.55      |
| 1          | 1          | start         | 0.43      | 1          | 1          | end           | 1.42      |
| 2          | 0          | start         | 4.1       | 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.5       | 2          | 1          | end           | 5         |
```
결과적으로 필요한 테이블은 다음과 같다.
Code
```sql
select a1.machine_id, a1.timestamp, a2.timestamp
from Activity a1
join Activity a2
on a1.process_id=a2.process_id
and a1.machine_id=a2.machine_id
and a1.timestamp<a2.timestamp;
```
Output
```text
| machine_id | timestamp | timestamp |
| ---------- | --------- | --------- |
| 0          | 0.712     | 1.52      |
| 0          | 3.14      | 4.12      |
| 1          | 0.55      | 1.55      |
| 1          | 0.43      | 1.42      |
| 2          | 4.1       | 4.512     |
| 2          | 2.5       | 5         |
```


