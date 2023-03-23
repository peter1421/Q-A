export  function get(url) {
  return new Promise((resolve, reject) => {
    var httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
      alert("Giving up :( Cannot create an XMLHTTP instance");
      return false;
    }
    httpRequest.open("GET", url, true);
    httpRequest.send();
    httpRequest.onload = function () {
      if (alertContents(httpRequest)) {
        resolve(JSON.parse(httpRequest.responseText));
      } else {
        reject(new Error(httpRequest));
      }
    };
  });
}

export function post(url, request) {
  return new Promise((resolve, reject) => {
    var httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
      alert("Giving up :( Cannot create an XMLHTTP instance");
      return false;
    }
    console.log(JSON.stringify(request));
    httpRequest.open("post", url, true);
    httpRequest.setRequestHeader("Content-type", "application/json");
    httpRequest.send(JSON.stringify(request));
    httpRequest.onload = function () {
      if (alertContents(httpRequest)) {
        resolve(JSON.parse(httpRequest.responseText));
        // resolve(JSON.stringify(httpRequest.responseText));
      } else {
        reject(new Error(httpRequest));
      }
    };
  });
}
function alertContents(httpRequest) {
  if (httpRequest.status === 200) {
      return true;
  } else {
      console.log('There was a problem with the request.');
      return false;
  }
}
// export {get, post}
