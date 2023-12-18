<?php
namespace QubengageSort\Tests;

use PHPUnit\Framework\TestCase;
use function QubengageSort\getSortedAttendance;

class SortTest extends TestCase
{
    public function testSortedEndpointIsRunning() {
        $url = "http://semsort.esha.qpc.hal.davecutting.uk/";
        $response = file_get_contents($url);
        $this->assertNotFalse($response, "The sorted endpoint is not running.");
    }
    
    public function testSortsItemsByAttendanceDescending()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [10, 5, 8];
        $expected = [
            ['item' => 'Item 1', 'attendance' => 10],
            ['item' => 'Item 3', 'attendance' => 8],
            ['item' => 'Item 2', 'attendance' => 5]
        ];

        $result = getSortedAttendance($items, $attendances);
        $this->assertEquals($expected, $result);
    }

    public function testHandlesArraysWithSingleElement()
    {
        $items = ['Item 1'];
        $attendances = [10];
        $expected = [['item' => 'Item 1', 'attendance' => 10]];

        $result = getSortedAttendance($items, $attendances);
        $this->assertEquals($expected, $result);
    }

    public function testSortIsStableForEqualAttendances()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [20, 20, 20];
        $expected = [
            ['item' => 'Item 1', 'attendance' => 20],
            ['item' => 'Item 2', 'attendance' => 20],
            ['item' => 'Item 3', 'attendance' => 20]
        ];

        $result = getSortedAttendance($items, $attendances);
        $this->assertEquals($expected, $result);
    }
}