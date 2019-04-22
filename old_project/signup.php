<?php
if(isset($_POST['name']) && isset($_POST['password']) && isset($_POST['email']) && isset($_POST['phonenumber']) && isset($_POST['country'])) {
    $data = $_POST['name'] . '-' . $_POST['password']. '-' . $_POST['email']. '-' . $_POST['phonenumber']. '-' . $_POST['country'] . "\r\n";
    if(!preg_match('/^.*(?=.{5,})(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*$/',$_POST['password']))
    {
        die("Error: Enter the password again");
    }
    $connect = mysqli_connect("localhost","root","","dataset") or die("Cannot Connect");

    $name  = $_POST['name'];
    $password = $_POST['password'];
    $email = $_POST['email'];
    $phonenumber=$_POST['phonenumber'];
    $country=$_POST['country'];
    $sql="INSERT INTO signup(name, password, email, phonenumber, country) VALUES('$name','$password','$email','$phonenumber','$country'); ";
    $res=mysqli_query($connect,$sql);

       
    header("Location: http://localhost/webproj/New%20folder/profile_new.html");
    exit;
}
?>