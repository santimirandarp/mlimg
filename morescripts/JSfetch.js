const nodeFetch = require('node-fetch');
const {createApi} = require('unsplash-js');

const unsplash = createApi({
  //config object
  accessKey: 'zZaJ1hDXtarFT4ndOFoMJRCGgfFKa-rJju-P2VT_lNU',
  fetch: nodeFetch,
});

unsplash.search.getPhotos(
  { query: 'cat',
    page:1, //1
    perPage:30 //10
  }
)
  .then(result => {
  if (result.errors) {
    // handle error here
    console.log('error occurred: ', result.errors[0]);
  } else {
    // handle success here
    //retrieves an array of objects containing urls
    //then we can make a call to that url, 
    //and download images.
    const photo = result.response;
    console.log(photo);
  }
});
