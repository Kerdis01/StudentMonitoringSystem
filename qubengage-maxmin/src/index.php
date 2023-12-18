<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
use function QubengageMaxmin\getMaxMin;

$output = array(
    "error" => false,
    "items" => "",
    "attendance" => 0,
    "max_item" => "",
    "min_item" => ""
);

try {
    $item_1 = $_REQUEST['item_1'];
    $item_2 = $_REQUEST['item_2'];
    $item_3 = $_REQUEST['item_3'];
    $item_4 = $_REQUEST['item_4'];
    $attendance_1 = $_REQUEST['attendance_1'];
    $attendance_2 = $_REQUEST['attendance_2'];
    $attendance_3 = $_REQUEST['attendance_3'];
    $attendance_4 = $_REQUEST['attendance_4'];

    $items = array($item_1, $item_2, $item_3, $item_4);
    $attendances = array($attendance_1, $attendance_2, $attendance_3, $attendance_4);

    // Validate the inputs
    foreach ($attendances as $attendance) {
		if (!is_numeric($attendance)) {
			throw new InvalidArgumentException("All attendance values must be numeric.");
		}
		if ($attendance < 0) {
			throw new InvalidArgumentException("All attendance values must be positive.");
		}
	}

    $max_min_items = getMaxMin($items, $attendances);

    $output['items'] = $items;
    $output['attendance'] = $attendances;
    $output['max_item'] = $max_min_items[0];
    $output['min_item'] = $max_min_items[1];

} catch (InvalidArgumentException $ex) {
    $output['error'] = true;
    $output['max_item'] = "Error: " . $ex->getMessage();
} catch (LengthException $ex) {
    $output['error'] = true;
    $output['max_item'] = "Error: " . $ex->getMessage();
} catch (Exception $ex) {
    $output['error'] = true;
    $output['max_item'] = "An unexpected error occurred.";
}

echo json_encode($output);
exit();
