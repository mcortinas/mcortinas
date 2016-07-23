(function($) {
    "use strict"; 
    $(function() {     	
    	// primary navigation		
    	var winWidth = $(window).width();  
    	if (winWidth > 992) {  	
	    	$('#primary-menu .menu-item-has-children').each(function() {
				$('a:first', this).append('<span class="glyphicon glyphicon-chevron-down"></span>');
			});		    	
    	}
		$('#primary-menu li').hover(function() {
			if (winWidth > 992) {
				if ($(this).hasClass('menu-item-has-children')) {					
					$('ul',this).prepend('<li class="spacer"></li>').fadeIn('fast');					
				}
			}
			}, function() {
				$('ul',this).fadeOut('fast', function() {
				$('.spacer',this).remove();
			});
		});			
		$(window).resize(function() {
			winWidth = $(window).width();
			if (winWidth < 992) {
				$('#primary-menu li ul, #primary-menu li .glyphicon').hide();
			} else {
				$('#primary-menu li .glyphicon').show();
			}
		});	
		if ($('#logo img').length) {
			var logoHeight = $('#logo img').height();
			if (logoHeight > 41) {
				var navMargin = logoHeight / 3.3;
				$('#primary-menu').css('margin-top', navMargin+'px');
			}	
		}			
		// misc
		$('#primary-sidebar .widget:first').addClass('first');
		$('.widget li:last-child, #primary-menu li:last-child').addClass('last');
		$('.wp-caption').removeAttr('style');	
		$('.post-tags span:last-child').remove();
 	}); 
}(jQuery));