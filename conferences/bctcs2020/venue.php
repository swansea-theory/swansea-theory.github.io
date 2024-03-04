<?php
  $title="Venue";
  include ("partials/header.php");
?>

<div class="container">
  <div class="row">
    <div class="col">
      <h1 class="display-3 text-center my-5">Conference Venue</h1>
      <h2>Location</h2>
      <p>The event will be held in the Computational Foundry building of Swansea University.</p>

      <div class="card">
        <div class="card-header">
          Address
        </div>
        <div class="card-body">      
          Computational Foundry,<br>
          Bay Campus,<br>
          Swansea University,<br>
          Swansea,<br>
          SA1 8EN,<br>
          United Kingdom.
        </div>
      </div>

      <center class="mt-4 mb-4">
        <div class="mapouter">
          <div class="gmap_canvas">
            <iframe width="100%" height="500" id="gmap_canvas" src="https://maps.google.com/maps?q=Computatioanl%20Foundry%2C%20Swansea%20University%2C%20Bay%20Campus%2C%20Fabian%20Way%2C%20Skewen%2C%20SA1%208EN&t=&z=15&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
          </div>
          <style>.mapouter{position:relative;text-align:right;height:500px;width:100%;}.gmap_canvas {overflow:hidden;background:none!important;height:500px;width:100%;}</style>
        </div>
      </center>

      <h2>Travel</h2>
      
      <h3>Local Bus Services</h3>
      <p>There are various bus services you could use to arrive to Bay Campus, mostly opperated by First Cymru. The services mentioned bellow all terminate at Bay Campus, directly opposite of the Computational Foundry. Tickets can be purchased onboard the buses, which accept card and contact less payments.</p>

      <p>If you are leaving the same day, it may be worth purchasing a two-way ticket, which is often cheaper than other alternatives, however is bound to the same route in both directions, and it's price varies depending on the start and end points.</p>
      
      <p>If you would like some more flexibility, you can purchase an "Adult day ticket" for £4.70, which allows you to use any service operated by First Cymru in the Swansea Bay area, for the rest of the day.</p>

      <h3>Arriving By Train</h3>
      
      <p>If arriving by train, you could use unibus service 10 towards Bay Campus, which stops accross the road from the train station. This is a 24-hour service which runs every 15 minutes during the day.</p>

      <h3>Arriving By Bus</h3>
      <p>If arriving in Swansea Bus Station, you can use unibus service 8, which is a 24-hour service running every 20 minutes during the day from Stand E.</p>
    </div>
  </div>
</div>

<?php include ("partials/footer.php"); ?>