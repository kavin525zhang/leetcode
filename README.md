### [283.移动零](https://leetcode-cn.com/problems/move-zeroes/)
* [方法一](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v1.py)
> 思路：从末尾开始遍历，遇到0，则将后面非0数往前移
* [方法二](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/mine_v2.py)
> 思路：遍历所有元素，遇到0，则删除，同时记录删除0个数，最后在末尾加上相同数目0
* [官方版本](https://github.com/kavin525zhang/leetcode/blob/main/source_code/283.%E7%A7%BB%E5%8A%A8%E9%9B%B6/sota.py)
> 思路：从头开始遍历，采用双指针，左指针要么与右指针相同，要么指向0，所以当右指针遇到不等于0的数，直接与左指针数对调      
> 时间复杂度：O(n), 空间复杂度：O(1)

### [287.寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)
* [方法一](https://github.com/kavin525zhang/leetcode/tree/main/source_code/287.寻找重复数/mine_v1.py)
> 思路：方法来源于一个严格的限制条件， 在n + 1的列表中只会出现1~n的数，因此元素值一定在列表的下标中，结合元素和下标，遍历所有元素， 当元素对应的下标位置元素小于n + 1时， 说明第一次出现， 在相应位置增加n + 1,大于 n + 1时说明出现过一次,即为重复数，返回
* [官方版本：快慢指针](https://github.com/kavin525zhang/leetcode/tree/main/source_code/287.寻找重复数/sota_v1.py)

快慢指针相关题目：

* [141.环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)
* [142.环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)

### [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)
* [方法一](https://github.com/kavin525zhang/leetcode/blob/main/source_code/216.%20%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%20III/mine_v1.py)

### [1392. 最长快乐前缀](https://leetcode-cn.com/problems/longest-happy-prefix/)
* [方法一](https://github.com/kavin525zhang/leetcode/blob/main/source_code/1392.%20%E6%9C%80%E9%95%BF%E5%BF%AB%E4%B9%90%E5%89%8D%E7%BC%80/mine_v1.py)
> 思路：最开始做成回文了， 一个正常的思路是从头往后遍历， 当字符等于最后一个字符时，比较一下包含当前字符的之前的字符串是否等于末尾相同长度的字符串，等于即为快乐前缀， 然后继续往后判断， 注意不能是整个字符串
* [官方版本：Rabin-Karp 字符串编码](https://leetcode-cn.com/problems/longest-happy-prefix/solution/zui-chang-kuai-le-qian-zhui-by-leetcode-solution/)
> 思路：官方的解答为什么比我时间复杂度低的原因是，我需要去判断字符串相不相等， 而它将其编码为整数

### [1943. 描述绘画结果](https://leetcode-cn.com/problems/describe-the-painting/)
* [官方版本：差分 + 前缀和](https://leetcode-cn.com/problems/describe-the-painting/solution/miao-shu-hui-hua-jie-guo-by-leetcode-sol-tnvy/)

### [1331. 数组序号转换](https://leetcode-cn.com/problems/rank-transform-of-an-array/) 简单
* [方法一]()

### [1654. 到家的最少跳跃次数](https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/)

### [1544. 整理字符串](https://leetcode-cn.com/problems/make-the-string-great/) 简单


