package priorityqueue;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

/**
 * Represents a task with a description, due date, and priority.
 * The priority is used to determine the urgency of the task,
 * with lower values indicating higher priority.
 */
public class Task {
    private String description;
    private LocalDate dueDate;
    private double priority; // Lower values indicates higher priority

    /**
     * Constructs a new Task with the specified description, due date, and priority.
     *
     * @param description The description of the task.
     * @param dueDate     The due date of the task.
     * @param priority    The priority of the task, with lower values indicating higher priority.
     */
    public Task(String description, LocalDate dueDate, double priority) {
        this.description = description;
        this.dueDate = dueDate;
        this.priority = priority;
    }

    /**
     * Calculates the priority based on the number of days until the due date.
     * Priority is the number of days until the task is due, with today counting as zero.
     *
     * @param dueDate The due date of the task.
     * @return The calculated priority based on the due date.
     */
    public double calculatePriority(LocalDate dueDate) {
        long daysUntilDue = LocalDate.now().until(dueDate, ChronoUnit.DAYS);
        return daysUntilDue;
    }

    public String getDescription() {
        return this.description;
    }

    public LocalDate getDueDate() {
        return this.dueDate;
    }

    public double getPriority() {
        return this.priority;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setLocalDate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public void setPriority(double priority) {
        this.priority = priority;
    }

    /**
     * Returns a string representation of the Task, including its description,
     * due date, and priority.
     *
     * @return A string representation of the Task.
     */
    @Override
    public String toString() {
        return "Task{" +
               "description='" + this.description + '\'' +
               ", dueDate=" + dueDate + 
               ", priority=" + priority + 
               '}';
    }
}
