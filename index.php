
  <?php

// Function to convert PDF to HTML
function pdfToHtml($pdfPath, $htmlPath) {
    // Use the pdftohtml command from Poppler
    $command = "pdftohtml -c \"$pdfPath\" \"$htmlPath\"";
    
    // Execute the command
    exec($command, $output, $returnVar);
    
    // Check if the conversion was successful
    if ($returnVar === 0) {
        echo "Conversion successful!";
    } else {
        echo "Conversion failed. Check the error message: " . implode("\n", $output);
    }
}

// Example usage
$pdfFilePath = __DIR__.'/files/JS3.pdf';
$htmlFilePath = __DIR__.'/files/output.html';

pdfToHtml($pdfFilePath, $htmlFilePath);

?>
