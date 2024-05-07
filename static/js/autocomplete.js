let availableKeywords = [
  "Adani Ports and Special Economic Zone Ltd",
  "Asian Paints Ltd",
  "Axis Bank Ltd",
  "Bajaj Auto Ltd",
  "Bajaj Finserv Ltd",
  "Bajaj Finance Ltd",
  "Bharti Airtel Ltd",
  "Bharat Petroleum Corporation Ltd",
  "Britannia Industries Ltd",
  "Cipla Ltd",
  "Coal India Ltd",
  "Divi's Laboratories Ltd",
  "Dr. Reddy's Laboratories Ltd",
  "Eicher Motors Ltd",
  "Grasim Industries Ltd",
  "HCL Technologies Ltd",
  "HDFC Bank Ltd",
  "HDFC Life Insurance Company Ltd",
  "Hero MotoCorp Ltd",
  "Hindalco Industries Ltd",
  "Hindustan Unilever Ltd",
  "ICICI Bank Ltd",
  "IndusInd Bank Ltd",
  "Infosys Ltd",
  "ITC Ltd",
  "JSW Steel Ltd",
  "Kotak Mahindra Bank Ltd",
  "Larsen & Toubro Ltd",
  "Mahindra & Mahindra Ltd",
  "Maruti Suzuki India Ltd",
  "Nestle India Ltd",
  "NTPC Ltd",
  "Oil and Natural Gas Corporation Ltd",
  "Power Grid Corporation of India Ltd",
  "Reliance Industries Ltd",
  "State Bank of India",
  "SBI Life Insurance Company Ltd",
  "Shree Cement Ltd",
  "Sun Pharmaceutical Industries Ltd",
  "Tata Consultancy Services Ltd",
  "Tata Consumer Products Ltd",
  "Tata Motors Ltd",
  "Tata Steel Ltd",
  "Tech Mahindra Ltd",
  "Titan Company Ltd",
  "UltraTech Cement Ltd",
  "United Breweries Ltd",
  "Wipro Ltd",
  "Zee Entertainment Enterprises Ltd",
  "Adani Green Energy Ltd",
];

const resultsBox = document.querySelector(".result-box");
const inputBox = document.getElementById("search-bar");

inputBox.onkeyup = function () {
  let result = [];
  let input = inputBox.value;
  if (input.length) {
    result = availableKeywords.filter((keyword) => {
      return keyword.toLowerCase().includes(input.toLowerCase());
    });
    console.log(result);
  }
  display(result);
  if (!result.length) {
    resultsBox.innerHTML = "";
  }
};

function display(result) {
  const content = result.map((list) => {
    return "<li onclick = selectInput(this)>" + list + "</li>";
  });

  resultsBox.innerHTML = "<ul>" + content.join("") + "</ul>";
}
function selectInput(list) {
  inputBox.value = list.innerHTML;
  resultsBox.innerHTML = "";
}
function searchStocks() {
  // const searchTerm = document.getElementById("search-bar").value;
  // console.log("Search term:", searchTerm);
  const searchTerm = document.getElementById("search-bar").value;
  console.log("Search term:", searchTerm);
  if (searchTerm) {
    fetch("/report", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(searchTerm),
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        throw new Error("Network response was not ok.");
      })
      .then((data) => {
        console.log("Response from Flask:", searchTerm);
      })
      .catch((error) => {
        console.error("There was a problem with the fetch operation:", error);
      });
  }
  else {
    alert("Please enter a search term.");
  }
  // if (searchTerm) {
  //     const StockSearchTerm = encodeURIComponent(searchTerm);
  //     const stockURL = "https://www.google.com/search?q=" + StockSearchTerm;
  //     console.log("Stock URL:",stockURL);
  //     window.open(stockURL, '_blank');
  // } else {
  //     alert('Please enter a search term.');
  // }
}
// function searchStock() {
//     const stockName = document.getElementById('searchInput').value;
//     if (stockName) {
//         // Make an AJAX request to your Flask backend
//         const xhr = new XMLHttpRequest();
//         xhr.open('POST', '/report', true);
//         xhr.setRequestHeader('Content-Type', 'application/json');
//         xhr.onreadystatechange = function() {
//             if (xhr.readyState === XMLHttpRequest.DONE) {
//                 if (xhr.status === 200) {
//                     // Handle successful response
//                     console.log(xhr.responseText);
//                 } else {
//                     // Handle error
//                     console.error('Error:', xhr.statusText);
//                 }
//             }
//         };
//         const data = JSON.stringify({ stockName: stockName });
//         xhr.send(data);
//     } else {
//         alert('Please enter a stock name.');
//     }
// }
