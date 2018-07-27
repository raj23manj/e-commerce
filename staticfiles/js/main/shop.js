$(document).on('click', '#add_dynamic_product', function () {
  $.ajax({
    url: '/shop/dynamic_content/',
    data: {
    },
    dataType: 'json',
    success: function (data) {
      console.log(data);
    }
  });

});