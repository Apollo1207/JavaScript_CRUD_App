var x = document.getElementById("first_card_seats").innerHTML;
var y = document.getElementById("second_card_seats").innerHTML;
var z = document.getElementById("third_card_seats").innerHTML;
var k = document.getElementById("second_card_seats").innerHTML;
var arraySeats = [x,y,z,k];

function seatsCounter(arr){
var sum = 0;
for(var i = 0; i < arraySeats.length; i++){
    sum += parseInt(arraySeats[i]);
    }
document.getElementById("demo").innerHTML = sum;
}

function searchFunction() {
    let input, filter, myCards, card, location, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    myCards = document.getElementById("myCards");
    card = myCards.getElementsByClassName("card");
    for (i = 0; i < card.length; i++) {
        location = card[i].getElementsByClassName("location")[0];
        txtValue = location.textContent || location.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            card[i].style.display = "";
        } else {
            card[i].style.display = "none";
        }
    }
}

function sortFunction(parent, childSelector, keySelector) {
    var items = parent.children(childSelector).sort(function(a, b) {
        var vA = $(keySelector, a).text();
        var vB = $(keySelector, b).text();
        vA = parseFloat(vA)
        vB = parseFloat(vB)
        return (vA > vB) ? -1 : (vA < vB) ? 1 : 0;
    }); 
    parent.append(items);
}

$('#sScale').data("sortKey", "span.scale");

$(document).ready(function() {
    $('input[type="checkbox"]').click(function() {
        if ($(this).prop("checked") === true) {
            sortFunction($('.row'), "div", $(this).data("sortKey"));

        }
    });
});