<?php
namespace QubengageMaxmin;

function getMaxMin($items, $attendances)
{
    if (empty($items) || empty($attendances)) {
        // If both arrays are empty, return two empty strings as per test case.
        return ['', ''];
    }

    if (count($items) !== count($attendances)) {
        // If array lengths are not equal, throw an exception as per test case.
        throw new \InvalidArgumentException('Arrays $items and $attendances must have the same length.');
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
