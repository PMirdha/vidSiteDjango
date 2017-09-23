$(document).ready(function() {	
	$(".add_button").click(function() {
		//Start Ajax request
		var item_id=$(this).attr('id');
		var item_title=$(this).attr('value');
		var payload={"item_id":item_id,"item_title":item_title};
		//alert(item_title);
		var self_var=this;
		$.get("",
			payload,
			function (data) {
				if($(''))

				$("#last_summary").before("<input type='text' name='audio_name'"+
								"id='"+item_id+"'"+
								" readonly='true' value='"+
								item_title+
								"' >");
			});
	});
	function submitOk() {
		return false;
	}
	

});