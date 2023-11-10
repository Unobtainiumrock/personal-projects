package priorityqueue;

public class TaskManager implements ITaskManager {
    private PriorityQueue<Task> taskQueue;
    private PriorityCalculator priorityCalculator;
    
    public TaskManager(PriorityCalculator priorityCalculator) {
        this.taskQueue = new MinHeapPQ<>();
        this.priorityCalculator = priorityCalculator;
    }

    @Override
    public void addTask(Task newTask) {
        // Need to rework the addding of tasks
        double priority = priorityCalculator.calculatePriority(newTask);
        newTask.setPriority(priority);
        taskQueue.insert(newTask, priority);
    }

    @Override
    public Task getNextTask() {
        return taskQueue.poll();
    }

    @Override
    public boolean removeTask(Task task) {
        // Implement this later.
        return true;
    }

    @Override
    public boolean updateTask(Task oldTask, Task newTask) {
        // Implement this later.
        return true;
    }

}
