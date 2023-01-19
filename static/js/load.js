function getQuoteLocal() {
  const quote = document.getElementById("quote");
  const author = document.getElementById("author");
  fetch("./static/js/tech_quotes.json")
    .then((response) => response.json())
    .then((data) => {
      const quoteData = data[Math.floor(Math.random() * data.length - 1)];
      quote.innerHTML = quoteData.quote;
      author.innerHTML = quoteData.author;
    });
}
