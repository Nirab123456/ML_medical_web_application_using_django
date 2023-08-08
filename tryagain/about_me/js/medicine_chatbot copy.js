            
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
    
    
    
    
    
    
    
    
        const showHideButton = document.getElementById('showHideButton');
        const sectionToHide = document.getElementById('sectionToHide');
        const select_question = document.getElementById('select_question');
        const question = document.getElementById('question');
        const topic = document.getElementById('topic');
    
        function toggleSectionVisibility() {
            if (select_question.value === '' || !select_question.value) {
                sectionToHide.style.display = 'block';
            } else {
                sectionToHide.style.display = 'none';
            }
    
            if (question.value) {
                select_question.style.display = 'none';
            } else {
                select_question.style.display = 'block';
            }
            if (select_question.value !== '' ){
                topic.style.display = 'none';
            }
            else{
                topic.style.display = 'block';
            }
        }
    



        // Add event listener for the button click
        showHideButton.addEventListener('click', () => {
            if (sectionToHide.style.display === 'none') {
                sectionToHide.style.display = 'block';
            } else {
                sectionToHide.style.display = 'none';
            }
    
            // Call toggleSectionVisibility to handle the visibility change
            toggleSectionVisibility();
        });
    
        // Add event listener for the select box change
        select_question.addEventListener('change', toggleSectionVisibility);
    
        // Call the function initially to set the initial visibility based on the select box value and question value
        toggleSectionVisibility();
    
    
    
    
    
        function handleSelectionChange() {
          var nameInputs = document.querySelectorAll("#name-container input");
          var drugNames = [];
          for (var i = 0; i < nameInputs.length; i++) {
              drugNames.push(encodeURIComponent(nameInputs[i].value));
          }
          console.log(drugNames);

    
          var selected_question = encodeURIComponent(document.getElementById("select_question").value);
          console.log(selected_question);
          var question = encodeURIComponent(document.getElementById("question").value);
          console.log(question);
    
          var topic = encodeURIComponent(document.getElementById("topic").value);
          console.log(topic);
          if (topic === "" || topic === "none") {
              topic = null;
          }
    
          // If selected_question is "none" or not a valid value, use the custom question
          if (selected_question === "" || selected_question === "none") {
              selected_question = null;
          } else {
              // If a valid value is selected, clear the custom question input
              document.getElementById("question").value = "";
              question = null;
          }

          
    
          var xhr = new XMLHttpRequest();
          xhr.open('GET', '/get_medicine_chat/?name=' + drugNames + '&topic=' + topic + '&question=' + question + '&selected_question=' + selected_question, true);
    
    

    
          xhr.onload = function() {
    
    
            if (xhr.status === 200) {
              var get_medicine_chat = JSON.parse(xhr.responseText);
              console.log(get_medicine_chat);
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
