### [283.移动零](https://github.com/kavin525zhang/leetcode/tree/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6)
* [方法一](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v1.py)
> 思路：从末尾开始遍历，遇到0，则将后面非0数往前移
* [方法二](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v2.py)
> 思路：遍历所有元素，遇到0，则删除，同时记录删除0个数，最后在末尾加上相同数目0
* [官方版本](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/sota.py)
> 思路：从头开始遍历，采用双指针，左指针要么与右指针相同，要么指向0，所以当右指针遇到不等于0的数，直接与左指针数对调      
> 时间复杂度：O(n), 空间复杂度：O(1)

### [287.寻找重复数](https://github.com/kavin525zhang/leetcode/tree/main/source_code/287.寻找重复数/README.md)
* [方法一](https://github.com/kavin525zhang/leetcode/tree/main/source_code/287.寻找重复数/mine_v1.py)
> 思路：方法来源于一个严格的限制条件， 在n + 1的列表中只会出现1~n的数，因此元素值一定在列表的下标中，结合元素和下标，遍历所有元素， 当元素对应的下标位置元素小于n + 1时， 说明第一次出现， 在相应位置增加n + 1,大于 n + 1时说明出现过一次,即为重复数，返回
* [官方版本：快慢指针](https://github.com/kavin525zhang/leetcode/tree/main/source_code/287.寻找重复数/sota_v1.py)

快慢指针相关题目：

* [141.环形链表](https://github.com/kavin525zhang/leetcode/blob/main/source_code/141.%20%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8/%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0.md)
* [142.环形链表 II](https://github.com/kavin525zhang/leetcode/blob/main/source_code/142.%20%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8%20II/%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0.md)
