<?php
namespace QubengageSort;
function getSortedAttendance($items, $attendances) {
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
        throw new \LengthException('The number of items must match the number of attendances.');
    }

    foreach ($attendances as $attendance) {
      if (!is_numeric($attendance)) {
          throw new \InvalidArgumentException("All attendance values must be numeric.");
      }
      if ($attendance < 0) {
          throw new \InvalidArgumentException("All attendance values must be positive.");
      }
  }
    
    $item_attendances = array();
    for ($i = 0; $i < count($items); $i++) {
        $item_attendances_array = array("item" => $items[$i], "attendance" => $attendances[$i]);
        array_push($item_attendances, $item_attendances_array);
    }

    usort($item_attendances, function($a, $b) {
        return $b['attendance'] <=> $a['attendance'];
    });

    return $item_attendances;
}
