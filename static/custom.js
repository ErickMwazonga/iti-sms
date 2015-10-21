var transparentDemo = true;
var fixedTop = false;

$(window).scroll(function(e) {
    oVal = ($(window).scrollTop() / 170);
    $(".blur").css("opacity", oVal);
    
});


autofill = function() {
	console.log('wooroo');
	//$.getJSON('/api/autofill', $('#id_phoneNumber').value), function(data) {

	//}
}