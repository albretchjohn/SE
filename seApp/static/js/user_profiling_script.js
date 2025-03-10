
function nextStep() {
    const currentStep = document.querySelector('.form-step:not(.hidden)');
    const nextStep = currentStep.nextElementSibling;

    if (nextStep) {
        currentStep.classList.add('hidden');
        nextStep.classList.remove('hidden');
    }
}

function previousStep() {
    const currentStep = document.querySelector('.form-step:not(.hidden)');
    const previousStep = currentStep.previousElementSibling;

    if (previousStep) {
        currentStep.classList.add('hidden');
        previousStep.classList.remove('hidden');
    }
}

function toggleDropdown() {
    const dropdown = document.getElementById('dropdown_content');
    dropdown.classList.toggle('hidden');
}

function checkOtherCondition() {
    const otherCondition = document.getElementById('other_medical_condition');
    otherCondition.classList.toggle('hidden');
}

function checkAllergies() {
    const allergies = document.getElementById('allergies').value;
    const allergyDetails = document.getElementById('allergy_details');
    
    if (allergies === 'yes') {
        allergyDetails.classList.remove('hidden');
    } else {
        allergyDetails.classList.add('hidden');
    }
}

function checkForms(event) {  // Add event parameter here
    // Find all required form fields
    const requiredFields = document.querySelectorAll('input[required], select[required], textarea[required]');
    let hasEmptyRequiredField = false;
    
    // Check if any required field is empty
    for (let field of requiredFields) {
        // Check for empty value (handles most input types)
        if (!field.value.trim()) {
            hasEmptyRequiredField = true;
            break; // Stop checking as soon as we find one
        }
        
        // Special case for checkboxes and radio buttons
        if ((field.type === 'checkbox' || field.type === 'radio') && !field.checked) {
            hasEmptyRequiredField = true;
            break;
        }
    }
    
    // If any required field is empty, show alert and prevent submission
    if (hasEmptyRequiredField) {
        event.preventDefault(); 
        alert('Please fill all required form fields.');
        return false; // This helps prevent form submission when used with onclick
    }
    
    return true; // Allow the form to submit
}




