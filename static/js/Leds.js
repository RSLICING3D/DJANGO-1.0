var a = document.getElementById("invisibleZero").value;
var b = document.getElementById("invisibleOne").value;
var c = document.getElementById("invisibleTwo").value;
var d = document.getElementById("invisibleThree").value;
var e = document.getElementById("invisibleFour").value;
var f = document.getElementById("invisibleFive").value;
var g = document.getElementById("invisibleSix").value;
var h = document.getElementById("invisibleSeven").value;
var i = document.getElementById("invisibleEight").value;
var j = document.getElementById("invisibleNine").value;

if (a == "1") {
    setInterval(LedOn0())
} else if(a == "0"){
    setInterval(LedOff0())
}

if (b == "1") {
    setInterval(LedOn1())
} else if(b == "0"){
    setInterval(LedOff1())
}

if (c == "1") {
    setInterval(LedOn2())
} else if(c == "0"){
    setInterval(LedOff2())
}

if (d == "1") {
    setInterval(LedOn3())
} else if(d == "0"){
    setInterval(LedOff3())
}

if (e == "1") {
    setInterval(LedOn4())
} else if(e == "0"){
    setInterval(LedOff4())
}

if (f == "1") {
    setInterval(LedOn5())
} else if(f == "0"){
    setInterval(LedOff5())
}

if (g == "1") {
    setInterval(LedOn6())
} else if(g == "0"){
    setInterval(LedOff6())
}

if (h == "1") {
    setInterval(LedOn7())
} else if(h == "0"){
    setInterval(LedOff7())
}

if (i == "1") {
    setInterval(LedOn8())
} else if(i == "0"){
    setInterval(LedOff8())
}

if (j == "1") {
    setInterval(LedOn9())
} else if(j == "0"){
    setInterval(LedOff9())
}


function LedOff0(){
    var image1 = document.getElementById("Q00-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn0(){
    var image1 = document.getElementById("Q00-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff1(){
    var image1 = document.getElementById("Q01-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn1(){
    var image1 = document.getElementById("Q01-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff2(){
    var image1 = document.getElementById("Q02-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn2(){
    var image1 = document.getElementById("Q02-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff3(){
    var image1 = document.getElementById("Q03-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn3(){
    var image1 = document.getElementById("Q03-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff4(){
    var image1 = document.getElementById("Q04-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn4(){
    var image1 = document.getElementById("Q04-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff5(){
    var image1 = document.getElementById("Q05-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn5(){
    var image1 = document.getElementById("Q05-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff6(){
    var image1 = document.getElementById("Q06-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn6(){
    var image1 = document.getElementById("Q06-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff7(){
    var image1 = document.getElementById("Q07-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn7(){
    var image1 = document.getElementById("Q07-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff8(){
    var image1 = document.getElementById("Q08-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn8(){
    var image1 = document.getElementById("Q08-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}

function LedOff9(){
    var image1 = document.getElementById("Q09-image")
    image1.src = "{% static 'media/Led-Off.png' %}"
}
function LedOn9(){
    var image1 = document.getElementById("Q09-image")
    image1.src = "{% static 'media/Led-ON.png' %}"
}