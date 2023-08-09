  // Retrieve the query parameters from the URL
  const urlParams = new URLSearchParams(window.location.search);
  const strength = urlParams.get('strength');
  const dosageForm = urlParams.get('dosage_form');
  const drugName = urlParams.get('name');
  const generic_name = urlParams.get('generic_name');
  
  // Now you have the values of the query parameters in the variables (strength, dosageForm, drugName).
  // You can use these values as needed in the JavaScript code of this HTML page.
  // console.log('Strength:', strength);
  // console.log('Dosage Form:', dosageForm);
  // console.log('Drug Name:', drugName);





var currentPage = 1; // The current page number
var medicationDetails = []; 
document.getElementById("sortOption").addEventListener("change", handleSortOptionChange());

function fetchMedicationDetails(sortOption, currentPage) {
  var xhr = new XMLHttpRequest();

  if(!generic_name){
  xhr.open('GET', '/get_medication_details/?strength=' + strength + '&dosage_form=' + dosageForm + '&name=' + drugName, true);
  }else{
    xhr.open('GET', '/get_generic_medication_details/?strength=' + strength + '&dosage_form=' + dosageForm + '&generic_name=' + generic_name, true);
  }
  xhr.onload = function () {
    if (xhr.status === 200) {
      medicationDetails = JSON.parse(xhr.responseText); // Assign the fetched medication details to the global variable

      if (Array.isArray(medicationDetails) && medicationDetails.length > 0) {
        // Sort the medication details based on the selected sort option

        // console.log(currentPage)

        var startIndex = (currentPage - 1) * 10;
        var endIndex = startIndex + 10;
        
        if (startIndex < 0) {
          startIndex = 0; // Ensure startIndex is not negative
        }

        if (endIndex > medicationDetails.length) {
          endIndex = medicationDetails.length; // Ensure endIndex is within bounds
        }
          // Create a copy of the subset of medication details to be sorted
          var medicationSubset = medicationDetails.slice(startIndex, endIndex);

          if (sortOption === "priceAsc") {
            medicationSubset.sort(function (a, b) {
              return a.price_analysis - b.price_analysis;
            });
          } else if (sortOption === "priceDesc") {
            medicationSubset.sort(function (a, b) {
              return b.price_analysis - a.price_analysis;
            });
          }

        var detailsHtml = "";
        for (var i = 0; i < medicationSubset.length; i++) {
          var medication = medicationSubset[i];

          detailsHtml +=
            `
          <div class="card card-margin">
            <div class="row row-space">
              <div  class="my_coll" >
                <table class="table  widget-26">
                  <tbody>
                    <tr>
                      <td>
                        <div class="widget-26-job-title">
                          <a href="#">${medication.name.trim()}</a>
                          <p class="m-0">
                            <a href="#">${medication.dosage_form.trim()}.</a>
                          </p>
                        </div>
                      </td>
                      <td class="column-2">
                        <div class="widget-26-job-info">
                          <p class="type m-0">${medication.manufacturer.trim()}</p>
                          <a class="type m-0 employer-name">${medication.generic_name.trim()}.</a>
                        </div>
                      </td>`;
          if (medication.price !== '0') {
            detailsHtml += `<td class="column-3">
                              <div>
                                <p class="m-0 text-center Class">PRICE: ${medication.price.trim()} </p>
                              </div>
                            </td>`;
          } else {
            detailsHtml += `<td class="column-3">
                              <div class="widget-26-job-category">
                                <p class="m-0 text-center Class">PRICE DATA IS UNAVAILABLE</p>
                              </div>
                            </td>`;
          }
          detailsHtml += `</tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
                `;
        
        
        

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
  xhr.onerror = function () {
    console.error('Request failed. Network error');
    // Display "No data found" message for network errors
    document.getElementById("medicationDetails").innerHTML = "<p>No data found</p>";
  };
  xhr.send();
}

function calculateTotalPages(items) {
  var itemsPerPage = 10;
  var totalItems = items.length;
  return Math.ceil(totalItems / itemsPerPage);
}

function displayPage(pageNumber) {
  showPage(pageNumber);
}

var trackpage=0;
function showPage(pageNumber) {
  var totalPages = calculateTotalPages(medicationDetails);

  if(pageNumber===2){
    
    trackpage += pageNumber;
    pageNumber =1 + Math.floor(trackpage / 2);
    if(pageNumber>totalPages){
      pageNumber=totalPages;
      trackpage=totalPages*2-2;
    }

  }
  else if(pageNumber===0)
  {

    trackpage -= 2;
    pageNumber =1+ Math.floor(trackpage / 2);
    if(pageNumber<1){
      pageNumber=1;
      trackpage=0;
    }

  }
  
  else if(pageNumber ===991){
    pageNumber=1+ Math.floor(trackpage / 2);
  }else if (pageNumber >0 && pageNumber < 991){
    trackpage = (pageNumber-1)*2;
    pageNumber =1+ Math.floor(trackpage / 2);
  }
  else if (pageNumber > totalPages) {
    pageNumber = totalPages;
  } else if (pageNumber < 1) {
    pageNumber = 1;
  }
  



  function handleSortOptionChange() {
  var sortOption = document.getElementById("sortOption").value;
  return sortOption;
}

  if (pageNumber >= 1 && pageNumber <= totalPages) {
    var sortOption = handleSortOptionChange();
    fetchMedicationDetails(sortOption, pageNumber);
  }
}

function handleSortOptionChange() {
  showPage(991);
}


// Call this after fetching medicationDetails
fetchMedicationDetails('default', 1);
