
function addWord(word) {
    var url = "/addWord?word="+word+"&categories="+encodeURIComponent(JSON.stringify(categories));
    $.ajax(url, {"dataType": "json", "type": "GET", "success": function (data) {
        categories=data;	
	update();
        console.log(data);
    }});
}


