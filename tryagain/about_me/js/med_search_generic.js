document.addEventListener("DOMContentLoaded", function() {

var timeout; // Global variable to store timeout reference
  
  function genericrecomendation() {
    clearTimeout(timeout); // Clear previous timeout, if any
  
    // Set a new timeout to fetch word recommendations after a brief delay (e.g., 300ms)
    timeout = setTimeout(function() {
      var input = document.getElementById("generic_name").value.trim();
      console.log(input);
  
      // Check if there is any input
      if (input.length === 0) {
        var recommendationsHtml = `
        <select class=' my-custom-input-group form-select' aria-label='Default select example'  onchange='selectgenericrecomendtions()'>
        <option value="">USE A PROPER GENERIC NAME</option>
        </select>
        `
        document.getElementById("genericrecomendation").innerHTML = recommendationsHtml;
        return;
      }
  
      // Make an AJAX call to fetch word recommendations based on the input
      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/get_generic_name_recommendations/?input=' + encodeURIComponent(input), true);
      xhr.onload = function() {




        if (xhr.status === 200) {
          var wordRecommendations = JSON.parse(xhr.responseText);
  
          // Display word recommendations in a list
          var recommendationsHtml = "<select id='generic_select' class=' my-custom-input-group form-select' aria-label='Default select example'  onchange='selectgenericrecomendtions()'>";

          
            if (wordRecommendations.length !== 0) {
              for (var i = 0; i < wordRecommendations.length; i++) {
                var word = wordRecommendations[i];
                recommendationsHtml += '<option value="' + word + '">' + word + '</option>';
              }
            } else {
              recommendationsHtml += '<option value="">USE A PROPER GENERIC NAME</option>';
            }




            recommendationsHtml += "</select>";
          document.getElementById("genericrecomendation").innerHTML = recommendationsHtml;
        } 
        
        
        
        else {
          console.error('Request failed. Status:', xhr.status);
          // Display no recommendations for error cases
          document.getElementById("genericrecomendation").innerHTML = "";
        }
      };
      xhr.onerror = function() {
        console.error('Request failed. Network error');
        // Display no recommendations for network errors
        document.getElementById("genericrecomendation").innerHTML = "";
      };
      xhr.send();
    }, 300); // Adjust the delay as needed (in milliseconds)


  }
  
  // Function to select a word recommendation and populate the input field with it
  function selectgenericrecomendtions() {
    var selectElement = document.getElementById("generic_select");
    var selectedOption = selectElement.options[selectElement.selectedIndex].value;
    document.getElementById("generic_name").value = selectedOption;
  }

  // Function to select a word recommendation and populate the input field with it
  function selectRecommendation() {
    var selectElement = document.querySelector("select");
    var selectedOption = selectElement.options[selectElement.selectedIndex].value;
    document.getElementById("generic_name").value = selectedOption;
  }
  

  function handleFormSubmission(event) {
    var selectedStrength = encodeURIComponent(document.getElementById("strength").value);
    var selectedDosageForm = encodeURIComponent(document.getElementById("dosage_form").value);
    var drugName = encodeURIComponent(document.getElementById("generic_name").value);
    // var sortOption = document.getElementById("sortOption").value;
    console.log(selectedStrength);
    console.log(selectedDosageForm);
    console.log(drugName);

    if (selectedStrength && selectedDosageForm && drugName) {
      event.preventDefault(); // Prevent default form submission behavior

      // Construct the URL with query parameters
      var queryParams = '?strength=' + selectedStrength + '&dosage_form=' + selectedDosageForm + '&generic_name=' + drugName;
      // You can add more parameters if needed like this: '&param1=value1&param2=value2'

      // Redirect to the target HTML page with the query parameters
      window.location.href = '/med_search_results/' + queryParams;
    }
  }

  // Attach the handleFormSubmission function to the form's submit event
  document.getElementById("med_search_form").addEventListener("submit", handleFormSubmission);



  genericrecomendation();
});


