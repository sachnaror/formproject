document.addEventListener('DOMContentLoaded', () => {
    var editButton = document.getElementById('editButton');
    var saveButton = document.getElementById('saveButton');
    var cancelButton = document.getElementById('cancelButton');

    // Function to show edit button and hide save and cancel buttons
    function toggleButtons() {
        editButton.style.display = '';
        saveButton.style.display = 'none';
        cancelButton.style.display = 'none';
    }

    // Add click event listener to the editButton
    editButton.addEventListener('click', function () {
        // Hide the editButton
        editButton.style.display = 'none';

        // Show the saveButton and cancelButton
        saveButton.style.display = '';
        cancelButton.style.display = '';
    });

    // Add click event listeners to the saveButton and cancelButton
    saveButton.addEventListener('click', toggleButtons);
    cancelButton.addEventListener('click', toggleButtons);
});
