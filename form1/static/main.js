document.addEventListener("DOMContentLoaded", () => {
    var editButton = document.getElementById("editButton");
    var saveButton = document.getElementById("saveButton");
    var cancelButton = document.getElementById("cancelButton");
    var dropdownMenuButton = document.getElementById("dropdownMenuButton1");

    // Function to toggle edit, save, and cancel buttons
    function toggleButtons(showEdit) {
        if (showEdit) {
            editButton.style.display = "";
            saveButton.style.display = "none";
            cancelButton.style.display = "none";
        } else {
            editButton.style.display = "none";
            saveButton.style.display = "";
            cancelButton.style.display = "";
        }
    }

    // Function to reset the dropdown value to "Select ID"
    function resetDropdown() {
        dropdownMenuButton.textContent = "Select ID";
    }

    // Function to update dropdown text and toggle buttons
    function selectDropdownItem(value) {
        dropdownMenuButton.textContent = value;
        toggleButtons(false);
    }

    // Add click event listeners to the saveButton and cancelButton
    saveButton.addEventListener("click", function () {
        resetDropdown();
        toggleButtons(true);
    });

    cancelButton.addEventListener("click", function () {
        resetDropdown();
        toggleButtons(true);
    });

    // Attach event listeners to dropdown items
    document.querySelectorAll(".dropdown-item").forEach((item) => {
        item.addEventListener("click", function () {
            selectDropdownItem(this.textContent);
        });
    });
});

let stars = document.getElementsByClassName("star");
let output = document.getElementById("output");

// Funtion to update rating
function fun(n) {
    remove();
    for (let i = 0; i < n; i++) {
        stars[i].className = "star " + "star_color";
    }
    const hiddenInput = document.getElementById("rating");
    hiddenInput.value = n;
    console.log("one");
}

// To remove the pre-applied styling
function remove() {
    let i = 0;
    while (i < 5) {
        stars[i].className = "star";
        i++;
    }
}
