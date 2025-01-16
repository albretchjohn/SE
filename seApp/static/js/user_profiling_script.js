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