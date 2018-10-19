function comprar(){}
$desc_pro=$(this).closest('.producto').children().children('div').children().first().children().children().html();
        console.log($desc_pro);
         $.notify({
        icon: 'glyphicon glyphicon-shopping-cart',
        title:"<strong>Has añadido: </strong>",    
	   
	   message: $desc_pro + "<strong> a tu carrito</strong>",
   
         },{
	 
             type: 'success',
            offset: {y:50, x:0},
                               	animate: {
		enter: 'animated fadeInRight',
		exit: 'animated fadeOutRight'
	},
         });
        var lista_productos=[];
      
        
        var productos_carrito=sessionStorage.getItem("carrito-productos");
        if(productos_carrito!=null){
            lista_productos.push(productos_carrito);
            

           }
        else {
            var lista_productos3=[];
           
           sessionStorage.setItem("carrito-productos", lista_productos3);
        }
        
     lista_productos.push($(this).val());
        sessionStorage.setItem("carrito-productos",lista_productos);
      
      
        $.ajax({
            url: '{% url "index:obtener_total_carrito" %}',
            
            data:{ lista_productos_carrito:JSON.stringify(sessionStorage.getItem("carrito-productos")),
                
                  
                
            },
            dataType:'json',
            success: function(data){
               
              console.log(data.total);
                console.log(data.cantidad)
                $('#total-carrito').text(" $"+data.total+" ");;
                $('#cantidad-carrito').text(" "+data.cantidad+" "+"item(s)");
               
                
                
            }
            
        });
        
    });
    $('.favorito').click(function(){
       

       
        $desc_pro=$(this).closest('.producto').children().children('div').children().first().children().children().html();
        console.log($desc_pro);
         $.notify({
        icon: 'glyphicon glyphicon-heart',
        title:"<strong>Has añadido: </strong>",    
	   
	   message: $desc_pro + "<strong> a tus favoritos</strong>",
   
         },{
	 
             type: 'danger',
            offset: {y:50, x:0},
                               	animate: {
		enter: 'animated fadeInRight',
		exit: 'animated fadeOutRight'
	},
         });
        var lista_favoritos=[];
      
        
        var productos_favorito=sessionStorage.getItem("productos-favoritos");
        if(productos_favorito!=null){
            lista_favoritos.push(productos_favorito);
            

           }
        else {
            var lista_productos3=[];
           
           sessionStorage.setItem("productos-favoritos", lista_productos3);
        }
        
     lista_favoritos.push($(this).val());
        sessionStorage.setItem("productos-favoritos",lista_favoritos);
      console.log("favoritos");
        console.log(sessionStorage.getItem("productos-favoritos"));