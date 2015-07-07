function startScript( current_userId, kingScore) {
	$( document ).ready( readyFunction );

	function readyFunction() {
		$("button").click( function(evnt) {
			var url = $SCRIPT_ROOT + '/answer';


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
					$("." + selectedId).hide(1000);
					if(data.score >= kingScore){
						$("#userscore").append('<img src="/static/img/crown.svg" id="crown">');
					}
				}
			);
			evnt.preventDefault();

			

		});
	}
}