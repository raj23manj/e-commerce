$(document).on('click', '#add_dynamic_product', function () {
  $.ajax({
    url: '/shop/dynamic_content',
    data: {
    },
    dataType: 'text',
    success: function (data) {
      $('#products-container').append(data);
    }
  });

});