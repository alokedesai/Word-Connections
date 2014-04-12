function addWord(echo) {
    $.ajax("/addWord?word="+echo, {"dataType": "json", "type": "GET", "success": function (data) {
	
        console.log(data);
    }});
}


