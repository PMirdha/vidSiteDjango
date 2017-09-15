$(document).ready(function() {	
	$(".add_button").click(function() {
		//alert($(this).attr('name'));
		//Start Ajax request
		var self_var=this;
		$.get("",
			{"gen_it_id":$(this).attr('value')},
			function (data) {
				//alert(data);
				//var n = data;
				$("#last_summary").before("<input type='text' name='audio_name"+
								//$(self_var).attr('value')+
								//n+
								"' readonly='true' value='"+
								$(self_var).attr('id')+
								"' >");
			});
	});
	function submitOk() {
		return false;
	}
	

});