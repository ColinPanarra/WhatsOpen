var database = firebase.database();

var openStoresRef = firebase.database().ref('stores/')
  openStoresRef.on('value', function(snapshot) {
    updateOpenStores(postElement, snapshot.val()); 
  })
