import axios from 'axios';

/**
 * INSTALL axios
 * 
 * Method PUT
 * 
 * The function verifies if a token is saved in local storage and makes a request.
 *
 * @param {string} url - Endpoint URL (example: api/login, not necessarily localhost:8000).
 * @param {object} data - JSON data to send to the API.
 *
 * @returns {Promise} A Promise that resolves to a JSON result with { success: "yes"/"no", data/error: data/error }.
 *
 * @creator David
 */
function DataFetchPut(url, data) {
    // Append the base URL to the provided endpoint URL.
    url = 'http://localhost:8000/' + url;

    // Access the token saved in local storage; if it doesn't exist, return null.
    let token = localStorage.getItem("token");
        
    // With authentication and send JSON.
    if (token !== null) {
        return new Promise((resolve, reject) => {
            axios.put(url, data, {
                headers: {
                    Authorization: token
                }
            })
            .then(response => {
                resolve({ success: "yes", data: response['data'] });
            })
            .catch(error => {
                reject({ success: "no", error: error });
            });
        });
    }
    else {
        // Without authentication and send JSON.
        return new Promise((resolve, reject) => {
            axios.put(url, data)
            .then(response => {
                resolve({ success: "yes", data: response['data'] });
            })
            .catch(error => {
                reject({ success: "no", error: error });
            });
        });
    }
}

export default DataFetchPut;
