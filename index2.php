<?php

// Function to convert PDF to HTML
function pdfToHtml($pdfPath, $outputDir) {
    // Use the pdftohtml command from Poppler
    $command = "pdftohtml -c \"$pdfPath\" \"$outputDir\"";
    
    // Execute the command and capture output
    exec($command, $output, $returnVar);
    
    // Check if the conversion was successful
    if ($returnVar === 0) {
        // Get the list of HTML files
        $htmlFiles = glob($outputDir . '/*.html');
        
        // Combine the contents of HTML files into one
        $combinedHtmlContent = '';
        foreach ($htmlFiles as $htmlFile) {
            $combinedHtmlContent .= file_get_contents($htmlFile);
        }
        
        // Return the combined HTML content
        return $combinedHtmlContent;
    } else {
        // Return an error message
        return "Conversion failed. Check the error message: " . implode("\n", $output);
    }
}

// Example usage
$pdfFilePath = __DIR__.'/files/JS3.pdf';
$outputDir = __DIR__.'/files/';

// Get combined HTML content from PDF
$htmlContent = pdfToHtml($pdfFilePath, $outputDir);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF to HTML</title>
</head>
<body>

<?php
// Output the combined HTML content
if (isset($htmlContent)) {
    echo $htmlContent;
} else {
    echo "Error converting PDF to HTML.";
}
?>

</body>
</html>
