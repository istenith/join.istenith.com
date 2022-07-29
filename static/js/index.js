var $input;

// function validate_email() {
//   var userEmail = document.getElementById("id_email").value;
//   var emailStart = userEmail.substring(0, 2);
//   var regx = /21/;
//   if (regx.test(emailStart)) {
//   } else {
//   }

function onInputFocus(event) {
  var $target = $(event.target);
  var $parent = $target.parent();
  $parent.addClass("input--filled");
}

function onInputBlur(event) {
  var $target = $(event.target);
  var $parent = $target.parent();

  if (event.target.value.trim() === "") {
    $parent.removeClass("input--filled");
  }
}

$(document).ready(function () {
  $input = $(".input__field");

  // in case there is any value already
  $input.each(function () {
    if ($input.val().trim() !== "") {
      var $parent = $input.parent();
      $parent.addClass("input--filled");
    }
  });

  $input.on("focus", onInputFocus);
  $input.on("blur", onInputBlur);
});

// Declared the regx variable
//  declared a variable in js having the starting 2 characters of the email via getelement method
//  now if statment used and if(regX== true), then run the success page ki submit hogya successfully.
//  if the statemnet is false then throw the same type error that we get in the Django emailValidator
//  return the same home page to refill the form easy af
// aidjafha
// disojfioa
