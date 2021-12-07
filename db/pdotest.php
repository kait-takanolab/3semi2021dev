<?php

$dsn = 'mysql:dbname=3semi2021;host=127.0.0.1';
$user = 'scott';
$password = 'tiger';

try {
    // データベースへの接続
    $db = new PDO($dsn, $user, $password);
    $sql = "select * from emp";
    $stmt = $db->prepare($sql);
    $stmt->execute();
    $data = array();
    $count = $stmt->rowCount();
    While($row = $stmt->fetch(PDO::FETCH_ASSOC)){
	$data[] = $row;
    }

    print("Connected.");

} catch (PDOException $e) {
    print "エラー発生: " . $e->getMessage();
    die();
}
?>

<html>
<body>
<table border=1>
	<tr><th>EMPNO</th><th>ENAME</th><th>JOB</th><th>MGR</th><th>HIREDATE</th><th>SAL</th><th>COMM</th><th>DEPTNO</th></tr>
	<?php foreach($data as $row): ?>
	<tr>
	<td><?php echo $row['EMPNO']; ?></td>
	<td><?php echo $row['ENAME']; ?></td>
	<td><?php echo $row['JOB']; ?></td>
	<td><?php echo $row['MGR']; ?></td>
	<td><?php echo $row['HIREDATE']; ?></td>
	<td><?php echo $row['SAL']; ?></td>
	<td><?php echo $row['COMM']; ?></td>
	<td><?php echo $row['DEPTNO']; ?></td>
	</tr>
	<?php endforeach; ?>
</table>
</body>
</html>

// サーバからの切断
$db = null;
?>