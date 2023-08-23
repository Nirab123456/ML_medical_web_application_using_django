
  // Retrieve the query parameters from the URL
  const urlParams = new URLSearchParams(window.location.search);
  const drugName = urlParams.get('name');
  const generic_name = urlParams.get('generic_name');

  


// Make an AJAX call to fetch the medication details based on the selected strength, dosage form, and drug name
var xhr = new XMLHttpRequest();
if(!generic_name){
xhr.open('GET', '/get_medicine_details/?name=' + drugName, true);
}else{
  xhr.open('GET', '/get_medicine_details_generic/?generic_name=' + generic_name, true);
}
xhr.onload = function() {
if (xhr.status === 200) {
    var get_medicine_details = JSON.parse(xhr.responseText);
    if (Array.isArray(get_medicine_details) && get_medicine_details.length > 0) {

    // Display details for each medication
    var detailsHtml = "";
    for (var i = 0; i < get_medicine_details.length; i++) {
        var medication = get_medicine_details[i];
        detailsHtml += 
        
        `
        <div class="medication-table">
            <table>
                <tbody>
                    <tr>
                        <td><strong>Generic Name:</strong></td>
                        <td>${medication.generic_name}</td>
                    </tr>
                    <tr>
                        <td><strong>DRUG CLASS:</strong></td>
                        <td>${medication.drug_class}</td>
                    </tr>
                    <tr>
                        <td><strong>INDICATION DESCRIPTION:</strong></td>
                        <td>${medication.indication_description}</td>
                    </tr>
                    <tr>
                        <td><strong>Indication:</strong></td>
                        <td>${medication.indication}</td>
                    </tr>
                    <tr>
                        <td><strong>PHARMACOLOGY DESCRIPTION:</strong></td>
                        <td>${medication.pharmacology_description}</td>
                    </tr>
                    <tr>
                        <td><strong>THERAPEUTIC CLASS:</strong></td>
                        <td>${medication.therapeutic_class_description}</td>
                    </tr>
                    <tr>
                        <td><strong>DOSAGE DESCRIPTION:</strong></td>
                        <td>${medication.dosage_description}</td>
                    </tr>
                    <tr>
                        <td><strong>INTERACTIONS DESCRIPTION:</strong></td>
                        <td>${medication.interaction_description}</td>
                    </tr>
                    <tr>
                        <td><strong>CONTRAINDICATIONS DESCRIPTION:</strong></td>
                        <td>${medication.contraindications_description}</td>
                    </tr>
                    <tr>
                        <td><strong>CONTRAINDICATIONS DESCRIPTION:</strong></td>
                        <td>${medication.contraindications_description}</td>
                    </tr>
                    <tr>
                        <td><strong>WARNINGS DESCRIPTION:</strong></td>
                        <td>${medication.side_effects_description}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        `;



        
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
