module.exports = {
  testingType: "e2e",
  video: false,

  e2e: {
    baseUrl: "https://jsonplaceholder.typicode.com",
    specPattern: '**/integration/*.js'
  },
};
