var $input;

function validate_email() {
  var userEmail = document.getElementById("id_email").value;
  var emailStart = userEmail.substring(0, 2);
  var regx = /21/;
  if (regx.test(emailStart)) {
    alert("wohoo chl pada!");
  } else {
    alert("email dekh ke daal bhay");
  }
}

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
