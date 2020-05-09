  
$(document).ready(function() {

	$('form').on('submit', function(event) {
		
		$.ajax({
			data : {
				search : $('#nameInput').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				$("#contentLink").hide();
			}
			else {
				$('#successAlert').text(data.search).show();
				$('#errorAlert').hide();
				$("#contentLink").attr("href", data.url);
			}	

		});

		event.preventDefault();

	});

});
