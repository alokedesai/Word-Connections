function testing_ajax(echo) {
    $.ajax("/echo?echo="+echo, {"dataType": "json", "type": "GET", "success": function (data) {
        console.log(data["echoed"]);
    }});
}


