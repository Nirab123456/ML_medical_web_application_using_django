

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
        var question = encodeURIComponent(document.getElementById("question").value);
        var topic = encodeURIComponent(document.getElementById("topic").value);
      
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/get_medicine_chat/?name=' + drugName + '&topic=' + topic + '&question=' + question, true);
        xhr.onload = function() {
          if (xhr.status === 200) {
            var get_medicine_chat = JSON.parse(xhr.responseText);
            console.log(get_medicine_chat); // Add this line for debugging
            if (get_medicine_chat) {
              var detailsHtml = "<div>";
              detailsHtml += "<p><strong>Generic Name:</strong> " + get_medicine_chat['answer']+ "</p>";
              // Add more fields here
              detailsHtml += "</div>";
              detailsHtml += "<hr>";
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
      