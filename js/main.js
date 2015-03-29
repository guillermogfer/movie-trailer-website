// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
  });

// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});

$(document).ready(function () {
    // Animate in the movies when the page loads
    $('.movie-tile').hide().first().show("fast", function showNext() {
        $(this).next("div").show("fast", showNext);

        // Fire 'dotdotdot' plugin in each div appearance. Firing once at the end produces ugly lines reorder effect
        $('.ellipsis').dotdotdot({
            watch: 'window'
        });

        // Determine if last child
        if($(this).is(":last-child")){
            $('.ellipsis-title').each(function () {
                // Remove all titles tooltips except for a possible clipped title
                if ($('h2', this).text().indexOf("...") == -1) {
                    $(this).removeAttr('title');
                }
            });

            // Fire bootstrap tooltip
            $('[data-toggle="tooltip"]').tooltip();
        }
    });

    // Activate star rating plugin
    $('.rb-rating').rating({
        showCaption: true,
        defaultCaption: '{rating} / 5',
        starCaptions: {},
        showClear: false,
        min: 0,
        max: 5,
        step: 0.1,
        size: 'xs',
        stars: 5,
        disabled: false,
        readonly: true,
        starCaptionClasses: function(val) {
            if (val>= 0 && val<2) {
                return 'label label-danger';
            }
            else if (val>=2 && val<4) {
                return 'label label-primary';
            }
            else {
                return 'label label-success outstanding';
            }
        }
    });

    // Set events to toggle poster image and overview
    $('.poster').mouseenter(function() {
        $(this).siblings().fadeIn("slow");
    });
    $('.inner').mouseleave(function() {
        $(this).hide();
    });
});