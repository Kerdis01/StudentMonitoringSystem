<?php
namespace QubengageMaxmin\Tests;

use PHPUnit\Framework\TestCase;
use function QubengageMaxmin\getMaxMin;

class maxMinFunctionsTest extends TestCase
{
    public function testMaxMinFunctionWithValidInput()
    {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [10, 20, 30, 40];

        $max_min_items = getMaxMin($items, $attendances);

        $this->assertEquals('Item 4 - 40', $max_min_items[0]);
        $this->assertEquals('Item 1 - 10', $max_min_items[1]);
    }

    public function testMaxMinFunctionWithEmptyArrays()
    {
        $items = [];
        $attendances = [];

        $max_min_items = getMaxMin($items, $attendances);

        $this->assertEmpty($max_min_items[0]);
        $this->assertEmpty($max_min_items[1]);
    }

    public function testMaxMinFunctionWithEqualAttendances()
    {
        $items = ['Item 1', 'Item 2', 'Item 3', 'Item 4'];
        $attendances = [20, 20, 20, 20];

        $max_min_items = getMaxMin($items, $attendances);

        $this->assertEquals('Item 4 - 20', $max_min_items[0]);
        $this->assertEquals('Item 1 - 20', $max_min_items[1]);
    }


    public function testMaxMinFunctionWithUnequalArrayLengths()
    {
        $this->expectException(\InvalidArgumentException::class);
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [20, 20];
        getMaxMin($items, $attendances);
    }
}

