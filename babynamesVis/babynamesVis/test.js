(function($) {
  
  // $(document).ready(function() {

  'use strict';
  
  // cache the desired selectors
  var $body    = $('body');
  var $list    = $('.m-info');
  var $message = $('.m-message');
  var $modal   = $('.modal');
  var $loader  = $('.loader');
  var $framework;

  $('.boxes a').on('click', function(e) {

    // prevent the default behavior of the link
    e.preventDefault();

    // get the text of the link
    $framework = $(this).text();

    // execute the AJAX request
    $.ajax({
      // where the data live
      url: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/Demo.json',
      
      // second url which contains the word "Foundation2" instead of "Foundation"
      // url: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/Demo2.json',
      
      // third url which is an empty array
      // url: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/Demo3.json',
      
      // fourth url which leads to an error
      // url: 'https://s3-us-west-2.amazonaws.com/s.cdpn.io/162656/demo.json',
      
      // what is their type
      dataType: 'json',
      // show the loader before making the request 
      beforeSend: function() {
        $loader.show();
      }
    }).done(successFunction)
      .fail(failFunction)
      .always(alwaysFunction);
  }); 

  
  // success function
  function successFunction(data) {
    // if data exists
    if (data.length > 0) {
      // loop through them
      for (var i = 0; i < data.length; i++) {
        // hide the list in case there isn't any propery with name equal to the text value 
        // check if the text value of the link is equal to the "name" property
        if ($framework === data[i].name) { 
          // show the list and hide the message
          $list.show();
          $message.hide();
          // populate the corresponding list items
          $list.find('li:nth-of-type(2)').text($framework);
          $list.find('li:nth-of-type(4)').text(data[i].currentVersion);
          $list.find('li:nth-of-type(6)').text(data[i].numberOfStars);
          $list.find('li:nth-of-type(8)').html('<a href="' + data[i].url + '" target="_blank">' + data[i].url + '</a>');  
          // terminate the loop and not scan all the file
          break;
        } else {
          // otherwise hide the list and show the corresponding message 
          $list.hide();
          $message.show().text('No data received for this framework!');
        }
      } 
    } else {
      // otherwise hide the list and show the corresponding message 
      $list.hide();
      $message.text('No data received from your respose!');
    }
  }
  
  
  // fail function
  function failFunction(request, textStatus, errorThrown) {
    // hide the list and show the corresponding message
    $list.hide();
    $message.text('An error occurred during your request: ' + request.status + ' ' + textStatus + ' ' + errorThrown);
  }
  
  
  // always function
  function alwaysFunction() {
    // hide the loader and show the modal
    $loader.hide();
    $modal.addClass('active');
    $body.css('overflow', 'hidden');
  }
  
  
  // close the button
  $modal.find('button').on('click', function() {
    $body.css('overflow', 'visible');
    $(this).parent().removeClass('active');
  });
  
  // });

})(jQuery);