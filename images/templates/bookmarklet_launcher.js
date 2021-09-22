(function() {
	if (window.myBookmarklet !== undefined){
		myBookmarklet()
	}
	else {
		document.body.appendChild(document.createElement('script')).src='https://3190-85-26-234-182.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
	}
})();