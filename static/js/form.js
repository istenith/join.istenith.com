$(document).ready(function(){

	var current_fs, next_fs, previous_fs;
	
	// No BACK button on first screen
	if($(".show").hasClass("first-screen")) {
	$(".prev").css({ 'display' : 'none' });
	}
	
	// Next button
	$(".next-button").click(function(){
	
	current_fs = $(this).parent().parent();
	next_fs = $(this).parent().parent().next();
	
	$(".prev").css({ 'display' : 'block' });
	
	$(current_fs).removeClass("show");
	$(next_fs).addClass("show");
	
	$("#progressbar li").eq($(".card2").index(next_fs)).addClass("active");
	
	current_fs.animate({}, {
	step: function() {
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	
	next_fs.css({
	'display': 'block'
	});
	}
	});
	});
	
	// Previous button
	$(".prev").click(function(){
	
	current_fs = $(".show");
	previous_fs = $(".show").prev();
	
	$(current_fs).removeClass("show");
	$(previous_fs).addClass("show");
	
	$(".prev").css({ 'display' : 'block' });
	
	if($(".show").hasClass("first-screen")) {
	$(".prev").css({ 'display' : 'none' });
	}
	
	$("#progressbar li").eq($(".card2").index(current_fs)).removeClass("active");
	
	current_fs.animate({}, {
	step: function() {
	
	current_fs.css({
	'display': 'none',
	'position': 'relative'
	});
	
	previous_fs.css({
	'display': 'block'
	});
	}
	});
	});
	
	});