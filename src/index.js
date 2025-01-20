// index.js

// API URL
const apiURL = 'https://jsonplaceholder.typicode.com/users';

// Function to fetch data from the API
async function fetchData() {
    try {
        const response = await fetch(apiURL);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the function to fetch data
fetchData();
