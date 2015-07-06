function startScript( current_userId) {
	$( document ).ready( readyFunction );

	function readyFunction() {
		$("button").click( function(evnt) {
			var url = $SCRIPT_ROOT + '/answer';

			console.log(current_userId);

			var selectedId = $(this).attr('id');
			var selectedValue = $("select." + selectedId).val();
			$.getJSON( url, {
				id: selectedId,
				value: selectedValue,
				userid: current_userId
				},
				function (data) {
					//Doing the checking and all on server side
					alert(data.score);//Score
					if(data.correct > 0) {
						alert('Correct answer ');
						//var newDiv = "<div>Correct!!</div>";
						//$("<div>Correct!!</div>").hide().appendTo("select." + selectedId).fadeIn("fast");
					}
					else {
						alert('Sorry bro');
					}
				}
			);
			evnt.preventDefault();

			

		});
	}
}