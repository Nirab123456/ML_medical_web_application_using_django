
$(document).ready(function () {
    showWordRecommendations();
    $(".tab-list__link").on("click", function (e) {
        e.preventDefault();
        var targetTab = $(this).attr("href");
        $(".tab-pane").removeClass("active");
        $(targetTab).addClass("active");
    });
  });
  
  var timeout; // Global variable to store timeout reference
    
    function showWordRecommendations() {
      clearTimeout(timeout); // Clear previous timeout, if any
    
      // Set a new timeout to fetch word recommendations after a brief delay (e.g., 300ms)
      timeout = setTimeout(function() {
        var input = document.getElementById("name").value.trim();
        console.log(input);
    
        // Check if there is any input
        if (input.length === 0) {
          var recommendationsHtml = "<select class=' my-custom-input-group form-select' aria-label='Default select example'  onchange='selectRecommendation()'>";
          recommendationsHtml += '<option value="">USE A PROPER BRAND NAME</option>';
          document.getElementById("wordRecommendations").innerHTML = recommendationsHtml;
          return;
        }
    
        // Make an AJAX call to fetch word recommendations based on the input
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_word_recommendations/?input=' + encodeURIComponent(input), true);
        xhr.onload = function() {
  
  
  
  
          if (xhr.status === 200) {
            var wordRecommendations = JSON.parse(xhr.responseText);
    
            // Display word recommendations in a list
            var recommendationsHtml = "<select class=' my-custom-input-group form-select' aria-label='Default select example'  onchange='selectRecommendation()'>";
  
            
              if (wordRecommendations.length !== 0) {
                for (var i = 0; i < wordRecommendations.length; i++) {
                  var word = wordRecommendations[i];
                  recommendationsHtml += '<option value="' + word + '">' + word + '</option>';
                }
              } else {
                recommendationsHtml += '<option value="">USE A PROPER BRAND NAME</option>';
              }
  
  
  
  
              recommendationsHtml += "</select>";
            document.getElementById("wordRecommendations").innerHTML = recommendationsHtml;
          } 
          
          
          
          else {
            console.error('Request failed. Status:', xhr.status);
            // Display no recommendations for error cases
            document.getElementById("wordRecommendations").innerHTML = "";
          }
        };
        xhr.onerror = function() {
          console.error('Request failed. Network error');
          // Display no recommendations for network errors
          document.getElementById("wordRecommendations").innerHTML = "";
        };
        xhr.send();
      }, 300); // Adjust the delay as needed (in milliseconds)
  
  
    }
    
    // Function to select a word recommendation and populate the input field with it
    function selectRecommendation() {
      var selectElement = document.querySelector("select");
      var selectedOption = selectElement.options[selectElement.selectedIndex].value;
      document.getElementById("name").value = selectedOption;
    }
    
  
    function handleFormSubmission(event) {
      var drugName = encodeURIComponent(document.getElementById("name").value);
      // var sortOption = document.getElementById("sortOption").value;
      console.log(drugName);
  
      if (drugName) {
        event.preventDefault(); // Prevent default form submission behavior
  
        // Construct the URL with query parameters
        var queryParams = '?name=' + drugName;
        // You can add more parameters if needed like this: '&param1=value1&param2=value2'
  
        // Redirect to the target HTML page with the query parameters
        window.location.href = '/med_details_search_results/' + queryParams;
      }
    }
  
    // Attach the handleFormSubmission function to the form's submit event
    document.getElementById("med_search_form").addEventListener("submit", handleFormSubmission);
  
  