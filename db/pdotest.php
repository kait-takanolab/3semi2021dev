<?php

$dsn = 'mysql:dbname=3semi2021;host=127.0.0.1';
$user = 'scott';
$password = 'tiger';

try {
    // データベースへの接続
    $db = new PDO($dsn, $user, $password);
} catch (PDOException $e) {
    print "エラー発生: " . $e->getMessage();
    die();
}

print("Connected.");

// サーバからの切断
$db = null;
?>