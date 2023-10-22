import axios from 'axios'
/**
 * INSTALL axios
 * 
 * METHOD: GET
 * The function verify if token saved in local storage and make request
 * @param {*} url endpoint url (example:api/creators, not necessary localhost:8000)
 * @param {*} data if necessary set data
 * @returns json result with {success:"yes"/"no", data/error:data/error}
 * 
 * @creator David
 */
function DataFetchGet(url,data=null) {
    url='http://localhost:8000/' + url;

    //access token saved in local storage, if it doesn't exists return null
    let token=localStorage.getItem("token")

    //with authentication token
    if (token!=null){
        //if the data is not valid then the function makes a GET request with no additional parameters
        if (data==null){
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    headers:{
                        Authorization:token
                    }
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
        })}
        //if the data is valid then the function will make a GET request and pass the object
        //data as the query parameters
        else{
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    headers:{
                        Authorization:token
                    },
                    params:data
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
            })}
        }
    //without authentication token
    else{
        //if the data is null
        if (data==null){
            return new Promise((resolve,reject)=>{
                axios.get(url)
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
        })}
        //if the data isn't null
        else{
            return new Promise((resolve,reject)=>{
                axios.get(url,{
                    params:data
                })
                .then(response=>{resolve({success:"yes",data:response['data']})})
                .catch(error=>{reject({success:"no",error:error})});
            })}
    }
}
export default DataFetchGet;

