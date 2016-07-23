/* ===== 

You are free to modify this file but you should really create a folder in your
themes directory called (exactly) multi-column-tag-map and then copy this file 
to that folder. Make your edits to the copy. If you make your edits to the 
file in the plugins folder, all your edits will be overwritten if you update.

===== */ 

/* =====  version 12.0.4 ===== */ 

/* ===== equalize ===== */

(function (jQuery) {
	jQuery.fn.mctagmapEqualHeights = function() {
		var max_height = 0;
		var currentHeight = 0;
		this.each(function() {
			currentHeight = jQuery(this).height();
			if(currentHeight > max_height) {
				max_height = currentHeight;
			}
		});
		this.each(function() {
			jQuery(this).delay(0).animate({'min-height' : max_height}, 0);
		});
	};
})(jQuery);

jQuery(document).ready(function(){
								
/* ==== toggle ==== */
  jQuery('a.less').hide();
  jQuery('ul.links li.hideli').hide();
  jQuery('ul.links li.morelink').show();
  jQuery(' a.more').click(function() {
	jQuery(this).parent().siblings('li.hideli').slideToggle('fast');
	 jQuery(this).parent('li.morelink').children('a.less').show();
	 jQuery(this).hide();
  });
    jQuery('a.less').click(function() {
	jQuery(this).parent().siblings('li.hideli').slideToggle('fast');
	 jQuery(this).parent('li.morelink').children('a.more').show();
	 jQuery(this).hide();
  });

/* ===== equalize ===== */
	var numberOfHoldLeftChildren = 0;
	var numberOfTagIndex = jQuery('.mcEqualize .holdleft').eq(0).children('.tagindex').length;
	while(numberOfHoldLeftChildren <= numberOfTagIndex){
		jQuery('.mcEqualize .holdleft').children('.tagindex:nth-child('+numberOfHoldLeftChildren+')').mctagmapEqualHeights();
	    numberOfHoldLeftChildren++;
	}

/* ==== test purposes 
jQuery('.tagindex').css({'background-color' : '#D9CBDB', 'margin-bottom' : '10px'});
==== */
  
});