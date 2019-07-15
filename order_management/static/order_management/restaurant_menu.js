
$(document).ready( function () {
    $('#restaurantMenu').DataTable();
} );

$(function () { 
    $(".create-restaurant").modalForm({formURL: '{% url "order_management:create_restaurant_menu" %}' });

    $(".update-restaurant-menu").each(function () {
      $(this).modalForm({formURL: $(this).data('id')});
      });

     $(".delete-restaurant-menu").each(function () {
      $(this).modalForm({formURL: $(this).data('id')});
      });
  });
