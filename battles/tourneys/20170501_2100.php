<?php

include("ttest.php");

function gcd($a, $b) {
    if ($b == 0) {
        return $a;
    } else {
        return gcd($b, $a % $b);
    }
}

function fractionReducing($fraction) {
    $g = gcd($fraction[0], $fraction[1]);
    return [$fraction[0] / $g, $fraction[1] / $g];
}


mytest(fractionReducing([2,6]), [1,3]);


?>
