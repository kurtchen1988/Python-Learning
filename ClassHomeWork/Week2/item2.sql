--1. 在users表中查询注册时间最早的十条会员信息。
SELECT * FROM users ORDER BY cdate LIMIT 10

--2. 从两个表中查询点赞数最高的5条博客信息，要求显示字段：（博文id，标题，点赞数，会员名）
SELECT blog.id, blog.title, blog.pcount, users.name FROM users, blog WHERE blog.uid = users.id ORDER BY blog.pcount DESC LIMIT 5
SELECT blog.id, blog.title, blog.pcount, users.name FROM blog INNER JOIN users ON blog.uid = users.id ORDER BY blog.pcount DESC LIMIT 5

--3. 统计每个会员的发表博文数量（降序），要求显示字段（会员id号，姓名，博文数量）
SELECT users.id, users.name, count(*) AS artNum FROM users, blog WHERE blog.uid=users.id GROUP BY users.id ORDER BY artNum DESC
SELECT users.id, users.name, count(*) AS artNum FROM blog INNER JOIN users ON blog.uid = users.id GROUP BY users.id ORDER BY artNum DESC

--4. 获取会员的博文平均点赞数量最高的三位。显示字段（会员id，姓名，平均点赞数）
SELECT users.id, users.name, avg(blog.pcount) AS thumbNum FROM users,blog WHERE blog.uid=users.id GROUP BY users.id ORDER BY thumbNum LIMIT 3
SELECT users.id, users.name, avg(blog.pcount) AS thumbNum FROM blog INNER JOIN users ON blog.uid = users.id GROUP BY users.id ORDER BY thumbNum LIMIT 3

--5. 删除没有发表博文的所有会员信息。
DELETE FROM users WHERE users.id NOT IN (SELECT uid FROM blog)