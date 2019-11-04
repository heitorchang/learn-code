<?php

include("../../mytest.php");

// define function here
function checkPalindrome($inputString) {
    return $inputString == strrev($inputString);
}


mytest(checkPalindrome("aabaa"), true);


?>
