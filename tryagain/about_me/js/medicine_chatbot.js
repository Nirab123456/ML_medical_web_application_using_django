var timeout; // Global variable to store timeout reference
        
function showWordRecommendations() {
  clearTimeout(timeout); // Clear previous timeout, if any

  // Set a new timeout to fetch word recommendations after a brief delay (e.g., 300ms)
  timeout = setTimeout(function() {
    var input = document.getElementById("name").value.trim();

    // Check if there is any input
    if (input.length === 0) {
      document.getElementById("wordRecommendations").innerHTML = "";
      return;
    }

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
  document.getElementById("name").value = selectedOption;
  document.getElementById("wordRecommendations").innerHTML = "";
}

      function handleFormSubmit(event) {
        event.preventDefault(); // Prevent the form from being submitted traditionally
        handleSelectionChange();
      }
      function handleSelectionChange() {
        var drugName = encodeURIComponent(document.getElementById("name").value);

        // Make an AJAX call to fetch the medication details based on the selected strength, dosage form, and drug name
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_medicine_details/?name=' + drugName , true);
        xhr.onload = function() {
          if (xhr.status === 200) {
            var get_medicine_details = JSON.parse(xhr.responseText);
            if (Array.isArray(get_medicine_details) && get_medicine_details.length > 0) {

              // Display details for each medication
              var detailsHtml = "";
              for (var i = 0; i < get_medicine_details.length; i++) {
                var medication = get_medicine_details[i];
                detailsHtml += "<div class='medication-details'>";
                detailsHtml += "<p><strong>Generic Name:</strong> " + medication.generic_name + "</p>";
                detailsHtml += "<p><strong>DRUG CLASS:</strong> " + medication.drug_class + "</p>";
                detailsHtml += "<p><strong>Indication:</strong> " + medication.indication + "</p>";
                detailsHtml += "<p><strong>INDICATION DESCRIPTION:</strong> " + medication.indication_description + "</p>";
                detailsHtml += "<p><strong>THERAPEUTIC CLASS:</strong> " + medication.therapeutic_class_description + "</p>";
                detailsHtml += "<p><strong>PHARMACOLOGY DESCRIPTION:</strong> " + medication.pharmacology_description + "</p>";
                detailsHtml += "<p><strong>DOSAGE DESCRIPTION:</strong> " + medication.dosage_description + "</p>";
                detailsHtml += "<p><strong> INTERACTIONS DESCRIPTION:</strong> " + medication.interaction_description + "</p>";
                detailsHtml += "<p><strong>CONTRAINDICATIONS DESCRIPTION:</strong> " + medication.contraindications_description + "</p>";
                detailsHtml += "<p><strong> SIDE EFFECTS DESCRIPTION:</strong> " + medication.side_effects_description + "</p>";
                // Add more fields here
                detailsHtml += "</div>";
                detailsHtml += "<hr>";
              }
              document.getElementById("get_medicine_details").innerHTML = detailsHtml;
            } else {
              // Display "No data found" message
              document.getElementById("get_medicine_details").innerHTML = "<p>No data found</p>";
            }
          } else {
            console.error('Request failed. Status:', xhr.status);
            // Display "No data found" message for error cases
            document.getElementById("get_medicine_details").innerHTML = "<p>No data found</p>";
          }
        };
        xhr.onerror = function() {
          console.error('Request failed. Network error');
          // Display "No data found" message for network errors
          document.getElementById("get_medicine_details").innerHTML = "<p>No data found</p>";
        };
        xhr.send();
      }