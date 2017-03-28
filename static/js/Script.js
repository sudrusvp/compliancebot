/*eslint-env jquery, browser*/
$(function(){

	var sentHead = "<div class='row' style='margin: 5px 0px;'> <div class='col-sm-offset-4 col-sm-8 text-right' '> <div class='sent text-left' >";
	var receivedHead = "<div class='row' style='margin: 5px 0px;'> <div class='col-sm-8 text-left' '> <div class='received text-left' >";
	var tail = "</div> </div> </div>";
		
	function send() {
		//console.log("inside send1")
		var data = {
			"message" : $("#message").val(),
			
		};
		//console.log("inside send2")
		$(sentHead+data.message+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);
		//console.log("inside send3")
		$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
		//console.log("inside send4")
		$("#message").val("");
		//console.log("inside send5")
		//console.log("calling..")
		
		/*
		$.ajax({url: "/", type:'POST',
		success:function(res){
			//console.log("inside post1")
			//console.log(res)
			$(receivedHead+res+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);
			//console.log("inside post2")
			$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
			//console.log("inside post3")
			},
			
		error: function(err){
            $(receivedHead+'Can you say that again'+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);
			//console.log("inside post2")
			$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
        }});*/
        
        
		$.post("/",data,function(res,err){
			
			if (err !== 'success'){
				console.log('error occured'+err);
				$(receivedHead+'Can you please say that again'+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);
				//console.log("inside post2")
				$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
			}
			//console.log("inside post1")
			//console.log(res)


			$(receivedHead+res+tail).hide().appendTo('.chatdiv').show("puff", {times : 3}, 200);
			//console.log("inside post2")
			$(".chatdiv").animate({ scrollTop: $('.chatdiv').prop("scrollHeight")}, 1000);
			//console.log("inside post3")
			});

	};


	$("#message").keypress(function(event) {
		if (event.which === 13) {
			event.preventDefault();

			if( $("#message").val() !== "")
				send();
		}
	});

	$("#send").click(function(event){
		//console.log("send")
		if( $("#message").val() !== "")
			send()
	})

	function setInput(text) {
		$("#message").val(text);
		//send()
	}
});



