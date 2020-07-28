<?php 
require __DIR__ . '/vendor/autoload.php';

use php-timer\src\Timer\Timer;

Timer::start();
$time=Timer::stop();
var_dump($time);
print
Timer::secondsToTimeString($time);


?>
