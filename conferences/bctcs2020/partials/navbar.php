<?php
  require_once('functions.php');
?>

<nav class="navbar navbar-expand-lg navbar-dark bg-uniblue sticky-top">  
  <a class="navbar-brand" href="https://www.swansea.ac.uk">
    <img src="images/uni_logo_600.png" width="100" class="d-inline-block d-lg-none align-middle" alt="Swansea University Logo">
    <img src="images/uni_logo_600.png" width="200" class="d-none d-lg-inline-block align-middle" alt="Swansea University Logo">
  </a>
  <a class="navbar-brand" href="http://cs.swansea.ac.uk/bctcs2020">
    <span class="mx-3">BCTCS 2020</span>
  </a>

  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item <?php ifURLLastSegment('', 'active'); ?>">
        <a class="nav-link" href="/bctcs2020">Home</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('zoom', 'active'); ?>">
        <a class="nav-link" href="zoom">Zoom Software</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('venue', 'active'); ?>">
        <a class="nav-link" href="venue">Venue</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('programme', 'active'); ?>">
        <a class="nav-link" href="programme">Programme</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('abstracts', 'active'); ?>">
        <a class="nav-link" href="abstracts">Talks</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('invitedspeakers', 'active'); ?>">
        <a class="nav-link" href="invitedspeakers">Invited Speakers</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('submission', 'active'); ?>">
        <a class="nav-link" href="submission">Talk Submission</a>
      </li>
      <li class="nav-item <?php ifURLLastSegment('registration', 'active'); ?>">
        <a class="nav-link" href="registration">Registration</a>
      </li>
    </ul>
  </div>
</nav>
