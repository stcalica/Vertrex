/*
	The Base JS that will be loaded with every page
	This is where Facebook SDK will be called for each page
	


*/

$(document).ready(function(){

	$.ajaxSetup({ cache: true }); 
	$.getScript('//connect.facebook.net/en_US/sdk.js', function(){
		FB.init({
			appId: '',
 			version: 'v2.5'
		});
		$('#loginbutton, #feedbutton').removeAttr('disabled'); //does not disable buttons anymore 
		FB.getLoginStatus(updateStatusCallback); //need to make a function updateStatusCallback 
	})

});
