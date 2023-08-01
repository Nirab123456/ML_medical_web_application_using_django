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
function handleSelectionChange() {
  var selectedStrength = encodeURIComponent(document.getElementById("strength").value);
  var selectedDosageForm = encodeURIComponent(document.getElementById("dosage_form").value);
  var drugName = encodeURIComponent(document.getElementById("name").value);
  var sortOption = document.getElementById("sortOption").value;

  // Make an AJAX call to fetch the medication details based on the selected strength, dosage form, and drug name
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/get_medication/?strength=' + selectedStrength + '&dosage_form=' + selectedDosageForm + '&name=' + drugName + '&sort=' + sortOption, true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      var medicationDetails = JSON.parse(xhr.responseText);
      if (Array.isArray(medicationDetails) && medicationDetails.length > 0) {
        // Sort the medication details based on the selected sort option
        if (sortOption === "priceAsc") {
          medicationDetails.sort(function(a, b) {
            return a.price_analysis - b.price_analysis;
          });
        } else if (sortOption === "priceDesc") {
          medicationDetails.sort(function(a, b) {
            return b.price_analysis - a.price_analysis;
          });
        }
        
        // Display details for each medication
        var detailsHtml = "";
        for (var i = 0; i < medicationDetails.length; i++) {
          var medication = medicationDetails[i];
          detailsHtml += '<div class="card card-margin">';
          detailsHtml += '  <div class="card-body">';
          detailsHtml += '    <div class="row search-body">';
          detailsHtml += '      <div class="col-lg-12">';
          detailsHtml += '        <div class="search-result">';
          detailsHtml += '          <div class="result-body">';
          detailsHtml += '            <div class="table-responsive">';
          detailsHtml += '              <table class="table  widget-26">';
          detailsHtml += '                <tbody>';
          detailsHtml += '                  <tr>';
          detailsHtml += '                    <td class="column-1">';
          detailsHtml += '                      <div class="widget-26-job-title">';
          detailsHtml += '                        <a href="#">' + medication.name.trim() + '</a>';
          detailsHtml += '                        <p class="m-0">';
          detailsHtml += '                          <a href="#" class="employer-name text-center Class">' + medication.dosage_form.trim() + '.</a>';
          detailsHtml += '                        </p>';
          detailsHtml += '                      </div>';
          detailsHtml += '                    </td>';
          detailsHtml += '                    <td class="column-2" >';
          detailsHtml += '                      <div class="widget-26-job-info">';
          detailsHtml += '                        <p class="type m-0">' + medication.manufacturer.trim() + '</p>';
          detailsHtml += '                        <a  class="type m-0 employer-name">' + medication.generic_name.trim() + '.</a>';
          detailsHtml += '                      </div>';
          detailsHtml += '                    </td>';

          if(medication.price != '0'){
            detailsHtml += '                    <td class="column-3" >';
            detailsHtml += '                      <div class="widget-26-job-category">';
            detailsHtml += '                        <p class="m-0 text-center Class">' + medication.price.trim() + '</p>';
            detailsHtml += '                      </div>';
            detailsHtml += '                    </td>';
          }
            else{
            detailsHtml += '                    <td class="column-3">';
            detailsHtml += '                      <div class="widget-26-job-category">';
            detailsHtml += '                        <p class="m-0 text-center Class">PRICE DATA IS UNAVAILABLE</p>';
            detailsHtml += '                      </div>';
            detailsHtml += '                    </td>';
            }

          detailsHtml += '                  </tr>';
          detailsHtml += '                </tbody>';
          detailsHtml += '              </table>';
          detailsHtml += '            </div>';
          detailsHtml += '          </div>';
          detailsHtml += '        </div>';
          detailsHtml += '      </div>';
          detailsHtml += '    </div>';
          detailsHtml += '  </div>';
          detailsHtml += '</div>';
        }
        document.getElementById("medicationDetails").innerHTML = detailsHtml;
      } else {
        // Display "No data found" message
        document.getElementById("medicationDetails").innerHTML = "<p>No data found</p>";
      }
    } else {
      console.error('Request failed. Status:', xhr.status);
      // Display "No data found" message for error cases
      document.getElementById("medicationDetails").innerHTML = "<p>No data found</p>";
    }
  };
  xhr.onerror = function() {
    console.error('Request failed. Network error');
    // Display "No data found" message for network errors
    document.getElementById("medicationDetails").innerHTML = "<p>No data found</p>";
  };
  xhr.send();
}
