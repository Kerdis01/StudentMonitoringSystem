<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
use function QubengageSort\getSortedAttendance;

$output = array(
    "error" => false,
    "items" => "",
    "attendance" => 0,
    "sorted_attendance" => ""
);

try {
    // Assume that $_REQUEST will always have these indices set.
    // If not, you should add checks to handle missing indices.
    $items = array(
        $_REQUEST['item_1'],
        $_REQUEST['item_2'],
        $_REQUEST['item_3'],
        $_REQUEST['item_4']
    );
    $attendances = array(
        $_REQUEST['attendance_1'],
        $_REQUEST['attendance_2'],
        $_REQUEST['attendance_3'],
        $_REQUEST['attendance_4']
    );

    // Validate the inputs
    foreach ($attendances as $attendance) {
		if (!is_numeric($attendance)) {
			throw new InvalidArgumentException("All attendance values must be numeric.");
		}
		if ($attendance < 0) {
			throw new InvalidArgumentException("All attendance values must be positive.");
		}
	}

    // Now, call the getSortedAttendance function
    $sorted_attendance = getSortedAttendance($items, $attendances);

    $output['items'] = $items;
    $output['attendance'] = $attendances;
    $output['sorted_attendance'] = $sorted_attendance;

} catch (InvalidArgumentException $ex) {
    // Handle the case where an input is not valid
    $output['error'] = true;
    $output['sorted_attendance'] = "Error: " . $ex->getMessage();
} catch (Exception $ex) {
    // Handle any other exceptions
    $output['error'] = true;
    $output['sorted_attendance'] = "An unexpected error occurred.";
}

echo json_encode($output);
exit();