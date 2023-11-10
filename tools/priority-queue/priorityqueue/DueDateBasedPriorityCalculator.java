package priorityqueue;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class DueDateBasedPriorityCalculator implements PriorityCalculator {

    @Override
    public double calculatePriority(Task task) {
        LocalDate dueDate = task.getDueDate();
        long daysUntilDue = LocalDate.now().until(dueDate, ChronoUnit.DAYS);
        return daysUntilDue;
    }
}
