$(document).ready(function() {
	$.ajax({
		url: "data.json",
		dataType: "json",
		success: function(data) {
			$("#name").text(data.name);
			$("#website").html('<a href="' + data.website + '">' + data.website + '</a>');
			$("#school").text(data.school);
			var experienceList = "";
			for (var i = 0; i < data.experience.length; i++) {
				experienceList += "<li><strong>" + data.experience[i].title + "</strong>, " + data.experience[i].company + " (" + data.experience[i].year + ")</li>";
			}
			$("#experience").html(experienceList);
		},
		error: function() {
			alert("Error loading data.");
		}
	});
});
