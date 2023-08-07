function toggleMatchingGroups() {
  var matchingGroups = document.querySelectorAll(".full-details");
  for (var i = 0; i < matchingGroups.length; i++) {
    matchingGroups[i].classList.toggle("hidden");
  }
}

// Attach the toggle function to the button's click event
var toggleButton = document.getElementById("toggleButton");
toggleButton.addEventListener("click", toggleMatchingGroups);

function togglefullresults() {
  var full_result = document.querySelectorAll(".full-result");
  for (var i = 0; i < full_result.length; i++) {
    full_result[i].classList.toggle("hidden");
  }
}

var full_result_button = document.getElementById("full_result_button");
full_result_button.addEventListener("click", togglefullresults);






function handleSelectionChange() {
  const urlParams = new URLSearchParams(window.location.search);
  const drugNames = urlParams.get('name');

// Make an AJAX call to fetch the medication details based on the selected strength, dosage form, and drug name
var xhr = new XMLHttpRequest();
xhr.open('GET', '/get_presciption_classification_beta/?name=' + drugNames , true);
xhr.onload = function() {
  if (xhr.status === 200) {
    var get_presciption_classification = JSON.parse(xhr.responseText);

    // Assuming 'data' contains the JSON response from the server
    const drugClassGroups = get_presciption_classification.drug_class_groups;
    const allMachGroups = get_presciption_classification.all_mach_groups;
    const allMachGroups2 = get_presciption_classification.all_mach_groups_2;
    const all_groups_uniques = get_presciption_classification.all_matching_uniques;

    // // Now you can use these variables as needed
    console.log(all_groups_uniques);
    // console.log(allMachGroups);
    // console.log(allMachGroups2);
    // console.log(all_groups_uniques);

    if (Array.isArray(drugClassGroups) && drugClassGroups.length > 0) {
    // Display details for each medication
    var detailsHtml = '<div class="table medication-table">';
    var matchingGroupsFound = false;

    function areAllArraysEmpty(arr) {
      return arr.every(innerArr => innerArr.length === 0);
    }

    if (!areAllArraysEmpty(all_groups_uniques)) {
      matchingGroupsFound = true;
      detailsHtml += 
      `

      <div>
        <h3> ALL MATCHING GROUPS </h3>
        <h4>
      <p><strong>CLASSIFIED RELATED DRUGS: </strong>${all_groups_uniques[0]}</p>
      <p><strong>ALL MATCHING HEADINGS: </strong>${all_groups_uniques[1]}</p>
      
      `

      if (all_groups_uniques[2].length > 0) {
        detailsHtml += "<p><strong>ALL MATCHING SPECIFIC CLASS: </strong>" + all_groups_uniques[2] + "</p>";
      }
      detailsHtml += "</div></h4>";
    }

    if (!matchingGroupsFound) {
      detailsHtml += "<h3> NO MATCHING GROUPS </h3>";
    }

      

// i have to hide after this section

    if (allMachGroups2) {
      for (var i = 0; i < allMachGroups2.length; i++) {
        var medication = allMachGroups2[i];
        // console.log(medication);
        detailsHtml += `
        
        <div class='medication-details full-details hidden'>
        <h3 style="margin-top: 10px;">SPECEFIC DETAILED OBSERVATION OF MATCH <h3>
            <h4>
        <p><strong>MATCHING COUPLE: </strong> ${medication.name1} & ${medication.name2}</p>
        
        `

        if (medication.heading_matches && medication.specific_class_matches.length > 0) {
          detailsHtml += "<p><strong>SPECIFIC ISSUES: </strong>" + medication.specific_class_matches + "</p>";
        }
        else{
          detailsHtml += "<p><strong>PREDICTED ISSUES: </strong>" + medication.heading_matches + "</p>";
        }
        detailsHtml += "</div></h4>";
      }
}


    if (allMachGroups) {
      for (var i = 0; i < allMachGroups.length; i++) {
        var medication = allMachGroups[i];
        detailsHtml += `<div class='medication-details full-details hidden'>
        <h3 style="margin-top: 10px;"> DETAILED OBSERVATION OF MATCH </h3>
        <h4>
        <p><strong>MATCHING COUPLE: </strong>${medication.name1} & ${medication.name2}</p>`

        if (medication.heading_matches && medication.specific_class_matches.length > 0) {
          detailsHtml += "<p><strong>SPECIFIC ISSUES: </strong>" + medication.specific_class_matches + "</p>";
        }
        else{
          detailsHtml += "<p><strong>PREDICTED ISSUES: </strong>" + medication.heading_matches + "</p>";
        }
        detailsHtml += "</div></h4>";
      }
}

var all_headings = new Set(); // Move the declaration outside the loop
detailsHtml += `
<div class='full-result hidden'>
    <h3 style="margin-top: 10px;"> INDEVISUAL RESULTS </h3>


`

for (var i = 0; i < drugClassGroups.length; i++) {
  var medication = drugClassGroups[i];

  if (medication.heading && medication.specific_class.length > 0) {
    var headings = medication.heading.split(",");
    var specificClasses = medication.specific_class.split(",");

    for (var j = 0; j < headings.length; j++) {
      var heading_matches = headings[j].toUpperCase();
      var specific_class_matches = specificClasses[j].toUpperCase();
      console.log(specific_class_matches);
      all_headings.add(specific_class_matches);
    }
  } else {
    var heading_matches = headings[j].toUpperCase();
    var specific_class_matches = specificClasses[j].toUpperCase();
    all_headings.add(heading_matches);
  }

  detailsHtml += `
  
  
  <div  class='full-result medication-details hidden'>
    <h4>
  <p><strong>DRUG NAME: </strong>${medication.name.toUpperCase()}</p>
  <p><strong>HEADINGS: </strong>${Array.from(all_headings)}</p>
  </h4>
  </div>`;
}





    detailsHtml += `</div>
    
    </div>`;

    // Display the details on the page
    document.getElementById("get_presciption_classification").innerHTML = detailsHtml;
  } else {
    console.error(xhr.responseText);
  }

  } else {
    console.error(xhr.statusText);
  }

};
xhr.onerror = function() {
  console.error('Request failed. Network error');
  // Display "No data found" message for network errors
  document.getElementById("get_presciption_classification").innerHTML = "<p>No data found</p>";
};
xhr.send();
}
handleSelectionChange();
