<?php
header("Content-type:text/html;charset=utf-8");

  //将数组存到指定的text文件中
$file_path = "password2.txt";
if(file_exists($file_path)){
$fp = fopen($file_path,"r");
$str = fread($fp,filesize($file_path));//指定读取大小，这里把整个文件内容读取出来

}

//echo $output;
  //获取数据

?>

?>
<!DOCTYPE html>
<!-- saved from url=(0028)http://logicjake.xyz/secret/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="format-detection" content="telphone=no, email=no">
<meta name="renderer" content="webkit">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="HandheldFriendly" content="true">
<meta name="MobileOptimized" content="320">
<meta name="screen-orientation" content="portrait">
<meta name="x5-orientation" content="portrait">
<meta name="msapplication-tap-highlight" content="no">
<title>Password Generator</title>
<style type="text/css">
* {
    cursor: pointer;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-touch-callout: none;
    -webkit-user-drag: none;
    margin: 0;
    padding: 0;
}

input[type=text]:focus,
input[type=password]:focus,
input[type=email]:focus,
input[type=url]:focus,
input[type=date]:focus,
input[type=month]:focus,
input[type=time]:focus,
input[type=datetime]:focus,
input[type=datetime-local]:focus,
input[type=week]:focus,
input[type=number]:focus,
input[type=search]:focus,
input[type=tel]:focus,
input[type=color]:focus,
select:focus,
textarea:focus {
  outline: 0;
  outline: thin dotted \9;
  border-color: #129FEA
}

html, body {
    min-height: 100%;
    font-size: 10px;
}

html {
    font-family:
        HelveticaNeue-Light,
        'Helvetica Neue Light',
        'Helvetica Neue',
        Helvetica,
        Arial,
        sans-serif; /* 1 */
    -ms-text-size-adjust: 100%; /* 2 */
    -webkit-text-size-adjust: 100%; /* 2 */
}

h1 {
    font-size: 3rem;
    text-align: center;
    padding: 20px 0;
    color: #fff;
}

li {
    list-style: none;
}

ul {
    padding: 0;
    margin: 0;
}

blockquote {
    font-size: 1.3rem;
    line-height: 1.2em;
}

strong {
    font-weight: bold;
    color: red;
}
h2 {
    font-size: 1.6rem;
    padding: 0.2em 0 0.6em;
    color:#fff;
    text-align: left;
}


h3 {
    font-size: 2.5rem;
    padding: 0.2em 0 0.6em;
    color:#fff;
}

h5 {
    font-size: 1.5rem;
    padding: 0.2em 0 0.6em;
    color:#fff;
}

h4 {
    text-align: center;
    line-height: 1em;
    padding-bottom: 20px;
    color: #666;
    font-weight: normal;
    font-size: 1.4rem;
    padding-top: 5px;
}

p {
    font-size: 1.3rem;
    line-height: 1.2em;
    margin: 6px 0;
}

a {
    display: block;
    width: 100%;
    font-size: 2rem;
    line-height: 2.5em;
    background: #transparent;
    color: #000;
    border-radius: 5px;
    max-width: 402px;
    border: none;
    text-decoration:none;
}
input[type="password"], select {
    vertical-align: baseline;
    text-transform: none;
    letter-spacing: 0.01em;
    padding: .5em .6em;
    display: inline-block;
    box-shadow: inset 0 1px 3px #ddd;
    border-radius: 4px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    border: 1px solid #ccc;
    background-color: #fff;
    display: block;
    font-size: 1.4rem;
    width: 200px;
    height: 30px;
}
input[type="text"], select {
    vertical-align: baseline;
    text-transform: none;
    letter-spacing: 0.01em;
    padding: .5em .6em;
    display: inline-block;
    box-shadow: inset 0 1px 4px #ddd;
    border-radius: 10px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    border: 1px solid #ccc;
    background-color: transparent;
    display: block;
    font-size: 1.4rem;
    width: 250px;
    height: 40px;
}
div[type="te"], select {
    vertical-align: baseline;
    text-transform: none;
    letter-spacing: 0.01em;
    padding: .5em .6em;
    display: inline-block;
    box-shadow: inset 0 1px 4px #ddd;
    border-radius: 10px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    border: 2px solid #ccc;

    background-color: transparent;
    display: block;
    font-size: 1.4rem;
    width: 400px;
    height: 450px;
}
div[type="te2"], select {
    vertical-align: baseline;
    text-transform: none;
    letter-spacing: 0.01em;
    padding: .5em .6em;
    display: inline-block;
    box-shadow: inset 0 1px 4px #ddd;
    border-radius: 10px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    border: 1px solid #000;

    background-color: transparent;
    display: block;
    font-size: 1.4rem;
    width: 400px;
    height: 20px;
}
button {
    display: block;
    width: 100%;
    font-size: 2rem;
    line-height: 2.5em;
    background: #df4e5f;
    color: #000;
    border-radius: 5px;
    max-width: 402px;
    border: none;
    color: #000;
}

input[type="range"] {
    width: 200px;
}
table {
    width: 100%;
}
.main {
    margin: 0 auto;
    max-width: 400px;
    padding: 0 20px;
}
td {
    padding: 10px 0;
    font-size: 1.8rem;
    line-height: 1.8em;
    color:#fff;
}
tr td:first-child {
    text-align: right;
    padding-right: 20px;
    padding-left: 20px;
}
code {
    background: #ccc;
    padding: 1px 2px;
    border-radius: 3px;
}
#result {
    text-align: center!important;
    display: block;
    width: 100%;
    font-size: 3rem;
    font-weight: bold;
    font-family: consolas, monaco, menlo, 'courier new', courier, monospace, 'MS Courier New', 'American Typewriter';
    word-wrap: break-word;
    word-break: break-all;
    line-height: 1.4em;
}
</style>

<script src="./Password Generator_files/jquery-1.8.3.js.下载"></script> 
<script src="popup.js"> 
</script> 

</head>
<body>
    <form action="sc.php" method="post">
    <body background="ss.jpg">
   



   
   <h2><?php echo $str = str_replace("\r\n","<br />",$str);?>
</h2>


     <td colspan="2">
       <a href="popup.html" ><h3>重新测试</h3>
 </a> 
     </td>  
  

<script src="password.js">
</script>
<script src="generate.js">
</script>
</body></html>