<?php

include("../../mytest.php");

function centuryFromYear($year) {
    return 1 + floor(($year - 1) / 100);
}

mytest(centuryFromYear(1905), 20);
mytest(centuryFromYear(1900), 19);
mytest(centuryFromYear(2000), 20);
mytest(centuryFromYear(1), 1);
