function showLoading(){
  loading = document.getElementById("loading");
  info = document.getElementById("info");
  real = document.getElementById("real");
  fake = document.getElementById("fake");
  error = document.getElementById("error");
  info.style.opacity = 0;
  real.style.opacity = 0;
  fake.style.opacity = 0;
  error.style.opacity = 0;
  loading.style.opacity = 1;
}
function showReal(){
  body = document.body;
  body.style.backgroundColor = "#009900";
  real = document.getElementById("real");
  loading.style.opacity = 0;
  real.style.opacity = 1;
}
function showFake(){
  body = document.body;
  body.style.backgroundColor = "#c00000";
  fake = document.getElementById("fake");
  loading.style.opacity = 0;
  fake.style.opacity = 1;
}
function showError(message){
  body = document.body;
  body.style.backgroundColor = "#444";
  error = document.getElementById("error");
  loading.style.opacity = 0;
  error.style.opacity = 1;
  if (message){
    errorMessageSpan = document.getElementById('errorMessage');
    errorMessageSpan.innerText = message;
  }
}

function refreshInputField(input_field, url){
  input_field.focus();
  input_field.blur();
  input_field.focus();
  input_field.placeholder = url;
  input_field.value = '';
}

function handleForm(){
  showLoading();
  var originalUrl = document.getElementById('url').value;
  var url = originalUrl;
  if (url.length == 0){
    showError("Make sure you have entered a valid URL.");
    return;
  }
  if (url.indexOf("http") == -1){
    url = "http://".concat(url);
  }
  var l = document.createElement("a");
  l.href = url;
  shortenedURL = l.protocol + "//" + l.hostname;

  console.log(shortenedURL);

  var input_field = document.getElementById('url');

  var request = new XMLHttpRequest();
  request.open('POST', 'https://us-central1-fake-news-ai.cloudfunctions.net/detect', true);
  request.setRequestHeader('Content-type','application/json; charset=utf-8');
  request.onload = function() {
    if (this.status >= 200 && this.status < 400) {
      var resp = JSON.parse(this.responseText);
      console.log(resp);
      refreshInputField(input_field, originalUrl);

      if (resp['fake']) {
        showFake();
      } else {
        showReal();
      }
    } else {
      console.log("Server Error");
      refreshInputField(input_field, originalUrl);
      showError("There was an error reaching the site. Make sure the URL is valid.");
    }
  };

  request.onerror = function() {
    console.log("Connection Error");
    refreshInputField(input_field, originalUrl);
    showError("There was an error reaching the site. Make sure the URL is valid.");
  };

  request.send(JSON.stringify({"url": url}));
}
