<form action="/submit-form" method="post" onsubmit="setToken()">
  <!-- Other form elements here -->
  <input type="text" id="tokenInput" readonly>
  <input type="submit" value="Submit Form">
  <script>
    function setToken() {
      // Set the token value to a random number
      const token = Math.floor(Math.random() * 100000);
      // Set the value of the input field
      document.getElementById("tokenInput").value = token;
      // Set the hidden input field's value for server-side processing
      document.querySelector('[name="token"]').value = token;
    }
  </script>
</form>
