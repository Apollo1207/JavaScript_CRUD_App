function checkTypeInputValue() {
    var name = document.forms["myForm"]["name"].value;
    var seats = document.forms["myForm"]["seats"].value;
    var year = document.forms["myForm"]["year"].value;
    var location = document.forms["myForm"]["location"].value;
    var scale = document.forms["myForm"]["scale"].value;

    var regex_str = /^[a-zA-Z]+$/;
    var regex_num = /^[0-9]+$/;
    if (!name.match(regex_str) || !seats.match(regex_num) || !year.match(regex_num) || !location.match(regex_str) ||
        !scale.match(regex_num)
        ) {
        alert("Data entered incorrectly");
    } 

}