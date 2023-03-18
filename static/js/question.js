var dataUrl = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=6"
var xhr = new XMLHttpRequest()
xhr.open('GET', dataUrl, true)
xhr.send()
xhr.onload = function () {
    var data = JSON.parse(this.responseText);
    console.log(data);
}