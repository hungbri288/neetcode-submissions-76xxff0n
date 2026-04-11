class Solution {
    public int largestRectangleArea(int[] heights) {
        int max = 0;
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (!stack.isEmpty() && stack.peek()[1] >= heights[i]) {
                int[] top = stack.pop();
                max = Math.max(max, top[1] * (i - top[0]));
                start = top[0];
            }
            stack.push(new int[] {start, heights[i]});
        }
        for (int[] top : stack) {
            max = Math.max(max, top[1] * (heights.length - top[0]));
        }
        return max;
    }
}
