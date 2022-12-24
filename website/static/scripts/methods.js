// Initialize and add the map
function initMap() {
    // Your location
    const loc = { lat: 42.361145, lng: -71.057083 };
    // Centered map on location
    const map = new google.maps.Map(document.querySelector('.map'), {
      zoom: 14,
      center: loc
    });
    // The marker, positioned at location
    const marker = new google.maps.Marker({ position: loc, map: map });
  }

  // Sticky menu background
  window.addEventListener('scroll', function() {
    var path = window.location.pathname;
    var page = path.split("/").pop();
    //to set different property of nav bar for home and gallery page
    var color = ""
    if(page == "gallery"){
      color = "#ec7ead"
    }
    console.log('scroll y : '+window.scrollY )
    if (window.scrollY > 95) {

      document.querySelector('#navbar').style.opacity = .8;
      this.document.querySelector('#navbar').style.background = "#ec7ead";
    } else {
    
      this.document.querySelector('#navbar').style.background= color;
      //document.querySelector('#navbar').style.opacity = 1;
    }
  });
  
  

 
  // Smooth Scrolling
  $('#navbar a, .btn').on('click', function(event) {
    if (this.hash === '#contact') {
      event.preventDefault();
  
      const hash = this.hash;
      console.log(hash)
      $('html, body').animate(
        {
          scrollTop: $(hash).offset().top - 100
        },
        800
      );
    }
  });