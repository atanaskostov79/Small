<?php

$url = "https://www.bgelectronics.eu/index.php?route=feed/products_json/getData&langluage=bg";


$ch = curl_init();
			curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
			curl_setopt($ch, CURLOPT_HEADER, false);
			curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
			curl_setopt($ch, CURLOPT_URL, $url);
			curl_setopt($ch, CURLOPT_REFERER, $url);
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
			$result = curl_exec($ch);
			curl_close($ch);
		    // print_r (json_decode($result,true));
			$txt = json_decode($result,true);
            echo json_encode($result, true);
        //  file_put_contents('myfile.json', $txt);

        //     $myfile = fopen("newfile.json", "w") or die("Unable to open file!");

            // fwrite($myfile, $txt);
            // fclose($myfile);
          
            $arr = array('a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5);

            echo json_encode($arr);

            ?>