$(document).ready(function(){
	console.log('ready');
  /*Formatear valores numericos para que se vean como pesos*/
  var formatNumber = {
       separador: ".", // separador para los miles
       sepDecimal: ',', // separador para los decimales
         formatear:function (num){
         num +='';
         var splitStr = num.split('.');
         var splitLeft = splitStr[0];
         
         var regx = /(\d+)(\d{3})/;
         while (regx.test(splitLeft)) {
         splitLeft = splitLeft.replace(regx, '$1' + this.separador + '$2');
         }
         return this.simbol + splitLeft;
         },
       new:function(num, simbol){
       this.simbol = simbol ||'';
       return this.formatear(num);
       }
    }
    var valor = $('#valorNumerico').text();//ganancia 
    var valor2 = $('#valorNumerico2').text();//gasto
    $('#valorNumerico').text(formatNumber.new(valor, "$"));
    $('#valorNumerico2').text(formatNumber.new(valor2, "$"));
    var totalActual = valor - valor2;
    $('#totalActual').text(formatNumber.new(totalActual, "$"));

  /*focus del click del mouse*/
	$('#mensaje').on('shown.bs.modal', function(){
	   $('#titulo').focus();
	})
  /*este focus se uso en la misma ventada de modificar y eliminar*/
  $('#mensaje').on('shown.bs.modal', function(){
     $('#AgregarTitulo').focus();
  })

	$('#ventana1').on('shown.bs.modal', function(){
		  $('#fecha').focus();
	})

	$('#ventana2').on('shown.bs.modal', function(){
	   $('#fecha_ganancia').focus();
	})

	$('#ventana3').on('shown.bs.modal', function(){
	   $('#fecha_gasto').focus();
	})

/*---------validadicones de errores------------------*/
$("#AgregarTitulo, #titulo").keyup(function(){
        if( $(this).val() != "" ){
            $(".text-danger").fadeOut();
            $( "#errorForm" ).removeClass( "has-error" );

            $( "#errorForm3" ).removeClass( "has-error" );
            return false;
        }
});

/*Guardar notas rapidas con ajax*/
    $('#agregarNota').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        if( $("#AgregarTitulo").val() == "" ){
            $(".text-danger").remove();
            $("#AgregarTitulo").focus().after("<p class='text-danger'>Ingrese un titulo por favor.</p>" );
            $( "#errorForm" ).addClass( "has-error" );
            return false;
        }else{
          if( $("#titulo").val() == "" ){
            $(".text-danger").remove();
            $("#titulo").focus().after("<p class='text-danger'>Ingrese un titulo por favor.</p>" );
            $( "#errorForm3" ).addClass( "has-error" );
            return false;
          }
        }
				$.ajax({
              beforeSend: function(){

              },
              url: '/agregarAjax/',
              type: 'POST',
              data: $('#agregar_nota_form').serialize(),
              success: function(data){
                //console.log(resp);
                if(data == "Error"){
                 	 console.log('Algo salio mal :(')
                }else{
                   $('#agregar_nota_form')[0].reset();//limpiamos el formulario
                   $('#mensaje').modal('hide')
                   var html = "";
                   var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="id_nota">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.titulo+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarNota"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarNota"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };
                  /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                   $('#FechaTituloNota').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeExitoso .alert").fadeOut(6000).fadeIn(6000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+'X'+'</button>'+'<strong>'+'Nota Guardada '+'</strong>'+' La nota se guardo Correctamente.'+'</div>';
                   $('#mensajeExitoso').html(exito);
                   /*$.getScript('/{{STATIC_URL}}/js/script.js/');*/
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
		});/*Cierre de la funtion click*/

/*--------validaciones----------*/
   $("#valorGanancia, #valorGasto").keyup(function (){
            this.value = (this.value + '').replace(/[^0-9]/g, '');
           if( $(this).val() != "" ){
                    $(".text-danger").fadeOut();
                    $( "#errorForm" ).removeClass( "has-error" );
                    $( "#errorForm2" ).removeClass( "has-error" );
                    return false;
            }
    });

    /*Agregar ganancia y gasto al mismo tiempo */
    $('#agregarGananciGasto').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        if( $("#valorGanancia").val() == "" ){
            /*$(".text-danger").remove();*/
            $("#valorGanancia").focus().after("<p class='text-danger'>Ingrese un valor numérico por favor.</p>" );
            $( "#errorForm" ).addClass( "has-error" );
            return false;
        }else{
          if( $("#valorGasto").val() == "" ){
              /*$(".text-danger").remove();*/
              $("#valorGasto").focus().after("<p class='text-danger'>Ingrese un valor numérico por favor.</p>" );
              $( "#errorForm2" ).addClass( "has-error" );
              return false;
          }
        }
        $.ajax({
              beforeSend: function(){

              },
              url: '/registrar/',
              type: 'POST',
              data: $('#agregar_gananciaygasto_form').serialize(),
              success: function(data){
                if(data == "Error"){
                   console.log('Algo salio mal :(')
                }else{
                  var ganancia = $('#valorGanancia').val();//ganancia
                  var gasto = $('#valorGasto').val();//gasto
                  var valor = $('#ocultoGanancia').text();//ganancia 
                  var valor2 = $('#ocultoGasto').text();//gasto
                  $('#ventana1').modal('hide')//ocultamos el modal 
                  /*$('#FechaGananciasGastos').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  var contador = $('#contador').text();
                  //console.log(datos);
                  
                  gananciaParse = parseInt(ganancia);
                  gastoParse = parseInt(gasto);
                  valorParse = parseInt(valor);
                  valor2Parse = parseInt(valor2);
                  var sumaGanancias = valorParse + gananciaParse;
                  var sumaGastos = valor2Parse + gastoParse;
                  totalActual = sumaGanancias - sumaGastos;
                  $('#ocultoGanancia').text(sumaGanancias);
                  $('#ocultoGasto').text(sumaGastos);
                  $('#valorNumerico').text(formatNumber.new(sumaGanancias, "$"));
                  $('#valorNumerico2').text(formatNumber.new(sumaGastos, "$"));
                  $('#totalActual').text(formatNumber.new(totalActual, "$"));
                  $('#agregar_gananciaygasto_form')[0].reset();//borramos los datos del form 
                  //console.log(contador);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="idregistro">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.ganancia+'</td><td>'+
                                        datos[i].fields.gasto+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarRegistro"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarRegistro"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                     /*contador++;*/
                  };               
                  $('#FechaGananciasGastos').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeExitoso .alert").fadeOut(6000).fadeIn(6000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Ganancia Y Gasto '+'</strong>'+' La Ganancia y el Gasto se Guardo Correctamente.'+'</div>';
                   $('#mensajeExitoso').html(exito);//mensaje de exito
                 contador++;
                   /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                 console.log(contador);
                 if(contador>10){
                     // console.log('poraca paso');
                      var paginacion = '<nav class="pagination" style="display: none;">'+
                                          '<span class="step-links"> {{ datos.next_page_number }}'+
                                              '{% if datos.has_next %}'+
                                                  '<a id="siguiente" href="?page=0">next</a>'+
                                              '{% endif %}datos'+
                                          '</span>'+
                                      '</nav>';
                      $('#pag').html(paginacion);
                      $('#contador').text(contador);
                  }else{
                      $('#contador').text(contador);
                      $('.pagination').remove();
                  }
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
      });/*Cierre de la funtion click*/

/*----------validaciones-------------*/
    $("#valorGanancia2, #valorGasto3").keyup(function (){
            this.value = (this.value + '').replace(/[^0-9]/g, '');
           if( $(this).val() != "" ){
                    $(".text-danger").fadeOut();
                    $( "#errorForm4" ).removeClass( "has-error" );
                    $( "#errorForm5" ).removeClass( "has-error" );
                    return false;
            }
    });

    /*Agregar solo ganancia*/
    $('#agregarGanancia').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        /*-----validamos----*/
        if( $("#valorGanancia2").val() == "" ){
            /*$(".text-danger").remove();*/
            $("#valorGanancia2").focus().after("<p class='text-danger'>Ingrese un valor numérico por favor.</p>" );
            $( "#errorForm4" ).addClass( "has-error" );
            return false;
        }
        $.ajax({
              beforeSend: function(){

              },
              url: '/registrar/',
              type: 'POST',
              data: $('#agregar_ganancia_form').serialize(),
              success: function(data){
               // console.log(resp);
                if(data == "Error"){
                   console.log('Algo salio mal :(')
                }else{
                  var ganancia = $('#valorGanancia2').val();//ganancia
                  var gasto = $('#valorGasto2').val();//gasto
                  var valor = $('#ocultoGanancia').text();//ganancia 
                  var valor2 = $('#ocultoGasto').text();//gasto
                  $('#ventana2').modal('hide')//ocultamos el modal 
                  /*$('#FechaGananciasGastos').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  var contador = $('#contador').text();
                    //console.log(datos);
                  gananciaParse = parseInt(ganancia);
                  gastoParse = parseInt(gasto);
                  valorParse = parseInt(valor);
                  valor2Parse = parseInt(valor2);
                  var sumaGanancias = valorParse + gananciaParse;
                  var sumaGastos = valor2Parse + gastoParse;
                  totalActual = sumaGanancias - sumaGastos;
                  $('#ocultoGanancia').text(sumaGanancias);
                  $('#ocultoGasto').text(sumaGastos);
                  $('#valorNumerico').text(formatNumber.new(sumaGanancias, "$"));
                  $('#valorNumerico2').text(formatNumber.new(sumaGastos, "$"));
                  $('#totalActual').text(formatNumber.new(totalActual, "$"));
                  $('#agregar_ganancia_form')[0].reset();//borramos los datos del form 
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="idregistro">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.ganancia+'</td><td>'+
                                        datos[i].fields.gasto+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarRegistro"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarRegistro"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };          
                  $('#FechaGananciasGastos').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeExitoso .alert").fadeOut(6000).fadeIn(6000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Ganancia'+'</strong>'+' La Ganancia se Guardo Correctamente.'+'</div>';
                   $('#mensajeExitoso').html(exito);//mensaje de exito
                   contador++;
                   /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                   console.log(contador);
                   if(contador>10){
                       // console.log('poraca paso');
                        var paginacion = '<nav class="pagination" style="display: none;">'+
                                            '<span class="step-links"> {{ datos.next_page_number }}'+
                                                '{% if datos.has_next %}'+
                                                    '<a id="siguiente" href="?page=0">next</a>'+
                                                '{% endif %}datos'+
                                            '</span>'+
                                        '</nav>';
                        $('#pag').html(paginacion);
                        $('#contador').text(contador);
                    }else{
                        $('#contador').text(contador);
                        $('.pagination').remove();
                    }
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
    });/*Cierre de la funtion click*/

 /*Agregar solo gasto*/
    $('#agregarGasto').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        /*-----validamos----*/
        if( $("#valorGasto3").val() == "" ){
            /*$(".text-danger").remove();*/
            $("#valorGasto3").focus().after("<p class='text-danger'>Ingrese un valor numérico por favor.</p>" );
            $( "#errorForm5" ).addClass( "has-error" );
            return false;
        }
        $.ajax({
              beforeSend: function(){

              },
              url: '/registrar/',
              type: 'POST',
              data: $('#agregar_gasto_form').serialize(),
              success: function(data){
               // console.log(resp);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                  var ganancia = $('#valorGanancia3').val();//ganancia
                  var gasto = $('#valorGasto3').val();//gasto
                  var valor = $('#ocultoGanancia').text();//ganancia oculta
                  var valor2 = $('#ocultoGasto').text();//gasto oculto
                  $('#ventana3').modal('hide')//ocultamos el modal 
                  /* $('#FechaGananciasGastos').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  var contador = $('#contador').text();
                    //console.log(datos);
                  gananciaParse = parseInt(ganancia);
                  gastoParse = parseInt(gasto);
                  valorParse = parseInt(valor);
                  valor2Parse = parseInt(valor2);
                  var sumaGanancias = valorParse + gananciaParse;
                  var sumaGastos = valor2Parse + gastoParse;
                  totalActual = sumaGanancias - sumaGastos;
                  $('#ocultoGanancia').text(sumaGanancias);
                  $('#ocultoGasto').text(sumaGastos);
                  $('#valorNumerico').text(formatNumber.new(sumaGanancias, "$"));
                  $('#valorNumerico2').text(formatNumber.new(sumaGastos, "$"));
                  $('#totalActual').text(formatNumber.new(totalActual, "$"));
                  $('#agregar_gasto_form')[0].reset();//borramos los datos del form 
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="idregistro">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.ganancia+'</td><td>'+
                                        datos[i].fields.gasto+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarRegistro"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarRegistro"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };          
                  $('#FechaGananciasGastos').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeExitoso .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Gasto'+'</strong>'+' El Gasto se Guardo Correctamente.'+'</div>';
                  $('#mensajeExitoso').html(exito);//mensaje de exito
                   contador++;
                     /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                   console.log(contador);
                   if(contador>10){
                       // console.log('poraca paso');
                        var paginacion = '<nav class="pagination" style="display: none;">'+
                                            '<span class="step-links"> {{ datos.next_page_number }}'+
                                                '{% if datos.has_next %}'+
                                                    '<a id="siguiente" href="?page=0">next</a>'+
                                                '{% endif %}datos'+
                                            '</span>'+
                                        '</nav>';
                        $('#pag').html(paginacion);
                        $('#contador').text(contador);
                    }else{
                        $('#contador').text(contador);
                        $('.pagination').remove();
                    }
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
    });/*Cierre de la funtion click*/


/*_____________________________________________________________________________________________*/
/*modificar notas rapidas*/
  $('#modificar').on('shown.bs.modal', function(){
     $('#titulo').focus();
  })

 //Extraer los datos de la tabla para mostrarlos en el form
  $('#FechaTituloNota' ).on("click","#modificarNota",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');

      //alert($(this).attr('href'));
      //estraemos los campos.
      $('#idnota').val($(this).parent().parent().children('td:eq(0)').text());
      $('#titulo').val($(this).parent().parent().children('td:eq(2)').text());
      $('#nota').val($(this).parent().parent().children('td:eq(3)').text());
      //var url= $(this).attr('href');
  });

  $('#clickModificarNota').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/modificarNota/',
              type: 'POST',
              data: $('#modificar_nota_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#modificar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="id_nota">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.titulo+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarNota"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarNota"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };                  
                  $('#FechaTituloNota').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Editado'+'</strong>'+' La nota se modifico Correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
    });/*Cierre de la funtion click*/


/*______________________________________________________________________________________*/
/*Elminar las notas rapidas */
//Extraer los datos de la tabla para mostrarlos en el form
  $('#FechaTituloNota').on("click","#eliminarNota",function(e){
      /*e.preventDefault();*/
      console.log('poraca pasamos bien.');
      //extraemos el id de la nota que vamos a eliminar
      $('#ideliminar').val($(this).parent().parent().children('td:eq(0)').text());
      $("#titulo_eliminar").html($(this).parent().parent().children('td:eq(2)').text());
  });

   $('#clickEliminarNota').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/eliminarNota/',
              type: 'POST',
              data: $('#eliminar_nota_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#eliminar_nota_form')[0].reset();//borramos los datos del form 
                 $('#eliminar').modal('hide')//ocultamos el modal 
              /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="id_nota">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.titulo+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarNota"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarNota"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };
                  $('#FechaTituloNota').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Eliminado'+'</strong>'+' La nota se eliminino Correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
    });/*Cierre de la funtion click*/

/*_____________________________________________________________________________________________________________*/

//modificar registros de las GANANCIAS Y LOS GASTOS
$('#modificar').on('shown.bs.modal', function(){
     $('#fechaModificar').focus();
})

//Extraer los datos de la tabla para mostrarlos en el form
$('#FechaGananciasGastos' ).on("click","#modificarRegistro",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');

      //alert($(this).attr('href'));
      //estraemos los campos.
      $('#id_registro').val($(this).parent().parent().children('td:eq(0)').text());
      $('#fechaModificar').val($(this).parent().parent().children('td:eq(1)').text());
      $('#gananciaMod').val($(this).parent().parent().children('td:eq(2)').text());
      $('#gastoMod').val($(this).parent().parent().children('td:eq(3)').text());
      $('#notaMod').val($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

/*modificamos todos los registros ganancias y gastos*/
$('#clickModificarRegistro').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/modificar/',
              type: 'POST',
              data: $('#modificar_registro_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                $('#modificar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  var contador = $('#contador').text();
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="idregistro">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.ganancia+'</td><td>'+
                                        datos[i].fields.gasto+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarRegistro"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarRegistro"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };                  
                  $('#FechaGananciasGastos').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Editado'+'</strong>'+' El registro se modifico correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                  
                   /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                 console.log(contador);
                 if(contador>10){
                     // console.log('poraca paso');
                      var paginacion = '<nav class="pagination" style="display: none;">'+
                                          '<span class="step-links"> {{ datos.next_page_number }}'+
                                              '{% if datos.has_next %}'+
                                                  '<a id="siguiente" href="?page=0">next</a>'+
                                              '{% endif %}datos'+
                                          '</span>'+
                                      '</nav>';
                      $('#pag').html(paginacion);
                      $('#contador').text(contador);
                  }else{

                      $('#contador').text(contador);
                      $('.pagination').remove();
                  }
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/

/*ELIMINAMOS LOS REGISTROS GANANCIAS Y GASTOS*/
//Extraer los datos de la tabla para mostrarlos en el form
$('#FechaGananciasGastos' ).on("click","#eliminarRegistro",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');
      //alert($(this).attr('href'));
      //estraemos los campos.
    $('#id_eliminar').val($(this).parent().parent().children('td:eq(0)').text());
    $("#titulo_eliminar").html($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

$('#clickEliminarRegistro').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/eliminar/',
              type: 'POST',
              data: $('#eliminar_nota_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#eliminar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  var contador = $('#contador').text();
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     html +='<tr><td id="idregistro">'+
                                        datos[i].pk+'</td><td>'+
                                        datos[i].fields.fecha+'</td><td>'+
                                        datos[i].fields.ganancia+'</td><td>'+
                                        datos[i].fields.gasto+'</td><td>'+
                                        datos[i].fields.nota+'</td>'+
                        '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarRegistro"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                        '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarRegistro"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                     '</tr>'
                  };                  
                  $('#FechaGananciasGastos').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Eliminado'+'</strong>'+' El registro se elimino correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                   contador--;
                   /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                 console.log(contador);
                 if(contador>10){
                     // console.log('poraca paso');
                      var paginacion = '<nav class="pagination" style="display: none;">'+
                                          '<span class="step-links"> {{ datos.next_page_number }}'+
                                              '{% if datos.has_next %}'+
                                                  '<a id="siguiente" href="?page=0">next</a>'+
                                              '{% endif %}datos'+
                                          '</span>'+
                                      '</nav>';
                      $('#pag').html(paginacion);
                      $('#contador').text(contador);
                  }else{

                      $('#contador').text(contador);
                      $('.pagination').remove();
                  }
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/

/*----------------------------------------------------------------------------------------------------------*/

/*____________________________Modificar solo la ganancia _____________________________________*/
$('#FechaGanancia' ).on("click","#modificarGanancia",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');
      //alert($(this).attr('href'));
      //estraemos los campos.
      $('#id_registro').val($(this).parent().parent().children('td:eq(0)').text());
      $('#fechaModificar').val($(this).parent().parent().children('td:eq(1)').text());
      $('#gananciaMod').val($(this).parent().parent().children('td:eq(2)').text());
      $('#gastoMod').val($(this).parent().parent().children('td:eq(3)').text());
      $('#notaMod').val($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

$('#clickModificarGanancia').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/modificar/',
              type: 'POST',
              data: $('#modificar_registro_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#modificar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                  //console.log('ganancia modificada');
                  var contador=0;
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     if(datos[i].fields.ganancia > 0){
                       html +='<tr><td id="idregistro">'+
                                          datos[i].pk+'</td><td>'+
                                          datos[i].fields.fecha+'</td><td>'+
                                          datos[i].fields.ganancia+'</td><td id="idregistro">'+
                                          datos[i].fields.gasto+'</td><td>'+
                                          datos[i].fields.nota+'</td>'+
                          '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarGanancia"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                          '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarGanancia"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                       '</tr>';
                     };
                  };                 
                  $('#FechaGanancia').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Editado'+'</strong>'+' El registro se modifico correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                  /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                  var paginacion = '<nav class="pagination" style="display: none;">'+
                                      '<span class="step-links">'+
                                          '{% if datos.has_next %}'+
                                              '<a id="siguiente" href="?page=2">next</a>'+
                                          '{% endif %}datos'+
                                      '</span>'+
                                  '</nav>';
                  $('#pag').html(paginacion);
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/


/*___________________________Eliminar solo la ganancias_________________________*/
$('#FechaGanancia' ).on("click","#eliminarGanancia",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');
      //alert($(this).attr('href'));
      //estraemos los campos.
    $('#id_eliminar').val($(this).parent().parent().children('td:eq(0)').text());
    $("#titulo_eliminar").html($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

$('#clickEliminarGanancia').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/eliminar/',
              type: 'POST',
              data: $('#eliminar_nota_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#eliminar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     if (datos[i].fields.ganancia > 0 ){
                       html +='<tr><td id="idregistro">'+
                                          datos[i].pk+'</td><td>'+
                                          datos[i].fields.fecha+'</td><td>'+
                                          datos[i].fields.ganancia+'</td><td id="idregistro">'+
                                          datos[i].fields.gasto+'</td><td>'+
                                          datos[i].fields.nota+'</td>'+
                          '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarGanancia"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                          '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarGanancia"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                       '</tr>';
                      };
                  };                  
                  $('#FechaGanancia').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Eliminado'+'</strong>'+' El registro se elimino correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                  /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                  var paginacion = '<nav class="pagination" style="display: none;">'+
                                      '<span class="step-links">'+
                                          '{% if datos.has_previous %}'+
                                              '<a href="?page={{ datos.previous_page_number }}">previous</a>'+
                                          '{% endif %}'+
                                          '<span class="current">'+
                                              'Page {{ datos.number }} of {{ datos.paginator.num_pages }}.'+
                                          '</span>'+
                                          '{% if datos.has_next %}'+
                                              '<a id="siguiente" href="?page=2">next</a>'+
                                          '{% endif %}datos'+
                                      '</span>'+
                                  '</nav>';
                  $('#pag').html(paginacion);
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/

/*---------------------------------------------------------------------------------------------------------*/

/*___________________Modificar solo el gasto___________________________*/
$('#FechaGasto' ).on("click","#modificarGasto",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');
      //alert($(this).attr('href'));
      //estraemos los campos.
      $('#id_registro').val($(this).parent().parent().children('td:eq(0)').text());
      $('#fechaModificar').val($(this).parent().parent().children('td:eq(1)').text());
      $('#gastoMod').val($(this).parent().parent().children('td:eq(2)').text());
      $('#gananciaMod').val($(this).parent().parent().children('td:eq(3)').text());
      $('#notaMod').val($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

$('#clickModificarGasto').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/modificar/',
              type: 'POST',
              data: $('#modificar_registro_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#modificar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                    if (datos[i].fields.gasto > 0){
                       html +='<tr><td id="idregistro">'+
                                          datos[i].pk+'</td><td>'+
                                          datos[i].fields.fecha+'</td><td>'+
                                          datos[i].fields.gasto+'</td><td id="idregistro">'+
                                          datos[i].fields.ganancia+'</td><td>'+
                                          datos[i].fields.nota+'</td>'+
                          '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarGasto"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                          '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarGasto"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                       '</tr>';
                     };
                  };                  
                  $('#FechaGasto').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Editado'+'</strong>'+' El registro se modifico correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                  /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                  var paginacion = '<nav class="pagination" style="display: none;">'+
                                      '<span class="step-links">'+
                                          '{% if datos.has_previous %}'+
                                              '<a href="?page={{ datos.previous_page_number }}">previous</a>'+
                                          '{% endif %}'+
                                          '<span class="current">'+
                                              'Page {{ datos.number }} of {{ datos.paginator.num_pages }}.'+
                                          '</span>'+
                                          '{% if datos.has_next %}'+
                                              '<a id="siguiente" href="?page=2">next</a>'+
                                          '{% endif %}datos'+
                                      '</span>'+
                                  '</nav>';
                  $('#pag').html(paginacion);
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/


/*_____________________Eliminar solo gasto_______________________________*/
$('#FechaGasto' ).on("click","#eliminarGasto",function(){
      /*var variable = */
      console.log('poraca pasamos bien.');
      //alert($(this).attr('href'));
      //estraemos los campos.
    $('#id_eliminar').val($(this).parent().parent().children('td:eq(0)').text());
    $("#titulo_eliminar").html($(this).parent().parent().children('td:eq(4)').text());
      //var url= $(this).attr('href');
});

$('#clickEliminarGasto').click(function(e){
        e.preventDefault();
        console.log('ok ready;');
        $.ajax({
              beforeSend: function(){

              },
              url: '/eliminar/',
              type: 'POST',
              data: $('#eliminar_nota_form').serialize(),
              success: function(data){
                //console.log(data);
                if(data == "Error"){
                  console.log('Algo salio mal :(')
                }else{
                 //$('#modificar_nota_form')[0].reset();//borramos los datos del form 
                 $('#eliminar').modal('hide')//ocultamos el modal 
                /* $('#FechaTituloNota').empty();//limpiamos la tabla */
                  var html = "";
                  var datos = JSON.parse(data);
                    //console.log(datos);
                  for (var i = 0; i < datos.length; i++) {
                     /* console.log(datos[i].pk);*/
                     //console.log(datos[i].fields.fecha);
                     if (datos[i].fields.gasto > 0){
                       html +='<tr><td id="idregistro">'+
                                          datos[i].pk+'</td><td>'+
                                          datos[i].fields.fecha+'</td><td>'+
                                          datos[i].fields.gasto+'</td><td id="idregistro">'+
                                          datos[i].fields.ganancia+'</td><td>'+
                                          datos[i].fields.nota+'</td>'+
                          '<td><a href=""  class="btn btn-info btn-sm" data-toggle="modal" data-target="#modificar" id="modificarGasto"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span> Editar</a></td>'+
                          '<td><a href=""  class="btn btn-danger btn-sm" data-toggle="modal" data-target="#eliminar" id="eliminarGasto"><span class="glyphicon glyphicon-trash" aria-hidden="true"></span> Eliminar</a></td>'+
                       '</tr>';
                     };
                  };                  
                  $('#FechaGasto').html(html);//mandamos los nuevos datos a la tabla
                    setTimeout(function(){ $("#mensajeEditado .alert").fadeOut(6000).fadeIn(3000).fadeOut(900).fadeIn(800).fadeOut(600);}, 800); 
                   var exito = '<div class="alert alert-success">'+'<button type="button" class="close" data-dismiss="alert">'+
                   'X'+'</button>'+'<strong>'+'Eliminado'+'</strong>'+' El registro se elimino correctamente.'+'</div>';
                  $('#mensajeEditado').html(exito);//mensaje de exito
                  /*Volvemos a mandar el codigo de paginacion porque se desactiva cunado terminamos de hacerlo la primera vez*/
                  var paginacion = '<nav class="pagination" style="display: none;">'+
                                      '<span class="step-links">'+
                                          '{% if datos.has_previous %}'+
                                              '<a href="?page={{ datos.previous_page_number }}">previous</a>'+
                                          '{% endif %}'+
                                          '<span class="current">'+
                                              'Page {{ datos.number }} of {{ datos.paginator.num_pages }}.'+
                                          '</span>'+
                                          '{% if datos.has_next %}'+
                                              '<a id="siguiente" href="?page=2">next</a>'+
                                          '{% endif %}datos'+
                                      '</span>'+
                                  '</nav>';
                  $('#pag').html(paginacion);
                }
              },
              error: function(jqXHR,estado,error){
                  console.log(estado);
                  console.log(error);
              },
              complete: function(jqXHR,estado){
                  console.log(estado);
              },
              timeout: 10000//10 segundos.
        });/*Cierre del ajax*/
});/*Cierre de la funtion click*/

/*click para volver arriba*/
$('#arriba').click(function () {
        $('html, body').animate({
               scrollTop: '0px'
        },
        600);
        $('#buscar').focus();
});

/* hacemos que aparesca el boton para volver arriba*/
var boton = $('#cajaArriba');
var boton_offset = boton.offset();
    boton.css("display", "none");

$(window).on('scroll', function() {
    if($(window).scrollTop() > boton_offset.top) {
        boton.addClass('movimientoArriba');
        boton.css("display", "block");
    } else {
        boton.removeClass('movimientoArriba');
        boton.css("display", "none");
    }
});
/*---------------------------------------------------*/

/*paginacion con scroll infinito*/
$(window).scroll(function(){
    if($(window).scrollTop() >= $(document).height() - $(window).height()){
        if($('.pagination #siguiente').length){
            $('#cargando').show();
             /*_____________________________________*/
          $.ajax({
              type: 'GET',
              url: $('.pagination #siguiente').attr('href'),
              success: function(html){
                  //console.log(html);
                var nuevosRegistros = $(html).find('table tbody'),
                  nuevaPag     = $(html).find('.pagination'),
                  tabla        = $('table');
                  tabla.find('tbody').append(nuevosRegistros.html());//agregamos los nuevos datos 
                  tabla.after(nuevaPag.hide());
                $('#cargando').hide();//ocultamos la img cargando
                $('[data-toggle=popover]').popover({html:true});
              }
          });
            $('.pagination').remove();//evitams que se vea la paginacion y no solo eso si no que no se repitan los datos
        }
    }
});

/*---------------------------------------------------------------------------------------*/


});/*Cierre del document*/