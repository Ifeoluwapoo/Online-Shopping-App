
        $(function () {

            /* Functions */
          
            var loadForm = function () {
              var btn = $(this);
              $.ajax({
                url: btn.attr("data-url"),
                type: 'get',
                beforeSend: function () {
                  $("#myModalEdit").modal("show");
                },
                success: function (data) {
                    var result = data;
                  $("#myModalEdit").html(result);
                }
              });
            };
          
              var loadViewProductForm = function () {
              var btn = $(this);
              $.ajax({
                url: btn.attr("data-url"),
                type: 'get',
                beforeSend: function () {
                  $("#myModalView").modal("show");
                },
                success: function (data) {
                    var result = data;
                  $("#myModalView").html(result);
                }
              });
            };

          
            var loadDeleteForm = function () {
              var btn = $(this);
              $.ajax({
                url: btn.attr("data-url"),
                type: 'get',
                beforeSend: function () {
                  $("#myModalDelete").modal("show");
                },
                success: function (data) {
                    var result = data;
                  $("#myModalDelete").html(result);
                }
              });
            };
          

                      /* Functions Saving Edited Content on Form */

                      var saveForm = function () {
                        var form = $(this);
                            $.ajax({
                                   url: form.attr("action"),
                                   data: form.serialize(),
                                    type: form.attr("method"),
                                    success: function (data) {
                                        var result = data;
                                            if (data != null) {
                                                   //$("#myModalEdit").hide();
                                                   $('.modal').remove();
                                                    $('.modal-backdrop').remove();
                                                    $('body').removeClass( "modal-open" );
                                                    $('#myPage').html(function () {
                                                      location.reload(true); 
                                                  });
                                                    //$("#productTable").html();myPage
                                                    console.log("hi");
                                                    //RefreshTable();
                                                   //alert("Product is Edited!");
                                                 
                                            }
                                            else {
                                                   $("#myModalEdit").html(result);
                                            }
                                    },
                                    error: function(){
                                        alert("Something went wrong");
                                    }
                            });
                            return false;
                        };
          
                       // function RefreshTable() {
                        //    $( "#productTable" ).load( );
                       // }
                     
                       // $("#refresh-btn").on("click", RefreshTable);


                       var deleteForm = function () {
                        var form = $(this);
                            $.ajax({
                                   url: form.attr("action"),
                                   data: form.serialize(),
                                    type: form.attr("method"),
                                    success: function (data) {
                                        var result = data;
                                        console.log(data);
                                            if (data != null) {
                                                   //$("#myModalDelete").hide();
                                                   $('.modal').remove();
                                                    $('.modal-backdrop').remove();
                                                    $('body').removeClass( "modal-open" );
                                                    $('#myPage').html(function () {
                                                      location.reload(true); 
                                                  });
                                                    //$("#productTable").html();myPage
                                                    console.log("hi");
                                                 
                                            }
                                            else {
                                                   $("#myModalDelete").html(result);
                                            }
                                    },
                                    error: function(){
                                        alert("Something went wrong");
                                    }
                            });
                            return false;
                        };
          
          
            /* Binding */
          
            // Update book
            $("#productTable").on("click", "#productEdit", loadForm);
            $("#myModalEdit ").on("submit", "#product_update_form", saveForm);

            //Display view details.
            $("#productTable").on("click", "#productView", loadViewProductForm);
            
            //Display delete modal
            $("#productTable").on("click", "#productDelete", loadDeleteForm);
            $("#myModalDelete ").on("submit", "#product_delete_form", deleteForm);
          });