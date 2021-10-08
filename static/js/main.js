

var socket = new WebSocket('ws://172.20.108.25:8000/dashboard');

socket.onmessage = function (e){
    var djangoData = JSON.parse(e.data);
    console.log(djangoData);


}
