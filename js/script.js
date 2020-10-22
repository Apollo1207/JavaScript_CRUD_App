// var x = document.getElementById("a").innerHTML;
// console.log(x);

// var y = document.getElementById("b").innerHTML;
// console.log(y);

// var arr = [x,y];

// function arraySum(arr){
// var sum = 0;
// for(var i = 0; i < arr.length; i++){
//     sum += parseInt(arr[i]);
//     }
// document.getElementById("demo").innerHTML = sum;
// }

// var numArray = [140000, 104, 99];
// numArray.sort(function(a, b) {
//   return a - b;
// });

// console.log(numArray);







// var values = document.querySelector("span");
// console.log(values.value)







function myFunction() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    ul = document.getElementById("myUL");
    li = ul.getElementsByClassName("card");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByClassName("location")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}




function sortUsingNestedText(parent, childSelector, keySelector) {
    var items = parent.children(childSelector).sort(function(a, b) {
        var vA = $(keySelector, a).text();
        var vB = $(keySelector, b).text();
        vA = parseFloat(vA)
        vB = parseFloat(vB)
        return (vA > vB) ? -1 : (vA > vB) ? 1 : 0;
    });
    parent.append(items);
}


$('#sPrice').data("sortKey", "span.scale");



 $(document).ready(function(){
        $('input[type="checkbox"]').click(function(){
            if($(this).prop("checked") == true){
    sortUsingNestedText($('.row'), "div", $(this).data("sortKey"));
               
            }
            else if($(this).prop("checked") == false){
               sortUsingNestedText($('.row'), "div", $(this).data("sortKey"));
               
              
            }
        });
    });

