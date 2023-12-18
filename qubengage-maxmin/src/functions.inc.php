<?php
namespace QubengageMaxmin;

function getMaxMin($items, $attendances)
{
    // Error handling: Check if both parameters are arrays
    if (!is_array($items) || !is_array($attendances)) {
        throw new \InvalidArgumentException('Both items and attendances must be arrays.');
    }

    // Error handling: Check for empty arrays
    if (empty($items) || empty($attendances)) {
        // If either array is empty, return two empty strings as per test case.
        return ['', ''];
    }

    // Error handling: Check if the array sizes match
    if (count($items) !== count($attendances)) {
        throw new \LengthException('Arrays $items and $attendances must have the same length.');
    }

    $itemAttendances = [];
    foreach ($items as $i => $item) {
        $itemAttendances[] = ["item" => $item, "attendance" => $attendances[$i]];
    }

    usort($itemAttendances, function($a, $b) {
        return $b['attendance'] <=> $a['attendance'];
    });

    // Get the item with max attendance (first after sorting) and min attendance (last after sorting)
    $maxItem = $itemAttendances[0]['item'] . ' - ' . $itemAttendances[0]['attendance'];
    $minItem = end($itemAttendances)['item'] . ' - ' . end($itemAttendances)['attendance'];

    return [$maxItem, $minItem];
}
