<?php

$uriSegments = explode("/", parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
$lastUriSegment = array_pop($uriSegments);

function ifURLLastSegment($pattern, $output)
{
    global $uriSegments, $lastUriSegment;
    
    if ($lastUriSegment === $pattern)
    {
        echo $output;
    }
}

?>
