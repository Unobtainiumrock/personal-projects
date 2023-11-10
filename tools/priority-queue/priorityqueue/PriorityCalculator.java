package priorityqueue;

public interface PriorityCalculator {
    /**
     * Calculates the priority for a given task.
     *
     * @param task The task for which to calculate the priority.
     * @return The calculated priority.
     */
    double calculatePriority(Task task);
}
