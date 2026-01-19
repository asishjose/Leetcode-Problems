class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        sorted_boxes = sorted(capacity, reverse=True)
        added = 0
        number_of_boxes = 0
        for cap in sorted_boxes:
            added+=cap
            number_of_boxes += 1
            if added >= total_apples:
                return number_of_boxes
