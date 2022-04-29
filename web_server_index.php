<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0" name="viewport">
    <title>控制我的终端</title>

    <script>
        !function (n) {
            var e = n.document,
                t = e.documentElement,
                i = 640,
                d = i / 100,
                o = "orientationchange" in n ? "orientationchange" : "resize",
                a = function () {
                    var n = t.clientWidth || 320;
                    n > 640 && (n = 640),
                        t.style.fontSize = n / d + "px"
                };
            e.addEventListener && (n.addEventListener(o, a, !1), e.addEventListener("DOMContentLoaded", a, !1))
        }(window);
    </script>

</head>
<style>

    body {
        background-color: #5d7edf
    }

    h1 {
        text-align: center;
        display: block;
        margin-left: auto;
        margin-right: auto;
        margin-top: 1rem;
        border-style: solid;
        border-radius: 0.8rem;
        color: #5d7edf;
        background-color: aliceblue;
        opacity: 90%;
        font-family: system-ui;
        font-size: 0.5rem;
        padding: 0.4rem;


    }

    p {
        color: aliceblue;
        font-size: 0.3rem;
        opacity: 90%;
        font-family: system-ui;
        text-align: center;
    }

    p.bottom {
        padding: 0.3rem;

    }

    p.describe {
        align-items: center;
        font-size: 0.18rem;
        padding: 0.1rem;
    }

    a:link, a:visited {
        border-radius: 0.2rem;
        color: aliceblue;
        border: 0.02rem solid aliceblue;
        padding: 0.20rem 0.40rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        background: linear-gradient(145deg, #6487ef, #5471c9);
        box-shadow: 0.22rem 0.22rem 0.44rem #5370c6,
        -0.22rem -0.22rem 0.44rem #678cf8;
    }

    a:hover, a:active {
        opacity: 75%;
        background: aliceblue;
        color: #5d7edf;
    }


</style>
<body>
<h1 class="center">控 制 我 的 终 端</h1>
<p class="describe">一个远程查看与管理个人智能终端的地方</p>

<?php
$servername = "your server name";
$username = "your username";
$password = "your password";
$port = "your port";
$database = "your database name";

// Create connection
$conn = new mysqli($servername, $username, $password, $database, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT online FROM status WHERE deviceID = 0";
$resultrasperry = $conn->query($sql)->fetch_assoc()["online"];
$sql = "SELECT online FROM status WHERE deviceID = 1";
$resultdoorlock = $conn->query($sql)->fetch_assoc()["online"];

if ($resultdoorlock == 1) {
    echo "<p class='bottom'>智能门锁：
        <a href='https://cloudiful.xyz/doorlock.php' target='_self'>当前在线</a>
        </p>

";
} else {
    echo "<p class='bottom'>智能门锁：
        <a href='https://cloudiful.xyz/doorlock.php' target='_self'>当前离线</a>
        </p>
";
}

if ($resultrasperry == 1){
    echo "<p class='bottom'>树莓派：
        <a href='https://cloudiful.xyz/raspberry.php' target='_self'>当前在线</a>
        </p>";
}
else{
    echo "<p class='bottom'>树莓派：
        <a href='https://cloudiful.xyz/raspberry.php' target='_self'>当前离线</a>
        </p>";
}

$conn->close();

?>

<p class='bottom'>摄像头：
    <a href='https://cloudiful.xyz' target='_self'>未开放</a>
</p>

<p class="bottom">互联网ICP备案：
    <a href="https://beian.miit.gov.cn/" target="_blank">浙ICP备2022008757号-1</a>
</p>

</body>
</html>
