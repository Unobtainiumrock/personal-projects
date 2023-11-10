package priorityqueue;

public interface ITaskManager {
    void addTask(Task newTask);
    Task getNextTask();
    boolean removeTask(Task task);
    boolean updateTask(Task oldTask, Task newTask);
}