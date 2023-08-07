var numNameFields = 1;

function addNameField() {
    var nameContainer = document.getElementById("name-container");
    var nameFieldContainer = document.createElement("div");
    nameFieldContainer.className = "presciption_classification"; // Added 'input-group' class to ensure proper alignment

    var newInput = document.createElement("input");
    newInput.className = "input--style-1";
    newInput.type = "text";
    newInput.name = "name";
    newInput.id = "name-" + numNameFields;
    newInput.value = "";
    newInput.placeholder = "NAME OF THE DRUG e.g:NAPA";
    newInput.required = true;
    newInput.oninput = function(event) {
        showWordRecommendations(event, numNameFields);
    };

    var deleteButton = document.createElement("button");
    deleteButton.type = "button";
    deleteButton.className = "btn btn-danger";
    deleteButton.textContent = "Remove";
    deleteButton.onclick = function() {
        removeNameField(newInput.id);
    };

    nameFieldContainer.appendChild(newInput);
    nameFieldContainer.appendChild(deleteButton);
    nameContainer.appendChild(nameFieldContainer);
    numNameFields++;
}

// Function to remove the clicked name field
function removeNameField(inputId) {
    var nameContainer = document.getElementById("name-container");
    var inputToRemove = document.getElementById(inputId);
    nameContainer.removeChild(inputToRemove.parentElement); // Remove the parent div containing the input and delete button
}
 


// Global variable to store timeout references for each name field
var timeouts = {};

var recommendationsHtml = "<select class=' my-custom-input-group form-select' aria-label='Default select example'  onchange='selectRecommendation()'>";
recommendationsHtml += '<option value="">USE A PROPER BRAND NAME</option>';
document.getElementById("wordRecommendations").innerHTML = recommendationsHtml;


  function showWordRecommendations(event, fieldNum) {
    var input = event.target.value.trim();


      // Clear previous timeout, if any
      clearTimeout(timeouts[fieldNum]);
      timeouts[fieldNum] = setTimeout(function() {
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
    document.getElementById("name-" + (numNameFields - 1)).value = selectedOption;
}



function handleFormSubmit(event) {
event.preventDefault(); // Prevent the form from being submitted traditionally
handleSelectionChange();
}



function handleSelectionChange() {
  var nameInputs = document.querySelectorAll("#name-container input");
    var drugNames = [];
    for (var i = 0; i < nameInputs.length; i++) {
      drugNames.push(encodeURIComponent(nameInputs[i].value));
    }

      // Construct the URL with query parameters
      var queryParams = '?name=' + drugNames;
      // You can add more parameters if needed like this: '&param1=value1&param2=value2'

      // Redirect to the target HTML page with the query parameters
      window.location.href = '/presciption_classification_beta_results/' + queryParams;
    }

  // Attach the handleFormSubmission function to the form's submit event
  document.getElementById("med_search_form").addEventListener("submit", handleFormSubmit);

