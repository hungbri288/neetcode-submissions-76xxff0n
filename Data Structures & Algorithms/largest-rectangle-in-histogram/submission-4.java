class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int[] left = new int[n];
        int[] right = new int[n];
        int max = 0;
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            left[i] = -1;
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                left[i] = stack.peek();
            }
            stack.push(i);
        }

        stack.clear();

        for (int i = n - 1; i >= 0; i--) {
            right[i] = n;
            while (!stack.isEmpty() && heights[stack.peek()] >= heights[i]) {
                stack.pop();
            }
            if (!stack.isEmpty()) {
                right[i] = stack.peek();
            }
            stack.push(i);
        }

        for (int i = 0; i < n; i++) {
            left[i]++;
            right[i]--;
            max = Math.max(max, (right[i] - left[i] + 1) * heights[i]);
        }
        return max;
    }
}
