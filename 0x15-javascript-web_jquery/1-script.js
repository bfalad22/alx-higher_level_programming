<!DOCTYPE html>
<html>
<head>
  <title>Update Header Text Color</title>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
  <header>
    <h1>Hello, this is a header!</h1>
  </header>

  <script>
    // Wrap the script in a jQuery ready function to ensure the DOM is ready
    $(document).ready(function() {
      // Use the jQuery API to select the <header> element
      $('header').css('color', '#FF0000');
    });
  </script>
</body>
</html>

