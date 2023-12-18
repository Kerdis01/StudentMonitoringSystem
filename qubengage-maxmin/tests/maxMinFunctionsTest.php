<?php

namespace QubengageMaxmin\Tests;

use PHPUnit\Framework\TestCase;
use function QubengageMaxmin\getMaxMin;

class maxMinFunctionsTest extends TestCase
{
    public function testMaxMinEndpointIsRunning() {
        $url = "http://semmaxmin.esha.qpc.hal.davecutting.uk/";
        $response = file_get_contents($url);
        $this->assertNotFalse($response, "The maxmin endpoint is not running.");
    }
    
    public function testWithValidInputAndDifferentAttendances() {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [10, 20, 30, 40];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 4 - 40', $max_min_items[0]);
        $this->assertEquals('Item 1 - 10', $max_min_items[1]);
    }

    public function testWithEmptyArraysExpectingEmptyStrings() {
        $items = [];
        $attendances = [];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('', $max_min_items[0]);
        $this->assertEquals('', $max_min_items[1]);
    }

    public function testWithEqualAttendancesExpectingFirstAndLast() {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [20, 20, 20, 20];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 1 - 20', $max_min_items[0]);
        $this->assertEquals('Item 4 - 20', $max_min_items[1]);
    }

    public function testWithUnequalArrayLengthsExpectingException() {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [20, 20];
        getMaxMin($items, $attendances);
        $this->expectException(\InvalidArgumentException::class);
    }

    public function testWithNegativeAttendances() {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [-10, -20, -30];
        getMaxMin($items, $attendances);
        $this->expectException(\InvalidArgumentException::class);
        $this->expectExceptionMessage("All attendance values must be positive.");
    }

    public function testWithSingleItem() {
        $items = ['Item 1'];
        $attendances = [10];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 1 - 10', $max_min_items[0]);
        $this->assertEquals('Item 1 - 10', $max_min_items[1]);
    }
}
