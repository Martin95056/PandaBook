package my.implementation;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

public class FileHolder {

	private BlockingQueue<Line> queue;
	private boolean areProducersDone;

	public FileHolder() {
		queue = new LinkedBlockingQueue<Line>();
		areProducersDone = false;
	}

	public void add(Line data) {
		synchronized (queue) {
			queue.add(data);
			queue.notify();
		}
	}

	public boolean isEmpty() {
		return queue.isEmpty();
	}

	public Line get() {
		synchronized (queue) {
			while (queue.isEmpty()) {
				try {
					queue.wait();
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
			return queue.poll();
		}
	}

	public boolean isProducingFinished() {
		return areProducersDone;
	}

	// stop program
	public void setFinished() {
		this.areProducersDone = true;
	}
}
