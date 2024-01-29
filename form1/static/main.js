

document.addEventListener('DOMContentLoaded', () => {
    var editButton = document.getElementById('editButton');
    var saveButton = document.getElementById('saveButton');
    var cancelButton = document.getElementById('cancelButton');
    var dropdownMenuButton = document.getElementById('dropdownMenuButton1');

    // Function to show edit button and hide save and cancel buttons
    function toggleButtons() {
        editButton.style.display = '';
        saveButton.style.display = 'none';
        cancelButton.style.display = 'none';
    }

    // Function to check if an option has been selected in the dropdown
    function isOptionSelected() {
        // Check if the dropdown button has a valid selection
        // Assuming the default text is "Select ID" and changes when an option is selected
        return dropdownMenuButton.textContent.trim() !== "Select ID";
    }

    // Add click event listener to the editButton
    editButton.addEventListener('click', function () {
        if (isOptionSelected()) {
            // Hide the editButton
            editButton.style.display = 'none';

            // Show the saveButton and cancelButton
            saveButton.style.display = '';
            cancelButton.style.display = '';
        } else {
            alert("Sorry, please select an option from the dropdown.");
        }
    });

    // Add click event listeners to the saveButton and cancelButton
    saveButton.addEventListener('click', toggleButtons);
    cancelButton.addEventListener('click', toggleButtons);
});





