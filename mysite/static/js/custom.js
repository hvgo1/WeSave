(function ($) {

	new WOW().init();

	jQuery(window).load(function() { 
		jQuery("#preloader").delay(100).fadeOut("slow");
		jQuery("#load").delay(100).fadeOut("slow");
	});


	//jQuery to collapse the navbar on scroll
	$(window).scroll(function() {
		if ($(".navbar").offset().top > 50) {
			$(".navbar-fixed-top").addClass("top-nav-collapse");
		} else {
			$(".navbar-fixed-top").removeClass("top-nav-collapse");
		}
	});

	//jQuery for page scrolling feature - requires jQuery Easing plugin
	$(function() {
		$('.navbar-nav li a').bind('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1500, 'easeInOutExpo');
			event.preventDefault();
		});
		$('.page-scroll a').bind('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: $($anchor.attr('href')).offset().top
			}, 1500, 'easeInOutExpo');
			event.preventDefault();
		});
	});

	$(document).ready(function(){
		var next = 1;
		$(".add-more").click(function(e){
			e.preventDefault();
			var addto = "#field" + next;
			var addRemove = "#field" + (next);
			next = next + 1;
			var newIn = '<label id="label' + next + '">Wish</label><input autocomplete="off" placeholder="Input estimated cost" class="input form-control" id="field' + next + '" name="field' + next + '"type="text">';
			var newInput = $(newIn);
			var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >-</button></div><div id="field">';
			var removeButton = $(removeBtn);
			$(addto).after(newInput);
			$(addRemove).after(removeButton);
			$("field" + next).attr('data-source',$(addto).attr('data-source'));
			$("#count").val(next);
				$('.remove-me').click(function(e){
					e.preventDefault();
					//var labelNum = this.id.charAt(this.id.length-1);
					var labelNum = this.id.substr(this.id.lastIndexOf("e")+1);
					var labelID = "#label" + labelNum;
					var fieldNum = this.id.substr(this.id.lastIndexOf("e")+1);
					var fieldID = "#field" + fieldNum;
					$(this).remove();
					$(fieldID).remove();
					$(labelID).remove();
				});
		});
	});

})(jQuery);
