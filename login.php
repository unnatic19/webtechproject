<?php
$connect = mysqli_connect("localhost","root","","dataset") or die("Cannot Connect");
$name  = $_POST['username'];
$password = $_POST['password'];
$sql = "SELECT * from signup WHERE name = '$name' AND password = '$password';";
$res = mysqli_query($connect,$sql);
if((mysqli_num_rows($res))>0)
{
        echo $row['name'].$row['password'].$row['phonenumber'].$row['email'].$row['country'];
}
else{
    die("Resubmit");
}
       
header("Location: http://localhost/webproj/New%20folder/profile_new.html");
exit;

?>