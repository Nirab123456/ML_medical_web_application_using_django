
var numNameFields = 1;

function addNameField() {
    var nameContainer = document.getElementById("name-container");
    var nameFieldContainer = document.createElement("div");
    nameFieldContainer.className = "mb-3 input-group"; // Added 'input-group' class to ensure proper alignment

    var newInput = document.createElement("input");
    newInput.className = "form-control";
    newInput.type = "text";
    newInput.name = "name";
    newInput.id = "name-" + numNameFields;
    newInput.value = "";
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

function showWordRecommendations(event, fieldNum) {
    var input = event.target.value.trim();

    // Check if there is any input
    if (input.length === 0) {
        document.getElementById("wordRecommendations").innerHTML = "";
        return;
    }

    // Clear previous timeout, if any
    clearTimeout(timeouts[fieldNum]);

    // Set a new timeout to fetch word recommendations after a brief delay (e.g., 300ms)
    timeouts[fieldNum] = setTimeout(function() {
        // Make an AJAX call to fetch word recommendations based on the input
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_word_recommendations/?input=' + encodeURIComponent(input), true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                var wordRecommendations = JSON.parse(xhr.responseText);

                // Display word recommendations in a list
                var recommendationsHtml = " <select onchange='selectRecommendation()'>";
                recommendationsHtml += '<option>CAN SELECT MATCHING DRUG NAME</option>';
                for (var i = 0; i < wordRecommendations.length; i++) {
                    var word = wordRecommendations[i];
                    recommendationsHtml += '<option value="' + word + '">' + word + '</option>';
                }
                recommendationsHtml += "</select>";

                document.getElementById("wordRecommendations").innerHTML = recommendationsHtml;
            } else {
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
    document.getElementById("wordRecommendations").innerHTML = "";
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
      var question = encodeURIComponent(document.getElementById("question").value);
      var topic = encodeURIComponent(document.getElementById("topic").value);
    
      var xhr = new XMLHttpRequest();
      xhr.open('GET', '/get_medicine_chat/?name=' + drugNames + '&topic=' + topic + '&question=' + question, true);






      xhr.onload = function() {


        if (xhr.status === 200) {
          var get_medicine_chat = JSON.parse(xhr.responseText);
          if (Array.isArray(get_medicine_chat) && get_medicine_chat.length > 0) {

            var detailsHtml = "<div>";
            for (var i = 0; i < get_medicine_chat.length; i++) {
              detailsHtml += "<p><strong>" + get_medicine_chat[i]['name'] + " : </strong> " + get_medicine_chat[i]['answer']+ "</p>";
              // Add more fields here
              detailsHtml += "<hr>";
            }
            detailsHtml += "</div>";
            document.getElementById("get_medicine_chat").innerHTML = detailsHtml;

          } else {
            document.getElementById("get_medicine_chat").innerHTML = "<p>No data found </p>";
          }



        } else {
          console.error('Request failed. Status:', xhr.status);
          document.getElementById("get_medicine_chat").innerHTML = "<p>No data found </p>";
        }




      };





      xhr.onerror = function() {
        console.error('Request failed. Network error');
        document.getElementById("get_medicine_chat").innerHTML = "<p>No data found </p>";
      };
      xhr.send();
    }
    
