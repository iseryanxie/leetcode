/**
 * Definition for a binary tree node.
 */
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	inorderArray := []int{}
	if root == nil {
		return []int{}
	}
	if root.Left != nil {
		inorderArray = append(inorderArray, inorderTraversal(root.Left)...)
	}
	inorderArray = append(inorderArray, root.Val)
	if root.Right != nil {
		inorderArray = append(inorderArray, inorderTraversal(root.Right)...)
	}
	return inorderArray
}

func main() {
	node3 := TreeNode{Val: 3}
	node2 := TreeNode{Val: 2, Left: &node3}
	node1 := TreeNode{Val: 1, Right: &node2}
	fmt.Println(inorderTraversal(&node1))
}
