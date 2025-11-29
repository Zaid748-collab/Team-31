function toggleReadMore(button) {
    const card = button.parentElement;
    const moreText = card.querySelector(".more-text");

    if (moreText.style.display === "inline") {
        moreText.style.display = "none";
        button.textContent = "Read More";
    } else {
        moreText.style.display = "inline";
        button.textContent = "Read Less";
    }
}

function addToBasket(itemName) {
    alert(itemName + " added to basket!");
    //  replace this with basket functionality.
}
