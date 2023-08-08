
function toggleMatchingGroups(target) {
    var allGroups = document.querySelectorAll(".coll-2");
    for (var i = 0; i < allGroups.length; i++) {
        if (allGroups[i].classList.contains(target)) {
            allGroups[i].classList.remove("hidden");
            allGroups[i].querySelector("input").required = true;
        } else {
            allGroups[i].classList.add("hidden");
            allGroups[i].querySelector("input").required = false;
        }
    }

    // Show the genericrecomendation div and hide the wordRecommendations div when searching by generic_name
    var wordRecommendationsDiv = document.getElementById("wordRecommendations");
    var genericRecomendationDiv = document.getElementById("genericrecomendation");
    if (target === "generic_name") {
        wordRecommendationsDiv.style.display = "none";
        genericRecomendationDiv.style.display = "block";
    } else {
        wordRecommendationsDiv.style.display = "block";
        genericRecomendationDiv.style.display = "none";
    }
}

// Attach the toggle function to the buttons' click events
var toggleButtons = document.querySelectorAll(".toggle-button");
toggleButtons.forEach(function(button) {
    button.addEventListener("click", function() {
        var target = button.getAttribute("data-target");
        toggleMatchingGroups(target);
    });
});

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
