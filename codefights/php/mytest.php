<head>
    <style>
     .pass {
         color: #090;
         font-weight: bold;
     }

     .fail {
         color: #600;
         font-weight: bold;
     }
    </style>
</head>
<pre>

    <?php

    function mytest($testVal, $expectVal) {
        if (!isset($testVal)) {
            return 0;
        }
        print("Testing ");
        print_r($testVal);
        print(" expecting ");
        print_r($expectVal);
        print("\n");

        if ($testVal == $expectVal) {
            print("<span class='pass'>PASS</span>");
        }
        else {
            print("<span class='fail'>FAIL</span>");
        }
        print("\n");
        print("\n");
    }
    ?>

