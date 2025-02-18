class MedianFinder {
    // MedianFinder ob=new MedianFinder();
    PriorityQueue<Integer> low,high;
    public MedianFinder() {
        // ob=new MedianFinder();
        low=new PriorityQueue<>(Collections.reverseOrder());
        high=new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        low.offer(num);
        high.offer(low.poll());
        if(low.size()<high.size())
        {
            low.offer(high.poll());
        }
    }
    
    public double findMedian() {
        if(low.size()>high.size())
        {
            return (double)low.peek();
        }
        return (low.peek()+high.peek())/2.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */