var transparentDemo = true;
var fixedTop = false;

$(window).scroll(function(e) {
    oVal = ($(window).scrollTop() / 170);
    $(".blur").css("opacity", oVal);
    
});

addgroup = function(name) {
	arr = name.split(', ');
	for (var i = 0; i < arr.length; i++) {
		num = arr[i].split(' - ')[1]
		addcontact(parseInt(num));
	}
}

addcontact = function(num) {
	if ($('#id_phoneNumber').val() != ''){
		$('#id_phoneNumber').val($('#id_phoneNumber').val() + ", " + num);
	}
	else{
		$('#id_phoneNumber').val(num);
	}
}

addtemplate = function(template){
    $('#id_message').val(template);
}