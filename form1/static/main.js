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

//next button from tab1 to go to tab2
document.getElementById('nextBButton').addEventListener('click', function () {
    window.location.href = 'tab2.html';
});


//search field suggestions
document.getElementById('iazxsggdd').addEventListener('input', function () {
    const inputField = this;
    const suggestionsPanel = document.getElementById('nameSuggestions');
    const searchTerm = inputField.value;

    if (searchTerm.length > 0) {
        fetch(`/tab1/?term=${searchTerm}`)
            .then(response => response.json())
            .then(data => {
                suggestionsPanel.innerHTML = ''; // Clear previous suggestions
                data.forEach(function (suggestedWord) {
                    const div = document.createElement('div');
                    div.innerHTML = suggestedWord;
                    div.addEventListener('click', function () {
                        inputField.value = suggestedWord; // Fill input with clicked suggestion
                        suggestionsPanel.innerHTML = ''; // Clear suggestions
                    });
                    suggestionsPanel.appendChild(div);
                });
                if (data.length > 0) {
                    suggestionsPanel.style.display = 'block';
                } else {
                    suggestionsPanel.style.display = 'none';
                }
            });
    } else {
        suggestionsPanel.innerHTML = '';
        suggestionsPanel.style.display = 'none';
    }
});

// Optional: Hide suggestions when clicking outside
document.addEventListener('click', function (e) {
    const suggestionsPanel = document.getElementById('nameSuggestions');
    if (e.target.id !== 'iazxsggdd') {
        suggestionsPanel.innerHTML = '';
        suggestionsPanel.style.display = 'none';
    }
});
