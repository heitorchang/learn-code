<?php

include("ttest.php");

function swapAdjacentWords($s) {
    $result = [];
    $words = explode(" ", $s);

    for ($i = 0; $i < ceil(count($words) / 2); $i++) {
        if (isset($words[2 * $i + 1])) {
            $result[] = $words[2 * $i + 1];
        }
        $result[] = $words[2 * $i];
    }
    return implode(" ", $result);
}

mytest(swapAdjacentWords("How are you today guys"), "are How today you guys");


?>
