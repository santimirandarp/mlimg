import nodeFetch from 'node-fetch';
import {createApi} from 'unsplash-js';
const unsplash = createApi({
  accessKey: 'MY_ACCESS_KEY',
  fetch: nodeFetch,
});

unsplash.photos.get({ photoId: 'foo' }).then(result => {
  if (result.errors) {
    // handle error here
    console.log('error occurred: ', result.errors[0]);
  } else {
    // handle success here
    const photo = result.response;
    console.log(photo);
  }
});
