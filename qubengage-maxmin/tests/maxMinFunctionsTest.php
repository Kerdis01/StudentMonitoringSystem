<?php

namespace QubengageMaxmin\Tests;

use PHPUnit\Framework\TestCase;
use function QubengageMaxmin\getMaxMin;

class maxMinFunctionsTest extends TestCase
{
    public function testWithValidInputAndDifferentAttendances()
    {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [10, 20, 30, 40];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 4 - 40', $max_min_items[0]);
        $this->assertEquals('Item 1 - 10', $max_min_items[1]);
    }

    public function testWithEmptyArraysExpectingEmptyStrings()
    {
        $items = [];
        $attendances = [];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('', $max_min_items[0]);
        $this->assertEquals('', $max_min_items[1]);
    }

    public function testWithEqualAttendancesExpectingFirstAndLast()
    {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [20, 20, 20, 20];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 1 - 20', $max_min_items[1]);
        $this->assertEquals('Item 4 - 20', $max_min_items[0]);
    }

    public function testWithUnequalArrayLengthsExpectingException()
    {
        $this->expectException(\InvalidArgumentException::class);
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [20, 20];
        getMaxMin($items, $attendances);
    }

    public function testWithNegativeAttendances()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [-10, -20, -30];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 1 - -10', $max_min_items[0]);
        $this->assertEquals('Item 3 - -30', $max_min_items[1]);
    }

    public function testWithSingleItem()
    {
        $items = ['Item 1'];
        $attendances = [10];
        $max_min_items = getMaxMin($items, $attendances);
        $this->assertEquals('Item 1 - 10', $max_min_items[0]);
        $this->assertEquals('Item 1 - 10', $max_min_items[1]);
    }
}
