function toggleMatchingGroups() {
  var matchingGroups = document.querySelectorAll(".full-details");
  for (var i = 0; i < matchingGroups.length; i++) {
    matchingGroups[i].classList.toggle("hidden");
  }
}

// Attach the toggle function to the button's click event
var toggleButton = document.getElementById("toggleButton");
toggleButton.addEventListener("click", toggleMatchingGroups);

function handleSelectionChange() {
  var nameInputs = document.querySelectorAll("#name-container input");
    var drugNames = [];
    for (var i = 0; i < nameInputs.length; i++) {
      drugNames.push(encodeURIComponent(nameInputs[i].value));
    }

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
    // console.log(drugClassGroups);
    // console.log(allMachGroups);
    // console.log(allMachGroups2);
    // console.log(all_groups_uniques);

    if (Array.isArray(drugClassGroups) && drugClassGroups.length > 0) {
      // Display details for each medication
      var detailsHtml = "";
      if (all_groups_uniques) {
        detailsHtml += "<h4> ALL MATCHING GROUPS </h4>";
        detailsHtml += "<div class='medication-details'>";
        detailsHtml += "<p><strong>classified releted drugs: </strong>" + all_groups_uniques[0] + "</p>";
        detailsHtml += "<p><strong>ALL MATCHING HEADINGS: </strong>" + all_groups_uniques[1] + "</p>";
        detailsHtml += "<p><strong>ALL MATCHING SPECIFIC CLASS: </strong>" + all_groups_uniques[2] + "</p>";
        detailsHtml += "</div>";

    }

// i have to hide after this section

    if (allMachGroups2) {
      for (var i = 0; i < allMachGroups2.length; i++) {
        var medication = allMachGroups2[i];
        // console.log(medication);
        detailsHtml += "<div class='medication-details full-details hidden'>";
        detailsHtml += "<h6> DETAILED OBSERVATION OF MATCH </h6>";
        detailsHtml += "<p><strong>MATCHING COUPLE: </strong>" + medication.name1 + "&" + medication.name2 + "</p>";
        detailsHtml += "<h4> MACHING  ISSUES </h4>";

        if (medication.heading_matches && medication.specific_class_matches.length > 0) {
          detailsHtml += "<p><strong>SPECIFIC ISSUES: </strong>" + medication.specific_class_matches + "</p>";
        }
        else{
          detailsHtml += "<p><strong>PREDICTED ISSUES: </strong>" + medication.heading_matches + "</p>";
        }
        detailsHtml += "</div>";
      }
}


    if (allMachGroups) {
      for (var i = 0; i < allMachGroups.length; i++) {
        var medication = allMachGroups[i];
        detailsHtml += "<div class='medication-details full-details hidden'>";
        detailsHtml += "<p><strong>MATCHING COUPLE: </strong>" + medication.name1 + "&" + medication.name2 + "</p>";
        detailsHtml += "<h4> MACHING  ISSUES </h4>";

        if (medication.heading_matches && medication.specific_class_matches.length > 0) {
          detailsHtml += "<p><strong>SPECIFIC ISSUES: </strong>" + medication.specific_class_matches + "</p>";
        }
        else{
          detailsHtml += "<p><strong>PREDICTED ISSUES: </strong>" + medication.heading_matches + "</p>";
        }
        detailsHtml += "</div>";
      }
}


    for (var i = 0; i < drugClassGroups.length; i++) {
      var medication = drugClassGroups[i];
      if (medication.heading_matches && medication.specific_class_matches.length > 0) {
        detailsHtml += "<div class='full_matching_map medication-details'>";
        detailsHtml += "<p><strong>MATCHING DRUG: </strong>" + medication.name + "</p>";
        detailsHtml += "<p><strong>SPECIFIC ISSUES: </strong>" + medication.specific_class_matches + "</p>";
        detailsHtml += "</div>";
      }
      else{
        detailsHtml += "<div class='full_matching_map medication-details'>";
        detailsHtml += "<p><strong>MATCHING DRUG: </strong>" + medication.name + "</p>";
        detailsHtml += "<p><strong>PREDICTED ISSUES: </strong>" + medication.heading_matches + "</p>";
        detailsHtml += "</div>";
      }

    }





    detailsHtml += "</div>";

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

// handleSelectionChange();
