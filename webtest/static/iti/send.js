$(document).ready(function(){
	$(".cashtype").change(function(){
		if ($(".cashtype").val() == 'USD'){
			$("#amount_label").text("Amount: $")
		}
		if ($(".cashtype").val() == 'EUR'){
			$("#amount_label").text("Amount: €")
		}
		if ($(".cashtype").val() == 'CNY' || $(".cashtype").val() == 'JPY'){
			$("#amount_label").text("Amount: ¥")
		}
	});
	/*$("#submit1").click(function(){
	alert("123");
	});*/
});