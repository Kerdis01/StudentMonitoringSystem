<?php

namespace QubengageSort\Tests;

use PHPUnit\Framework\TestCase;
use function QubengageSort\getSortedAttendance;

class TestSortAttendancePHP extends TestCase
{
    public function testGetSortedAttendance_returnsArrayWithSameNumberOfItems()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [10, 5, 8];
        
        $result = getSortedAttendance($items, $attendances);
        
        $this->assertCount(3, $result);
    }

    public function testGetSortedAttendance_sortsItemsByAttendanceDescending()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [10, 5, 8];
        
        $result = getSortedAttendance($items, $attendances);
        
        $this->assertEquals('Item 1', $result[0]['item']);
        $this->assertEquals('Item 3', $result[1]['item']);
        $this->assertEquals('Item 2', $result[2]['item']);
    }

    public function testGetSortedAttendance_handlesEmptyArrays()
    {
        $items = [];
        $attendances = [];
        
        $result = getSortedAttendance($items, $attendances);
        
        $this->assertEmpty($result);
    }

    public function testGetSortedAttendance_handlesDifferentArrayLengths()
    {
        $items = ['Item 1', 'Item 2', 'Item 3'];
        $attendances = [10, 5];
        
        $result = getSortedAttendance($items, $attendances);
        
        $this->assertCount(2, $result);
    }
}
