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
					var scoreElement = document.getElementById("userscore");
					scoreElement.text = 'Your SCORE is ' + data.score;
					
				}
			);
			evnt.preventDefault();

			

		});
	}
}