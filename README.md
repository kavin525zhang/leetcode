### [283.移动零](https://github.com/kavin525zhang/leetcode/tree/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6)
* [方法一](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v1.py)
> 思路：从末尾开始遍历，遇到0，则将后面非0数往前移
* [方法二](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v2.py)
> 思路：遍历所有元素，遇到0，则删除，同时记录删除0个数，最后在末尾加上相同数目0
* [官方版本](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/sota.py)
> 思路：从头开始遍历，采用双指针，左指针要么与右指针相同，要么指向0，所以当右指针遇到不等于0的数，直接与左指针数对调      
> 时间复杂度：O(n), 空间复杂度：O(1)

### [287.寻找重复数]()
