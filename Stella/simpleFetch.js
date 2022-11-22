// const express = require('express')
// const app = express()

//const { response } = require("express");

// const port = 4567

// app.listen(port, () =>{
//     console.log('Listening on port ${port}')
// })

//import fetch from 'node-fetch';

const url1 ="https://vaseis.iee.ihu.gr/api/index.php/bases/?year=max";
//this request gives the maximum year that the API has data for
var currYear

(async() => {
  const getYear = async() =>{
    const response = await fetch(url1);
    const data = await response.json()
    currYear = data.maxYear;
    currYear = JSON.stringify(currYear);
    return currYear;
  }
  let year_local = await getYear();
  console.log(year_local);

  const url2 ="https://vaseis.iee.ihu.gr/api/index.php/bases/"+ year_local;
  //this request gives all the bases for every dept for the specific year

  fetch(url2)
    .then(data => {return data.json();})
    .then((objectData)=>{
      console.log(objectData)
      console.log(url2)
      })
      .catch(err => 'error');



})();

//const url3 = "https://vaseis.iee.ihu.gr/api/index.php/bases/2020/dept/1625";

// const url ='https://vaseis.iee.ihu.gr/api/bases/department/1625';
// const headers = {
//   "Content-Type": "application/json"
// }
// const data = {
//   "type": "gel-ime-gen"
// }

// fetch(url, { method: 'POST', headers: headers, body: data})
//   .then((res) => {
//      return res.json()
// })
// .then((json) => {
//    // Do something with the returned data.
//   console.log(json);

// });