package priorityqueue;

import java.util.Objects;

/* A PriorityQueue class that uses a min heap to maintain ordering. */
public class MinHeapPQ<T> implements PriorityQueue<T> {

    /* The heap backing our MinHeapPQ. */
    private MinHeap<PriorityItem<T>> heap;

    /* Initializes an empty MinHeapPQ. */
    public MinHeapPQ() {
        heap = new MinHeap<PriorityItem<T>>();
    }

    /* Returns the item with the smallest priority value, but does not remove it
       from the MinHeapPQ. */
    public T peek() {
        return heap.findMin().item;
    }

    /* Inserts ITEM with the priority value PRIORITYVALUE into the MinHeapPQ. If
       ITEM is already in the MinHeapPQ, throw an IllegalArgumentException. */
    public void insert(T item, double priorityValue) {
        PriorityItem<T> p = new PriorityItem<>(item, priorityValue);
        heap.insert(p);
    }

    /* Returns the item with the highest priority (smallest priority value), and
       removes it from the MinHeapPQ. */
    public T poll() {
        return heap.removeMin().item;
    }

    /* Changes the PriorityItem with item ITEM to have priority value
       PRIORITYVALUE. Assume the items in the MinHeapPQ are all unique. If ITEM
       is not in the MinHeapPQ, throw a NoSuchElementException. */
    public void changePriority(T item, double priorityValue) {
        PriorityItem<T> p = new PriorityItem<>(item, priorityValue);
        heap.update(p);
    }

    /* Returns the number of items in the MinHeapPQ. */
    public int size() {
        return heap.size();
    }

    /* Returns true if ITEM is stored in our MinHeapPQ. Note: Any priority value
       for this dummy PriorityItem would work. */
    public boolean contains(T item) {
        return heap.contains(new PriorityItem<T>(item, 0));
    }

    @Override
    public String toString() {
        return heap.toString();
    }

    /* A wrapper class that stores items and their associated priorities.

       Note: This class has a natural ordering that is inconsistent with
       equals. */
    public static class PriorityItem<T> implements Comparable<PriorityItem<T>> {
        private T item;
        private double priorityValue;

        private PriorityItem(T item, double priorityValue) {
            this.item = item;
            this.priorityValue = priorityValue;
        }

        public T item() {
            return this.item;
        }

        public double priorityValue() {
            return this.priorityValue;
        }

        @Override
        public String toString() {
            return "(PriorityItem: " + this.item.toString() + ", "
                    + this.priorityValue + ")";
        }

        @Override
        public int compareTo(PriorityItem<T> o) {
            // double diff = this.priorityValue - o.priorityValue;
            // if (diff > 0) {
            //     return 1;
            // } else if (diff < 0) {
            //     return -1;
            // } else {
            //     return 0;
            // }
            return Double.compare(this.priorityValue, o.priorityValue);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            PriorityItem<?> that = (PriorityItem<?>) o;

            return Double.compare(that.priorityValue, priorityValue) == 0
                    && (item == null ? that.item == null : item.equals(that.item));
        }

        @Override
        public int hashCode() {
            return Objects.hash(item, priorityValue);
        }
    }
}

