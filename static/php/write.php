<html>
<p>We appreciate your feedback!</p>
<?php
function writeToFile() {
    $fHandle = fopen('static/js/test.txt', 'w');
    fwrite($fHandle, 'Hellloo');
    fclose($fHandle);
}
?>
</html>